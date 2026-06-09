# <CHANGE_NAME> Architecture Guardian

Status: <DRAFT_OR_READY_OR_COMPLETED>.

This check confirms that the change preserves Blueprint layer boundaries and non-goals.

## Architecture Inputs

| Input | Path or value |
| --- | --- |
| Architecture owner | `<ARCHITECTURE_OWNER_PATH>` |
| Product map owner | `<PRODUCT_MAP_PATH>` |
| Bundle manifest owner | `<BUNDLE_MANIFEST_PATH>` |
| Governance index owner | `<GOVERNANCE_INDEX_PATH>` |
| Affected layer | `<CORE_EXTENSION_EXAMPLE_OR_ADOPTER_LAYER>` |

## Layer Boundary Guard

| Check | Result | Evidence |
| --- | --- | --- |
| Core rules stay in canonical owner documents | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Templates do not redefine core rules | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Examples do not become source of truth | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Extensions remain optional | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## Non-Goal Guard

| Non-goal | Present in change? | Evidence |
| --- | --- | --- |
| Runtime framework | `<YES_OR_NO>` | `<EVIDENCE>` |
| Agent runtime | `<YES_OR_NO>` | `<EVIDENCE>` |
| Workflow engine | `<YES_OR_NO>` | `<EVIDENCE>` |
| Code generator | `<YES_OR_NO>` | `<EVIDENCE>` |
| MCP server | `<YES_OR_NO>` | `<EVIDENCE>` |
| SaaS starter kit | `<YES_OR_NO>` | `<EVIDENCE>` |
| Product framework | `<YES_OR_NO>` | `<EVIDENCE>` |
| UI framework | `<YES_OR_NO>` | `<EVIDENCE>` |
| Product-specific memory | `<YES_OR_NO>` | `<EVIDENCE>` |

## Architecture Decision

Selected result:

- `<PROCEED>`
- `<UPDATE_OWNER_DOCUMENT>`
- `<ADD_OR_UPDATE_ADR>`
- `<MOVE_CONTENT_TO_EXTENSION_LAYER>`
- `<REMOVE_NON_GOAL_CONTENT>`
- `<STOP_FOR_ARCHITECTURE_REVIEW>`

Reason:

`<REASON>`
