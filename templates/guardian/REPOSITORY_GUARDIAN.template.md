# <CHANGE_NAME> Repository Guardian

Status: <DRAFT_OR_READY_OR_COMPLETED>.

This check confirms that work starts in the correct repository, branch, and scope before files are changed.

## Repository Identity

| Field | Value |
| --- | --- |
| Expected repository | `<OWNER_REPO>` |
| Actual repository | `<ACTUAL_OWNER_REPO>` |
| Working directory | `<PATH>` |
| Current branch | `<BRANCH_NAME>` |
| Intended base branch | `<BASE_BRANCH>` |
| Current HEAD | `<COMMIT_SHA>` |
| Worktree state | `<CLEAN_OR_DIRTY_WITH_NOTES>` |

## Source Reference Guard

| Question | Result | Evidence |
| --- | --- | --- |
| Does the task name a read-only source reference? | `<YES_OR_NO>` | `<SOURCE_REFERENCE_OR_NONE>` |
| Was the source reference modified? | `<YES_OR_NO>` | `<EVIDENCE>` |
| Were branches, commits, PRs, tags, or files created in the source reference? | `<YES_OR_NO>` | `<EVIDENCE>` |

## Branch Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Branch matches task type | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Normal integration work targets `develop` | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Release work targets `main` only through release PR | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Branch name maps to scope, not person | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## Start Decision

Selected result:

- `<PROCEED>`
- `<STOP_WRONG_REPOSITORY>`
- `<STOP_WRONG_BRANCH>`
- `<STOP_DIRTY_WORKTREE_CONFLICT>`
- `<STOP_SOURCE_REFERENCE_RISK>`

Reason:

`<REASON>`
