# Blueprint Project Memory Index

This index is the entrypoint for repository-owned project memory.

Project Memory stores durable state needed for recovery between work sessions. It is not a chat transcript and not a replacement for governance documents.

## Recovery Order

For a fresh session, read:

1. `README.md`
2. `OPEN_SOURCE_SPEC.md`
3. `PRODUCT_MAP.md`
4. `ARCHITECTURE.md`
5. `BUNDLE_MANIFEST.md`
6. `core/AGENTS.md`
7. `core/TASK_PROCESS_ROUTER.md`
8. `memory/project-kb/08_CURRENT_STATE.md`
9. `memory/project-kb/05_IMPLEMENTATION_STATUS.md`
10. `memory/project-kb/10_REFERENCE.md`

Load governance documents when the task changes rules, branches, PR standards, validation, documentation, or ADR policy.

Load `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` and `memory/project-kb/12_SYSTEM_RELATIONSHIP_MAP.md` when the task changes source-reference coverage, ownership, system relationships, process levels, project/feature management, or transfer completeness.

## Memory Files

| File | Purpose |
| --- | --- |
| `05_IMPLEMENTATION_STATUS.md` | What exists, what is planned, and what is excluded |
| `06_WORKFLOW_AND_RULES.md` | Active workflow rules and branch policy summary |
| `07_DECISIONS_LOG.md` | Accepted decisions and their consequences |
| `08_CURRENT_STATE.md` | Current repository state and next recommended work |
| `09_TASK_HISTORY.md` | Durable task history after merged work |
| `10_REFERENCE.md` | Canonical references and owner documents |
| `11_SOURCE_COVERAGE_MATRIX.md` | Source-reference coverage status and remaining gaps |
| `12_SYSTEM_RELATIONSHIP_MAP.md` | Owners, dependencies, and document interaction map |
| `current/CLEAN_START_BRIEF.md` | Short current handoff for the next session |
| `current/RECOVERY_VALIDATION.md` | Current recovery validation result |
| `current/SYSTEM_USE_CASE_VALIDATION.md` | Current system use-case validation result |
| `architecture-decisions/GUARDIAN_ARCHITECTURE.md` | Guardian process architecture |
| `GUARDIAN_VALIDATION_SCENARIOS.md` | Generic Guardian validation scenarios |

## Memory Rules

- Keep memory compact.
- Update memory only when durable project state changes.
- Do not copy chat transcripts into memory.
- Do not store private product history in Blueprint memory.
- Link to owner documents instead of duplicating full standards.
- Distinguish included, planned, excluded, and released states.

## Source Of Truth

Governance rules are owned by governance and core documents.

Project Memory records current state and recovery information. It must not redefine canonical rules.
