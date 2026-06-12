# Context Export Tasks

Feature: context-export
Version: v0.11.0
Status: Release target

## Phase 1 - Feature Artifacts

- [x] Add `FEATURE.md`.
- [x] Add `CLARIFICATION.md`.
- [x] Add `PLAN.md`.
- [x] Add `TASKS.md`.

## Phase 2 - Context Model

- [x] Add `context/README.md`.
- [x] Add `context/export-manifest.json`.
- [x] Add ignored output path for generated context bundles.

## Phase 3 - Commands

- [x] Add `scripts/export_context.py`.
- [x] Add `make context-export`.
- [x] Add `make context-chat`.
- [x] Add manifest validation to `make quality`.

## Phase 4 - Documentation And Memory

- [x] Update README, docs navigation, product map, manifest, reference map, and
  script guide.
- [x] Update Project Memory current state and implementation status.
- [x] Update release metadata for the context export release target.

## Phase 5 - Validation

- [x] Run `make quality`.
- [x] Run `make context-export`.
- [x] Run `make context-chat`.
- [x] Run `python3 -m py_compile scripts/export_context.py`.
- [x] Run release-readiness commands before merge or release.

## Phase 6 - Profile-Specific Exports

- [x] Add explicit `codex`, `cursor`, and `database-ingest` profiles.
- [x] Add `make context-codex`.
- [x] Add `make context-cursor`.
- [x] Add `make context-database`.
- [x] Document why the context pack includes each class of source-of-truth
  document.
- [x] Run profile-specific export validation before release.

## Phase 7 - JSONL Export

- [x] Add JSONL default outputs to the context manifest.
- [x] Add `python3 scripts/export_context.py jsonl`.
- [x] Add `make context-jsonl`.
- [x] Document the JSONL row shape and intended database/RAG use.
- [x] Run JSONL export validation before release.
