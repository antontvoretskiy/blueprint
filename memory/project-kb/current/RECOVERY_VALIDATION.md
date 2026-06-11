# Blueprint Recovery Validation

Status: Current recovery validation baseline.
Repository: `antontvoretskiy/blueprint`
Public branch model: `main` only
Last released version: `v0.7.0`
Next release target: `v0.8.0`
Validator: Blueprint Maintainers
Date: `2026-06-12`

This validation checks whether a fresh session can recover Blueprint state from
repository files after the public repository moved to a main-only distribution
model.

## Inputs

Read:

1. `core/AGENTS.md`
2. `memory/project-kb/00_INDEX.md`
3. `memory/project-kb/08_CURRENT_STATE.md`
4. `memory/project-kb/05_IMPLEMENTATION_STATUS.md`
5. `memory/project-kb/10_REFERENCE.md`
6. `core/TASK_PROCESS_ROUTER.md`
7. `memory/project-kb/current/CLEAN_START_BRIEF.md`

## Validation Matrix

| Check | Expected evidence | Result |
| --- | --- | --- |
| Repository identity is clear | Remote and repository name match the task | PASS |
| Public branch role is clear | `main` is the only public distribution branch | PASS |
| Current state is recoverable | `08_CURRENT_STATE.md` explains v0.7.0 and the v0.8.0 target | PASS |
| Included state is accurate | `05_IMPLEMENTATION_STATUS.md` matches repository contents | PASS |
| Reference map is usable | `10_REFERENCE.md` points to owner documents and validation fixtures | PASS |
| Next work is routable | `TASK_PROCESS_ROUTER.md` identifies the workflow and process level | PASS |
| Planned work is separated | Planned items are not described as included | PASS |
| Clean-start brief is scoped | Brief links back to canonical memory and owner docs | PASS |
| Old chat is not required | Recovery can complete from repository files | PASS |

## Recovery Summary

```text
Repository: antontvoretskiy/blueprint
Public branch model: main only
Current recovery point: v0.7.0 released on main; v0.8.0 validation fixtures selected as next release target
Included state: v0.7.0 public framework bundle plus v0.8.0 release-target validation fixture work on the scoped branch
Not included: CLI, installer, runtime, MCP integration, execution layers, release automation, additional examples
Next recommended work: complete v0.8.0 validation fixtures, run release validation, and publish only validated state to main
Applicable owner documents: core/AGENTS.md, memory/project-kb/00_INDEX.md, memory/project-kb/08_CURRENT_STATE.md, memory/project-kb/05_IMPLEMENTATION_STATUS.md, memory/project-kb/10_REFERENCE.md, core/TASK_PROCESS_ROUTER.md
```

## Acceptance Decision

Selected result:

- `RECOVERY_READY`

Reason:

`Repository-owned recovery files describe the released v0.7.0 state, the selected v0.8.0 validation-fixture target, and the main-only public branch model without requiring previous chat history.`
