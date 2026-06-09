# <RELEASE_NAME> Release Guardian

Status: <DRAFT_OR_READY_OR_COMPLETED>.

This check confirms readiness before integration state moves to release-ready state.

Use this only when release state changes.

## Release Identity

| Field | Value |
| --- | --- |
| Release version | `<VERSION>` |
| Source branch | `<SOURCE_BRANCH>` |
| Target branch | `<TARGET_BRANCH>` |
| Release PR | `<PR_LINK>` |
| Release commit | `<COMMIT_SHA>` |
| Tag planned | `<YES_OR_NO>` |

## Release Boundary Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Release starts from validated integration branch | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Release PR targets release-ready branch | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| No unrelated feature work is bundled | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Manifest and README match release scope | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Planned items remain marked as planned | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## Release Validation Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Local validation passed | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Link checks passed | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Forbidden wording scans passed | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Commit and PR title checks passed | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Release notes or release summary exist | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## Clean Start Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Current state reflects release readiness | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Task history records meaningful merged work | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Next session can recover without old chat history | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## Release Decision

Selected result:

- `<READY_FOR_RELEASE_PR>`
- `<NEEDS_VALIDATION>`
- `<NEEDS_DOCUMENTATION_SYNC>`
- `<NEEDS_SCOPE_SPLIT>`
- `<BLOCKED>`

Reason:

`<REASON>`
