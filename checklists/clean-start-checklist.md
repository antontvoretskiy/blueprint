# Blueprint Clean Start Checklist

Status: Checklist v0.3.0.

Use this checklist after a meaningful PR merges.

Canonical clean-start rules live in `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md`.

## Merge Confirmation

| Check | Result | Evidence |
| --- | --- | --- |
| PR is merged into the intended target branch | `<PASS_FAIL_OR_NA>` | `<PR_AND_BRANCH>` |
| Merge commit is recorded when relevant | `<PASS_FAIL_OR_NA>` | `<COMMIT_SHA_OR_REASON>` |
| Target branch is synced locally when continuing work | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Post-merge validation was run or reported as not applicable | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Repository State

| Check | Result | Evidence |
| --- | --- | --- |
| Implementation status reflects the merged change | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Current state reflects the merged change when recovery changed | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Reference map reflects new owner or template paths | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Task history records meaningful merged work | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Planned and included states remain distinct | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Handoff Quality

| Check | Result | Evidence |
| --- | --- | --- |
| Next session can recover from repository files and merged PR metadata | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Old chat history is not required to continue | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Follow-up work starts from the updated integration branch | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Merged branch cleanup decision is explicit | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Acceptance Decision

Selected result:

- `<CLEAN_START_READY>`
- `<NEEDS_MEMORY_UPDATE>`
- `<NEEDS_REFERENCE_UPDATE>`
- `<NEEDS_POST_MERGE_VALIDATION>`
- `<BLOCKED_CHAT_DEPENDENCY>`

Reason:

`<REASON>`
