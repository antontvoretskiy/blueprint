# <PROJECT_NAME> Project Memory Index

Status: <STATUS>.

This index is the entrypoint for repository-owned Project Memory.

Project Memory stores durable recovery state. It is not a chat transcript and not a replacement for governance, architecture, code, tests, or other owner documents.

## Recovery Order

For a fresh session, read:

1. `<ROOT_README_PATH>`
2. `<PRODUCT_OR_PROJECT_SPEC_PATH>`
3. `<ARCHITECTURE_PATH>`
4. `<BUNDLE_OR_MANIFEST_PATH>`
5. `<AGENT_ENTRYPOINT_PATH>`
6. `<TASK_ROUTER_PATH>`
7. `project-kb/08_CURRENT_STATE.md`
8. `project-kb/05_IMPLEMENTATION_STATUS.md`
9. `project-kb/10_REFERENCE.md`

Load governance documents when the task changes rules, branches, PR standards, validation, documentation, or architecture decisions.

Load feature artifacts when the task is a meaningful feature.

## Memory Files

| File | Purpose |
| --- | --- |
| `01_PROJECT_CONTEXT.md` | Project identity, purpose, audience, and current direction |
| `02_PROJECT_MAP.md` | Product or repository area map with ownership |
| `03_SYSTEM_ARCHITECTURE.md` | Architecture summary and source-of-truth owners |
| `04_DOMAIN_MODEL.md` | Shared vocabulary and boundary rules |
| `05_IMPLEMENTATION_STATUS.md` | Included, planned, excluded, released, and deprecated state |
| `06_WORKFLOW_AND_RULES.md` | Recovery-oriented workflow summary |
| `07_DECISIONS_LOG.md` | Accepted decisions and consequences |
| `08_CURRENT_STATE.md` | Current recovery point and next work |
| `09_TASK_HISTORY.md` | Durable task history after meaningful work |
| `10_REFERENCE.md` | Canonical reference map |
| `current/CLEAN_START_BRIEF.md` | Short current handoff when needed |

## Lower-Level Memory

Use lower-level memory only when root memory would become too detailed:

| Level | Path pattern | Purpose |
| --- | --- | --- |
| Domain Memory | `project-kb/domains/<domain>/` | Durable state for a major project domain |
| Module Memory | `project-kb/domains/<domain>/modules/<module>/` | Durable state for a module inside a domain |
| Subsystem Memory | `project-kb/domains/<domain>/modules/<module>/subsystems/<subsystem>/` | Durable state for specialized internals |
| Feature Memory | `project-kb/features/<feature>/` | Feature planning and execution artifacts |

## Memory Rules

- Keep root memory compact.
- Update memory only when durable project state changes.
- Link to canonical owner documents.
- Do not duplicate full standards.
- Do not copy chat transcripts into memory.
- Do not store private product history.
- Distinguish proposed, planned, included, implemented, released, deprecated, and excluded state.

## Source Of Truth

Governance rules are owned by governance and core documents.

Implementation reality is owned by code, tests, contracts, build artifacts, validation evidence, and implementation status.

Project Memory records recovery state and must not redefine canonical rules.
