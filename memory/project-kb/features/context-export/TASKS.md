# Context Export Tasks

Feature: context-export
Version: v0.9.0
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
- [x] Update release metadata for v0.9.0 target.

## Phase 5 - Validation

- [x] Run `make quality`.
- [x] Run `make context-export`.
- [x] Run `make context-chat`.
- [x] Run `python3 -m py_compile scripts/export_context.py`.
- [x] Run release-readiness commands before merge or release.
