# Context Export Plan

Feature: context-export
Version: v0.9.0
Status: Release target

## Summary

Add a repository-local context export workflow that can generate ordered
Markdown bundles for external LLMs and fresh Codex or Cursor chats.

## Technical Context

Affected layers:

- local validation scripts;
- Makefile commands;
- documentation navigation;
- Project Memory;
- release metadata.

Excluded layers:

- packaged CLI;
- installer;
- runtime;
- external editor integration;
- release automation;
- dependency automation.

## Governance Check

Relevant owner documents:

- `core/FEATURE_LIFECYCLE_STANDARD.md`
- `core/TASK_PROCESS_ROUTER.md`
- `governance/docs/git-policy.md`
- `governance/docs/verification-standard.md`
- `BUNDLE_MANIFEST.md`
- `memory/project-kb/10_REFERENCE.md`

This is a meaningful public workflow, so feature artifacts are required before
implementation.

## Document Model

| Document | Purpose |
| --- | --- |
| `context/README.md` | Human-facing command guide |
| `context/export-manifest.json` | Ordered profiles and source files |
| `scripts/export_context.py` | Manifest validation and bundle generation |
| `.blueprint/context/` | Ignored default output location |

## Validation Strategy

Required commands:

```bash
make quality
make context-export
make context-chat
python3 scripts/export_context.py check
python3 -m py_compile scripts/export_context.py
git diff --check
```

Release-readiness validation still requires:

```bash
make doctor
make config
make smoke
```

## Guardian Validation

| Check | Result | Evidence |
| --- | --- | --- |
| Repository source of truth preserved | PASS | Manifest references repository files; generated bundles are ignored |
| External tool boundary preserved | PASS | No Codex, Cursor, or external service API is called |
| Runtime boundary preserved | PASS | No product runtime or workflow engine is added |
| Validation evidence defined | PASS | `make quality` and direct export commands validate the feature |
