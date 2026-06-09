# Blueprint Branch Governance Checklist

Status: Checklist v0.3.0.

Use this checklist before pushing a branch or opening a PR.

Canonical branch rules live in `governance/docs/git-policy.md`.

## Branch Identity

| Check | Result | Evidence |
| --- | --- | --- |
| Current repository matches the intended repository | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Current branch exists for active work | `<PASS_FAIL_OR_NA>` | `<BRANCH_NAME_OR_REASON>` |
| Branch name describes scope, not a person | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Branch family matches the changed paths | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Base branch is correct for the work type | `<PASS_FAIL_OR_NA>` | `<BASE_BRANCH_OR_REASON>` |

## Scope Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Branch maps to one review story | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Changed paths match the branch purpose | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Unrelated local files are not staged | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Source-reference repositories remain read-only | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Release-ready branch is not used for ordinary work | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Refresh Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Target branch is current enough for review | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Stale branch handling is reported when needed | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Validation was re-run after branch refresh | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Acceptance Decision

Selected result:

- `<BRANCH_READY>`
- `<BRANCH_NEEDS_REFRESH>`
- `<BRANCH_NEEDS_SCOPE_SPLIT>`
- `<BRANCH_BLOCKED_WRONG_BASE>`
- `<BRANCH_BLOCKED_UNRELATED_CHANGES>`

Reason:

`<REASON>`
