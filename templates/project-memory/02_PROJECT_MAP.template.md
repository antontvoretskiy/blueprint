# <PROJECT_NAME> Project Map

Status: <STATUS>.

This file maps project areas, ownership, and current reality.

It helps contributors and agents understand where work belongs before implementation starts.

## Project Tree

```text
<PROJECT_NAME>
|- <AREA_A>
|  `- <MODULE_A>
|- <AREA_B>
`- <FUTURE_AREA_C>
```

## Project Areas

| Area | Role | Current reality | Owner |
| --- | --- | --- | --- |
| `<AREA_A>` | `<ROLE>` | `<CURRENT_REALITY>` | `<OWNER_PATH>` |
| `<AREA_B>` | `<ROLE>` | `<CURRENT_REALITY>` | `<OWNER_PATH>` |
| `<FUTURE_AREA_C>` | `<ROLE>` | Planned | `<OWNER_PATH_OR_NOT_CREATED>` |

## Ownership Rules

- Root Project Memory describes project areas at summary level.
- Domain Memory owns domain details.
- Module Memory owns large systems inside domains.
- Subsystem Memory owns specialized internal systems.
- Feature Memory owns planning and execution artifacts for meaningful features.
- Architecture decisions own accepted architecture direction, not implementation reality.

## Routing Rules

| Work type | Route to |
| --- | --- |
| Project-wide status change | `project-kb/05_IMPLEMENTATION_STATUS.md` |
| Current work or recovery change | `project-kb/08_CURRENT_STATE.md` |
| New durable decision | `project-kb/07_DECISIONS_LOG.md` |
| Area-specific detail | `<LOWER_LEVEL_OWNER_PATH>` |
| Meaningful feature planning | `project-kb/features/<feature>/` |

## Boundary Notes

- `<BOUNDARY_NOTE_1>`
- `<BOUNDARY_NOTE_2>`
- `<BOUNDARY_NOTE_3>`
