#!/usr/bin/env python3
"""Validate Blueprint validation fixture contracts without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "docs" / "validation" / "fixtures"
RESULT_TERMS = {"PASS", "FAIL", "NOT RUN", "N/A"}
LEVELS = {"L0", "L1", "L2", "L3", "L4"}

EXPECTED_UC_IDS = [f"UC-{index:02d}" for index in range(1, 16)]
EXPECTED_RT_LEVELS = {
    "RT-01": "L0",
    "RT-02": "L0",
    "RT-03": "L0",
    "RT-04": "L1",
    "RT-05": "L1",
    "RT-06": "L1",
    "RT-07": "L1",
    "RT-08": "L1",
    "RT-09": "L2",
    "RT-10": "L2",
    "RT-11": "L2",
    "RT-12": "L4",
    "RT-13": "L3",
    "RT-14": "L3",
    "RT-15": "L4",
    "RT-16": "L4",
    "RT-17": "L4",
    "RT-18": "L4",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_fixture(name: str, errors: list[str]) -> dict[str, Any]:
    path = FIXTURES / name
    if not path.exists():
        errors.append(f"missing fixture {rel(path)}")
        return {}
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        errors.append(f"{rel(path)} is invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{rel(path)} must contain a JSON object")
        return {}
    return data


def ensure_semver_tag(data: dict[str, Any], fixture_name: str, errors: list[str]) -> None:
    version = data.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"v\d+\.\d+\.\d+", version):
        errors.append(f"{fixture_name} must declare version as vX.Y.Z")


def ensure_result_terms(data: dict[str, Any], fixture_name: str, errors: list[str]) -> None:
    terms = data.get("result_terms")
    if terms is None:
        return
    if not isinstance(terms, list) or set(terms) != RESULT_TERMS:
        errors.append(f"{fixture_name} result_terms must be {sorted(RESULT_TERMS)}")


def ensure_owner_documents(items: list[dict[str, Any]], fixture_name: str, errors: list[str]) -> None:
    for item in items:
        item_id = item.get("id", "<unknown>")
        owner_documents = item.get("owner_documents", [])
        if not isinstance(owner_documents, list) or not owner_documents:
            errors.append(f"{fixture_name} {item_id} must list owner_documents")
            continue
        for raw_path in owner_documents:
            if not isinstance(raw_path, str):
                errors.append(f"{fixture_name} {item_id} has a non-string owner document")
                continue
            if "*" in raw_path:
                continue
            path = ROOT / raw_path
            if not path.exists():
                errors.append(f"{fixture_name} {item_id} references missing `{raw_path}`")


def ensure_ids(actual: list[str], expected: list[str], label: str, errors: list[str]) -> None:
    if actual != expected:
        errors.append(f"{label} IDs must be exactly {', '.join(expected)}")
    if len(actual) != len(set(actual)):
        errors.append(f"{label} IDs must be unique")


def check_system_use_cases(data: dict[str, Any], errors: list[str]) -> None:
    ensure_semver_tag(data, "system-use-cases.json", errors)
    ensure_result_terms(data, "system-use-cases.json", errors)
    use_cases = data.get("use_cases")
    if not isinstance(use_cases, list):
        errors.append("system-use-cases.json must contain use_cases list")
        return
    ensure_ids([str(item.get("id", "")) for item in use_cases], EXPECTED_UC_IDS, "use case", errors)
    ensure_owner_documents(use_cases, "system-use-cases.json", errors)
    for item in use_cases:
        item_id = item.get("id", "<unknown>")
        for field in ("name", "method", "pass_criteria"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"system-use-cases.json {item_id} must define {field}")
    dependency_checks = data.get("dependency_checks", [])
    if not isinstance(dependency_checks, list) or not dependency_checks:
        errors.append("system-use-cases.json must contain dependency_checks")
    else:
        ensure_owner_documents(dependency_checks, "system-use-cases.json", errors)


def check_process_level_regression(data: dict[str, Any], errors: list[str]) -> None:
    ensure_semver_tag(data, "process-level-regression.json", errors)
    ensure_result_terms(data, "process-level-regression.json", errors)
    if set(data.get("levels", [])) != LEVELS:
        errors.append(f"process-level-regression.json levels must be {sorted(LEVELS)}")
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list):
        errors.append("process-level-regression.json must contain scenarios list")
        return
    expected_ids = list(EXPECTED_RT_LEVELS)
    ensure_ids([str(item.get("id", "")) for item in scenarios], expected_ids, "process regression", errors)
    for item in scenarios:
        scenario_id = str(item.get("id", ""))
        expected_level = EXPECTED_RT_LEVELS.get(scenario_id)
        if item.get("expected_level") != expected_level:
            errors.append(f"process-level-regression.json {scenario_id} expected_level must be {expected_level}")
        compact_mode = item.get("compact_mode")
        expected_compact = scenario_id in {f"RT-{index:02d}" for index in range(1, 9)}
        if compact_mode is not expected_compact:
            errors.append(f"process-level-regression.json {scenario_id} compact_mode must be {expected_compact}")
        for field in ("input_task", "pass_criteria"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"process-level-regression.json {scenario_id} must define {field}")


def check_release_readiness(data: dict[str, Any], errors: list[str]) -> None:
    ensure_semver_tag(data, "release-readiness.json", errors)
    branch_model = data.get("branch_model")
    if not isinstance(branch_model, dict):
        errors.append("release-readiness.json must contain branch_model object")
    else:
        if branch_model.get("public_heads") != ["main"]:
            errors.append("release-readiness.json branch_model.public_heads must be ['main']")
        if branch_model.get("release_target") != "main":
            errors.append("release-readiness.json branch_model.release_target must be main")
        if branch_model.get("public_integration_branch_required") is not False:
            errors.append("release-readiness.json must not require a public integration branch")
    required_commands = data.get("required_commands", [])
    if not isinstance(required_commands, list):
        errors.append("release-readiness.json required_commands must be a list")
    else:
        for command in ("make quality", "make doctor", "make config", "make smoke", "git diff --check"):
            if command not in required_commands:
                errors.append(f"release-readiness.json missing required command `{command}`")
    evidence_requirements = data.get("evidence_requirements", [])
    if not isinstance(evidence_requirements, list) or not evidence_requirements:
        errors.append("release-readiness.json must contain evidence_requirements")
    else:
        ensure_owner_documents(evidence_requirements, "release-readiness.json", errors)
    forbidden_release_scopes = data.get("forbidden_release_scopes", [])
    if not isinstance(forbidden_release_scopes, list) or "runtime" not in forbidden_release_scopes:
        errors.append("release-readiness.json must list forbidden release scopes including runtime")


def main() -> int:
    errors: list[str] = []
    system_use_cases = load_fixture("system-use-cases.json", errors)
    process_level_regression = load_fixture("process-level-regression.json", errors)
    release_readiness = load_fixture("release-readiness.json", errors)

    if system_use_cases:
        check_system_use_cases(system_use_cases, errors)
    if process_level_regression:
        check_process_level_regression(process_level_regression, errors)
    if release_readiness:
        check_release_readiness(release_readiness, errors)

    if errors:
        print("fail validation fixtures")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("ok   validation fixtures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
