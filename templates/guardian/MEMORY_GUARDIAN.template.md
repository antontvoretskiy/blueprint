# <CHANGE_NAME> Memory Guardian

Status: <DRAFT_OR_READY_OR_COMPLETED>.

This check decides whether the change requires Project Memory, owner document, or clean-start updates.

Project Memory should change only when durable repository state changed.

## Memory Inputs

| Input | Path or value |
| --- | --- |
| Implementation status owner | `<IMPLEMENTATION_STATUS_PATH>` |
| Current state owner | `<CURRENT_STATE_PATH>` |
| Reference map owner | `<REFERENCE_MAP_PATH>` |
| Task history owner | `<TASK_HISTORY_PATH>` |
| Clean-start brief owner | `<CLEAN_START_BRIEF_PATH>` |
| Changed owner document | `<OWNER_DOCUMENT_OR_NONE>` |

## Update Need

| Criterion | Applies? | Evidence or reason |
| --- | --- | --- |
| Repository state changed | `<YES_OR_NO>` | `<EVIDENCE_OR_REASON>` |
| Included or planned status changed | `<YES_OR_NO>` | `<EVIDENCE_OR_REASON>` |
| Recovery path changed | `<YES_OR_NO>` | `<EVIDENCE_OR_REASON>` |
| Reference navigation changed | `<YES_OR_NO>` | `<EVIDENCE_OR_REASON>` |
| Accepted decision changed | `<YES_OR_NO>` | `<EVIDENCE_OR_REASON>` |
| Meaningful PR merged | `<YES_OR_NO>` | `<EVIDENCE_OR_REASON>` |
| Old chat dependency would remain without update | `<YES_OR_NO>` | `<EVIDENCE_OR_REASON>` |

## Required Updates

| File | Required? | Reason |
| --- | --- | --- |
| `<IMPLEMENTATION_STATUS_PATH>` | `<YES_OR_NO>` | `<REASON>` |
| `<CURRENT_STATE_PATH>` | `<YES_OR_NO>` | `<REASON>` |
| `<REFERENCE_MAP_PATH>` | `<YES_OR_NO>` | `<REASON>` |
| `<TASK_HISTORY_PATH>` | `<YES_OR_NO>` | `<REASON>` |
| `<CLEAN_START_BRIEF_PATH>` | `<YES_OR_NO>` | `<REASON>` |
| `<OWNER_DOCUMENT_OR_NONE>` | `<YES_OR_NO>` | `<REASON>` |

## Memory Decision

Selected result:

- `<NO_MEMORY_UPDATE_NEEDED>`
- `<UPDATE_PROJECT_MEMORY>`
- `<UPDATE_OWNER_DOCUMENT_ONLY>`
- `<UPDATE_CLEAN_START_ONLY>`
- `<STOP_MEMORY_CONFLICT>`

Reason:

`<REASON>`
