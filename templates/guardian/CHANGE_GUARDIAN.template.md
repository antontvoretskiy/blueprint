# <CHANGE_NAME> Change Guardian

Status: <DRAFT_OR_READY_OR_COMPLETED>.

This check confirms that the change stays inside the approved scope.

## Scope Summary

| Field | Value |
| --- | --- |
| Process level | `<L0_L1_L2_L3_OR_L4>` |
| Task class | `<TASK_CLASS>` |
| Allowed paths | `<ALLOWED_PATHS>` |
| Explicitly excluded paths | `<EXCLUDED_PATHS>` |
| Public claims changed | `<YES_OR_NO>` |
| Release state changed | `<YES_OR_NO>` |

## Path Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Changed files match allowed paths | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Forbidden paths are unchanged | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| One PR maps to one scope | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| No unrelated user changes were staged | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## Public Claim Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Included claims match files that exist | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Planned work remains marked as planned | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Excluded areas remain excluded | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Validation claims match command results | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## Change Decision

Selected result:

- `<PROCEED>`
- `<SPLIT_PR>`
- `<REMOVE_OUT_OF_SCOPE_CHANGES>`
- `<FIX_PUBLIC_CLAIMS>`
- `<STOP_UNTIL_SCOPE_IS_APPROVED>`

Reason:

`<REASON>`
