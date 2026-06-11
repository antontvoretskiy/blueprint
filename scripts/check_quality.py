#!/usr/bin/env python3
"""Run Blueprint repository quality checks without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]

PUBLIC_WORDING_PATHS = [
    "README.md",
    "ARCHITECTURE.md",
    "BUNDLE_MANIFEST.md",
    "OPEN_SOURCE_SPEC.md",
    "CONTRIBUTING.md",
    "ADAPTATION_GUIDE.md",
    "MIGRATION_GUIDE.md",
    "OPEN_SOURCE_GUIDE.md",
    "VALIDATION_CHECKLIST.md",
    "RELEASE.md",
    "CHANGELOG.md",
    "docs/index.md",
    "docs/nav.md",
    "docs/quickstart.md",
    "docs/concepts/repository-first.md",
    "docs/reference/templates.md",
    "docs/reference/governance.md",
    "docs/community.md",
    "docs/validation/fixtures/README.md",
    "scripts/README.md",
]

FORBIDDEN_PUBLIC_WORDING = [
    r"\bOS\b",
    r"Operating System",
    r"Project OS",
    r"Open Source OS",
    r"Reelza",
    r"Montage",
    r"Virality",
    r"Stage 04",
    r"Stage 05",
    r"Stage 06",
    r"Runtime Admin",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def fail(check: str, errors: list[str]) -> int:
    print(f"fail {check}")
    for error in errors:
        print(f"  - {error}")
    return 1


def ok(check: str) -> int:
    print(f"ok   {check}")
    return 0


def included_manifest_paths() -> list[str]:
    manifest = ROOT / "BUNDLE_MANIFEST.md"
    text = manifest.read_text()
    included = text.split("## Included Now", 1)[1].split("## Planned Later", 1)[0]
    paths: list[str] = []
    for line in included.splitlines():
        if not line.startswith("| `"):
            continue
        match = re.match(r"\| `([^`]+)` \|", line)
        if match:
            paths.append(match.group(1))
    return paths


def check_manifest_paths() -> int:
    errors: list[str] = []
    for raw_path in included_manifest_paths():
        if "*" in raw_path:
            continue
        path = ROOT / raw_path.rstrip("/")
        if not path.exists():
            errors.append(f"`{raw_path}` is listed in BUNDLE_MANIFEST.md but does not exist")
    return fail("manifest paths", errors) if errors else ok("manifest paths")


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and ".venv" not in path.parts
    )


def markdown_targets(text: str) -> list[str]:
    targets = [match.group(1).strip() for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", text)]
    targets.extend(match.group(1).strip() for match in re.finditer(r"<img\b[^>]*\bsrc=\"([^\"]+)\"", text))
    return targets


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto"}


def check_links() -> int:
    errors: list[str] = []
    for file_path in iter_markdown_files():
        text = file_path.read_text()
        for raw_target in markdown_targets(text):
            if not raw_target or raw_target.startswith("#") or is_external(raw_target):
                continue
            target = raw_target.strip("<>")
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            target_path = (ROOT / target.lstrip("/")) if target.startswith("/") else (file_path.parent / target)
            if not target_path.exists():
                errors.append(f"{rel(file_path)} links to missing `{raw_target}`")
    return fail("markdown links", errors) if errors else ok("markdown links")


def check_public_wording() -> int:
    errors: list[str] = []
    patterns = [(wording, re.compile(wording, re.IGNORECASE)) for wording in FORBIDDEN_PUBLIC_WORDING]
    for relative_path in PUBLIC_WORDING_PATHS:
        file_path = ROOT / relative_path
        if not file_path.exists():
            continue
        text = file_path.read_text()
        for wording, pattern in patterns:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{relative_path}:{line} matches forbidden public wording `{wording}`")
    return fail("public wording", errors) if errors else ok("public wording")


def check_template_index() -> int:
    errors: list[str] = []
    manifest = (ROOT / "BUNDLE_MANIFEST.md").read_text()
    for template in sorted((ROOT / "templates").rglob("*.template.md")):
        bundle_readme = template.parent / "README.md"
        if not bundle_readme.exists():
            errors.append(f"{rel(template)} has no bundle README.md")
            continue
        readme_text = bundle_readme.read_text()
        name = template.name
        if name not in readme_text:
            errors.append(f"{rel(template)} is missing from {rel(bundle_readme)}")
        if rel(template) not in manifest:
            errors.append(f"{rel(template)} is missing from BUNDLE_MANIFEST.md")
    return fail("template index", errors) if errors else ok("template index")


def check_release_consistency() -> int:
    errors: list[str] = []
    version = (ROOT / "VERSION").read_text().strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must use SemVer without a leading v")
        version_tag = f"v{version}"
    else:
        version_tag = f"v{version}"

    required = {
        "README.md": version_tag,
        "CHANGELOG.md": f"## {version_tag}",
    }
    for relative_path, expected in required.items():
        text = (ROOT / relative_path).read_text()
        if expected not in text:
            errors.append(f"{relative_path} does not contain `{expected}`")
    release_text = (ROOT / "RELEASE.md").read_text()
    release_markers = [
        f"Last released version: {version_tag}.",
        f"Next release target: {version_tag}.",
    ]
    if not any(marker in release_text for marker in release_markers):
        expected = "`Last released version` or `Next release target`"
        errors.append(f"RELEASE.md does not declare {version_tag} as {expected}")
    return fail("release consistency", errors) if errors else ok("release consistency")


def main() -> int:
    checks = [
        check_manifest_paths,
        check_links,
        check_public_wording,
        check_template_index,
        check_release_consistency,
    ]
    return 1 if any(check() for check in checks) else 0


if __name__ == "__main__":
    sys.exit(main())
