# Blueprint Recovery Checklist

Status: Checklist v0.3.0.

Use this checklist to confirm that a new session can recover the current repository state from versioned files.

## Recovery Inputs

| Check | Result | Evidence |
| --- | --- | --- |
| Recovery starts from the repository, not chat history | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Agent entrypoint is readable | `<PASS_FAIL_OR_NA>` | `<PATH_OR_REASON>` |
| Memory index is readable | `<PASS_FAIL_OR_NA>` | `<PATH_OR_REASON>` |
| Current state is readable | `<PASS_FAIL_OR_NA>` | `<PATH_OR_REASON>` |
| Implementation status is readable | `<PASS_FAIL_OR_NA>` | `<PATH_OR_REASON>` |
| Reference map is readable | `<PASS_FAIL_OR_NA>` | `<PATH_OR_REASON>` |
| Task router is readable | `<PASS_FAIL_OR_NA>` | `<PATH_OR_REASON>` |

## Recovery Questions

| Question | Result | Evidence |
| --- | --- | --- |
| What repository is this? | `<PASS_FAIL_OR_NA>` | `<ANSWER_OR_REASON>` |
| What branch should new work start from? | `<PASS_FAIL_OR_NA>` | `<ANSWER_OR_REASON>` |
| What is included now? | `<PASS_FAIL_OR_NA>` | `<ANSWER_OR_REASON>` |
| What remains planned? | `<PASS_FAIL_OR_NA>` | `<ANSWER_OR_REASON>` |
| What is explicitly excluded? | `<PASS_FAIL_OR_NA>` | `<ANSWER_OR_REASON>` |
| What owner documents apply to the next task? | `<PASS_FAIL_OR_NA>` | `<ANSWER_OR_REASON>` |

## Recovery Quality

| Check | Result | Evidence |
| --- | --- | --- |
| Current state does not contradict the manifest | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Reference map points to existing files | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Planned work is not described as included | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| The next session can continue without old chat context | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Acceptance Decision

Selected result:

- `<RECOVERY_READY>`
- `<RECOVERY_BLOCKED_MISSING_FILE>`
- `<RECOVERY_BLOCKED_STATUS_CONFLICT>`
- `<RECOVERY_BLOCKED_CHAT_DEPENDENCY>`

Reason:

`<REASON>`
