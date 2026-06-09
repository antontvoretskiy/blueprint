# <FEATURE_NAME> Tasks

Status: <PLANNING_OR_APPROVED_OR_COMPLETED_OR_ARCHIVED>.

This file breaks the feature into small, reviewable, reversible work.

Each task should map to one clear layer and one clear validation outcome.

## Task Rules

- Tasks must not mix unrelated layers.
- Tasks should be independently reviewable.
- Tasks should be reversible when possible.
- Implementation tasks should not start before `PLAN.md` is approved.
- Migration tasks require a migration matrix.
- Validation tasks must produce evidence.

## Phase 1 - Setup

| ID | Task | Paths | Depends on | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| T001 | `<SETUP_TASK>` | `<PATHS>` | None | `<VALIDATION>` | `<STATUS>` |
| T002 | `<SETUP_TASK>` | `<PATHS>` | T001 | `<VALIDATION>` | `<STATUS>` |

## Phase 2 - Foundation

| ID | Task | Paths | Depends on | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| T003 | `<FOUNDATION_TASK>` | `<PATHS>` | T001 | `<VALIDATION>` | `<STATUS>` |
| T004 | `<FOUNDATION_TASK>` | `<PATHS>` | T003 | `<VALIDATION>` | `<STATUS>` |

## Phase 3 - Priority 1

| ID | Task | Paths | Depends on | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| T005 | `<P1_TASK>` | `<PATHS>` | T003 | `<VALIDATION>` | `<STATUS>` |
| T006 | `<P1_TASK>` | `<PATHS>` | T005 | `<VALIDATION>` | `<STATUS>` |

## Phase 4 - Priority 2

| ID | Task | Paths | Depends on | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| T007 | `<P2_TASK>` | `<PATHS>` | T005 | `<VALIDATION>` | `<STATUS>` |
| T008 | `<P2_TASK>` | `<PATHS>` | T007 | `<VALIDATION>` | `<STATUS>` |

## Phase 5 - Priority 3

| ID | Task | Paths | Depends on | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| T009 | `<P3_TASK>` | `<PATHS>` | T005 | `<VALIDATION>` | `<STATUS>` |

## Phase 6 - Polish

| ID | Task | Paths | Depends on | Validation | Status |
| --- | --- | --- | --- | --- | --- |
| T010 | `<POLISH_TASK>` | `<PATHS>` | T005-T009 | `<VALIDATION>` | `<STATUS>` |
| T011 | `<DOCS_OR_MEMORY_TASK>` | `<PATHS>` | T010 | `<VALIDATION>` | `<STATUS>` |

## PR Split Plan

| PR | Scope | Tasks | Base branch | Notes |
| --- | --- | --- | --- | --- |
| `<PR_1>` | `<SCOPE>` | `<TASK_IDS>` | `<BASE_BRANCH>` | `<NOTES>` |
| `<PR_2>` | `<SCOPE>` | `<TASK_IDS>` | `<BASE_BRANCH>` | `<NOTES>` |

## Validation Checklist

- [ ] `<VALIDATION_COMMAND_OR_CHECK>`
- [ ] `<VALIDATION_COMMAND_OR_CHECK>`
- [ ] `<VALIDATION_COMMAND_OR_CHECK>`

## Completion Checklist

- [ ] included and excluded scope is explicit;
- [ ] all P1 tasks are complete;
- [ ] validation evidence is recorded;
- [ ] PR body can serve as handoff;
- [ ] required Project Memory or owner docs are updated;
- [ ] clean start can recover from repository files;
- [ ] feature artifacts are marked `Completed` or `Archived` when work is done.
