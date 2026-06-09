# <CHANGE_NAME> PR Guardian

Status: <DRAFT_OR_READY_OR_COMPLETED>.

This check confirms that a PR is ready for review and recoverable after merge.

## PR Identity

| Field | Value |
| --- | --- |
| PR link | `<PR_LINK>` |
| PR title | `<PR_TITLE>` |
| Base branch | `<BASE_BRANCH>` |
| Head branch | `<HEAD_BRANCH>` |
| Commit title | `<COMMIT_TITLE>` |
| Versioned asset | `<ASSET_AND_VERSION_OR_NONE>` |

## Title And Commit Guard

| Check | Result | Evidence |
| --- | --- | --- |
| PR title follows contribution standard | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Commit title follows contribution standard | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Version appears when public asset changes | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| No noisy low-signal wording is present | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## PR Body Guard

| Required section | Present? | Notes |
| --- | --- | --- |
| Problem | `<YES_OR_NO>` | `<NOTES>` |
| Solution | `<YES_OR_NO>` | `<NOTES>` |
| Scope | `<YES_OR_NO>` | `<NOTES>` |
| Validation | `<YES_OR_NO>` | `<NOTES>` |
| Risks | `<YES_OR_NO>` | `<NOTES>` |
| Follow-ups | `<YES_OR_NO>` | `<NOTES>` |
| Asset metadata block when required | `<YES_OR_NO>` | `<NOTES>` |

## Validation Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Required commands were run or reported as not run | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Link checks were run for docs changes | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Forbidden wording scans were run for public docs | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Scope exclusions are explicit | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Remaining risks are named | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## PR Decision

Selected result:

- `<READY_FOR_REVIEW>`
- `<NEEDS_BODY_UPDATE>`
- `<NEEDS_VALIDATION>`
- `<NEEDS_SCOPE_SPLIT>`
- `<BLOCKED>`

Reason:

`<REASON>`
