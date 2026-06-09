# <CHANGE_NAME> Clean Start Transition

Status: <DRAFT_OR_READY_OR_COMPLETED>.

This file records the post-merge transition for the next session.

It helps the next session recover quickly, but canonical state must remain in Project Memory, owner documents, merged PR metadata, and validation evidence.

## Merge Result

| Field | Value |
| --- | --- |
| PR | `<PR_LINK>` |
| Merge commit | `<MERGE_COMMIT_SHA>` |
| Target branch | `<TARGET_BRANCH>` |
| Branch deleted | `<YES_OR_NO>` |
| Release state changed | `<YES_OR_NO>` |

## Current Recovery Point

`<CURRENT_RECOVERY_SUMMARY>`

## Read First

1. `<RECOVERY_ENTRYPOINT>`
2. `<CURRENT_STATE_PATH>`
3. `<IMPLEMENTATION_STATUS_PATH>`
4. `<REFERENCE_MAP_PATH>`
5. `<TASK_ROUTER_PATH>`

## What Changed

- `<CHANGE_1>`
- `<CHANGE_2>`
- `<CHANGE_3>`

## What Did Not Change

- `<NON_CHANGE_1>`
- `<NON_CHANGE_2>`
- `<NON_CHANGE_3>`

## Validation Repeated After Merge

| Check | Result | Evidence |
| --- | --- | --- |
| `<VALIDATION_COMMAND_OR_CHECK>` | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE_OR_REASON>` |
| `<VALIDATION_COMMAND_OR_CHECK>` | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE_OR_REASON>` |

## Next Recommended Work

1. `<NEXT_STEP_1>`
2. `<NEXT_STEP_2>`
3. `<NEXT_STEP_3>`

## Remaining Risks

| Risk | Owner | Mitigation |
| --- | --- | --- |
| `<RISK_OR_NONE>` | `<OWNER>` | `<MITIGATION>` |

## Clean Start Rules

- Do not require old chat history for the next session.
- Do not create multiple active clean-start briefs.
- Do not store unique decisions only in this transition.
- Point back to canonical repository documents for durable state.
