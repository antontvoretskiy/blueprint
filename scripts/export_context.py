#!/usr/bin/env python3
"""Export ordered Blueprint context bundles from repository-owned files."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "context" / "export-manifest.json"
DEFAULT_PROFILE = "external-llm"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_manifest() -> dict[str, Any]:
    return json.loads(MANIFEST_PATH.read_text())


def git_value(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"
    return result.stdout.strip() or "unknown"


def documents_for_profile(manifest: dict[str, Any], profile: str) -> list[dict[str, Any]]:
    return [
        document
        for document in manifest.get("documents", [])
        if profile in document.get("profiles", [])
    ]


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    version = manifest.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"v\d+\.\d+\.\d+", version):
        errors.append("manifest version must use vX.Y.Z")

    profiles = manifest.get("profiles")
    if not isinstance(profiles, dict) or not profiles:
        errors.append("manifest must define profiles")
        profiles = {}
    for required_profile in ("external-llm", "chat-bootstrap"):
        if required_profile not in profiles:
            errors.append(f"manifest missing required profile `{required_profile}`")

    default_outputs = manifest.get("default_outputs")
    if not isinstance(default_outputs, dict):
        errors.append("manifest must define default_outputs")
        default_outputs = {}
    for profile in profiles:
        output = default_outputs.get(profile)
        if not isinstance(output, str) or not output.endswith(".md"):
            errors.append(f"profile `{profile}` must define a Markdown default output")
        elif not output.startswith(".blueprint/context/"):
            errors.append(f"profile `{profile}` output must stay under .blueprint/context/")

    documents = manifest.get("documents")
    if not isinstance(documents, list) or not documents:
        errors.append("manifest must define documents")
        return errors

    seen_ids: set[str] = set()
    for index, document in enumerate(documents, start=1):
        if not isinstance(document, dict):
            errors.append(f"document #{index} must be an object")
            continue
        document_id = document.get("id")
        if not isinstance(document_id, str) or not document_id:
            errors.append(f"document #{index} must define id")
        elif document_id in seen_ids:
            errors.append(f"duplicate document id `{document_id}`")
        else:
            seen_ids.add(document_id)

        raw_path = document.get("path")
        if not isinstance(raw_path, str) or not raw_path:
            errors.append(f"document `{document_id}` must define path")
        else:
            path = ROOT / raw_path
            if not path.exists():
                errors.append(f"document `{document_id}` references missing `{raw_path}`")
            elif not path.is_file():
                errors.append(f"document `{document_id}` path is not a file `{raw_path}`")

        document_profiles = document.get("profiles")
        if not isinstance(document_profiles, list) or not document_profiles:
            errors.append(f"document `{document_id}` must define profiles")
        else:
            for profile in document_profiles:
                if profile not in profiles:
                    errors.append(f"document `{document_id}` references unknown profile `{profile}`")

        for field in ("title", "purpose"):
            if not isinstance(document.get(field), str) or not document[field].strip():
                errors.append(f"document `{document_id}` must define {field}")

    for profile in profiles:
        profile_documents = documents_for_profile(manifest, profile)
        if not profile_documents:
            errors.append(f"profile `{profile}` has no documents")
        profile_paths = [document["path"] for document in profile_documents if "path" in document]
        if len(profile_paths) != len(set(profile_paths)):
            errors.append(f"profile `{profile}` contains duplicate document paths")

    return errors


def output_path_for(manifest: dict[str, Any], profile: str, output: str | None) -> Path:
    raw_output = output or manifest["default_outputs"][profile]
    path = Path(raw_output)
    if not path.is_absolute():
        path = ROOT / path
    return path


def render_bundle(manifest: dict[str, Any], profile: str, mode: str) -> str:
    profile_config = manifest["profiles"][profile]
    documents = documents_for_profile(manifest, profile)
    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    head = git_value(["rev-parse", "HEAD"])
    branch = git_value(["branch", "--show-current"])
    status = git_value(["status", "--short"])
    status_text = "clean" if status == "unknown" or not status else "dirty"

    lines = [
        f"# {profile_config['title']}",
        "",
        f"Generated: {generated_at}",
        f"Repository: antontvoretskiy/blueprint",
        f"Branch: {branch}",
        f"Commit: {head}",
        f"Worktree: {status_text}",
        f"Profile: {profile}",
        f"Manifest: {rel(MANIFEST_PATH)}",
        "",
        profile_config["description"],
        "",
        "## Use Instructions",
        "",
    ]
    if mode == "chat":
        lines.extend(
            [
                "Use this bundle as repository-owned context for a fresh coding-agent chat.",
                "Treat repository files as the source of truth. Do not rely on old chat history.",
                "Start by reading the table of contents, then the embedded documents in order.",
            ]
        )
    else:
        lines.extend(
            [
                "Use this bundle as a portable context payload for an external LLM, database, or review tool.",
                "The embedded documents appear in manifest order.",
                "Generated output is not canonical state; repository files remain canonical.",
            ]
        )

    lines.extend(["", "## Table Of Contents", ""])
    for index, document in enumerate(documents, start=1):
        lines.append(f"{index}. `{document['path']}` - {document['purpose']}")

    lines.extend(["", "## Documents", ""])
    for index, document in enumerate(documents, start=1):
        path = ROOT / document["path"]
        text = path.read_text()
        lines.extend(
            [
                f"### {index}. {document['title']}",
                "",
                f"Path: `{document['path']}`",
                "",
                f"Purpose: {document['purpose']}",
                "",
                "```markdown",
                text.rstrip(),
                "```",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def command_check(_: argparse.Namespace) -> int:
    manifest = load_manifest()
    errors = validate_manifest(manifest)
    if errors:
        print("fail context export")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("ok   context export")
    return 0


def command_export(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    errors = validate_manifest(manifest)
    if errors:
        print("fail context export")
        for error in errors:
            print(f"  - {error}")
        return 1
    profile = args.profile
    if profile not in manifest["profiles"]:
        print(f"fail context export\n  - unknown profile `{profile}`")
        return 1
    output_path = output_path_for(manifest, profile, args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_bundle(manifest, profile, args.mode))
    print(f"wrote {rel(output_path)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export ordered Blueprint context bundles.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser("check", help="validate the context export manifest")
    check.set_defaults(func=command_check)

    export = subparsers.add_parser("export", help="write a context bundle")
    export.add_argument("--profile", default=DEFAULT_PROFILE, help="manifest profile to export")
    export.add_argument("--output", help="output Markdown path")
    export.set_defaults(func=command_export, mode="export")

    chat = subparsers.add_parser("chat", help="write a chat bootstrap bundle")
    chat.add_argument("--profile", default="chat-bootstrap", help="manifest profile to export")
    chat.add_argument("--output", help="output Markdown path")
    chat.set_defaults(func=command_export, mode="chat")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
