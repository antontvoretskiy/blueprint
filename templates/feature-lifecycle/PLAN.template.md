# <FEATURE_NAME> Plan

Status: <PLANNING_OR_APPROVED_OR_COMPLETED_OR_ARCHIVED>.

This file defines how the feature will be built.

Implementation must not start until critical questions are resolved and Guardian validation passes.

## Summary

`<IMPLEMENTATION_PLAN_SUMMARY>`

## Technical Context

| Area | Value |
| --- | --- |
| Repository | `<OWNER_REPO>` |
| Base branch | `<BASE_BRANCH>` |
| Work branch | `<WORK_BRANCH>` |
| Process level | `<L2_OR_L3_OR_L4>` |
| Feature artifacts path | `project-kb/features/<feature-name>/` |
| Primary owner | `<OWNER>` |

## Affected Layers

| Layer | Paths | Owner | In scope? |
| --- | --- | --- | --- |
| `<LAYER_A>` | `<PATHS>` | `<OWNER_DOC>` | `<YES_OR_NO>` |
| `<LAYER_B>` | `<PATHS>` | `<OWNER_DOC>` | `<YES_OR_NO>` |

## Governance Check

| Check | Owner | Result |
| --- | --- | --- |
| Task routing | `<TASK_ROUTER_PATH>` | `<PASS_OR_FAIL_OR_NOT_RUN>` |
| Feature lifecycle | `<FEATURE_LIFECYCLE_STANDARD_PATH>` | `<PASS_OR_FAIL_OR_NOT_RUN>` |
| Branch policy | `<GIT_POLICY_PATH>` | `<PASS_OR_FAIL_OR_NOT_RUN>` |
| PR standard | `<PR_STANDARD_PATH>` | `<PASS_OR_FAIL_OR_NOT_RUN>` |
| Verification standard | `<VERIFICATION_STANDARD_PATH>` | `<PASS_OR_FAIL_OR_NOT_RUN>` |
| Documentation standard | `<DOCUMENTATION_STANDARD_PATH>` | `<PASS_OR_FAIL_OR_NOT_RUN>` |
| Security baseline | `<SECURITY_OWNER_PATH>` | `<PASS_OR_FAIL_OR_NOT_RUN>` |

## Research

| Question | Finding | Decision |
| --- | --- | --- |
| `<RESEARCH_QUESTION>` | `<FINDING>` | `<DECISION>` |

## Data Or Document Model

| Item | Type | Owner | Notes |
| --- | --- | --- | --- |
| `<ITEM_A>` | `<DATA_OR_DOCUMENT_OR_TEMPLATE>` | `<OWNER_PATH>` | `<NOTES>` |
| `<ITEM_B>` | `<DATA_OR_DOCUMENT_OR_TEMPLATE>` | `<OWNER_PATH>` | `<NOTES>` |

## Implementation Strategy

1. `<STEP_1>`
2. `<STEP_2>`
3. `<STEP_3>`

## Validation Strategy

| Claim | Evidence | Command or check |
| --- | --- | --- |
| `<CLAIM_1>` | `<EVIDENCE>` | `<VALIDATION_COMMAND>` |
| `<CLAIM_2>` | `<EVIDENCE>` | `<VALIDATION_COMMAND>` |

## Memory Update Plan

| Memory file | Update needed? | Reason |
| --- | --- | --- |
| `project-kb/05_IMPLEMENTATION_STATUS.md` | `<YES_OR_NO>` | `<REASON>` |
| `project-kb/07_DECISIONS_LOG.md` | `<YES_OR_NO>` | `<REASON>` |
| `project-kb/08_CURRENT_STATE.md` | `<YES_OR_NO>` | `<REASON>` |
| `project-kb/09_TASK_HISTORY.md` | `<YES_OR_NO>` | `<REASON>` |
| `project-kb/10_REFERENCE.md` | `<YES_OR_NO>` | `<REASON>` |

## Guardian Readiness

Guardian validation may run when:

- required feature artifacts exist;
- affected layers are identified;
- included and excluded paths are explicit;
- validation strategy is defined;
- memory update plan is clear.

Readiness status: `<READY_OR_BLOCKED>`.

## Explicit Exclusions

- `<EXCLUDED_SCOPE_1>`
- `<EXCLUDED_SCOPE_2>`
- `<EXCLUDED_SCOPE_3>`
