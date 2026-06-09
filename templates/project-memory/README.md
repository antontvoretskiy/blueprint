# Project Memory Templates

Status: Template Bundle v0.2.0.

This bundle provides reusable Project Memory templates for repositories adopting Blueprint.

Project Memory is repository-owned recovery state. It is not a chat transcript, not a duplicate documentation site, and not a replacement for owner documents.

## Install Target

When installed into another repository, render these templates into:

```text
project-kb/
```

Blueprint keeps its own active memory under:

```text
memory/project-kb/
```

The active Blueprint memory and these templates have different roles:

| Area | Role |
| --- | --- |
| `memory/project-kb/**` | Current Blueprint repository state |
| `templates/project-memory/**` | Reusable Project Memory files for adopter repositories |

## Template Files

| Template | Rendered file | Purpose |
| --- | --- | --- |
| `00_INDEX.template.md` | `project-kb/00_INDEX.md` | Recovery entrypoint and memory navigation |
| `01_PROJECT_CONTEXT.template.md` | `project-kb/01_PROJECT_CONTEXT.md` | Project identity, purpose, audience, and current direction |
| `02_PROJECT_MAP.template.md` | `project-kb/02_PROJECT_MAP.md` | Product or repository area map with ownership |
| `03_SYSTEM_ARCHITECTURE.template.md` | `project-kb/03_SYSTEM_ARCHITECTURE.md` | Architecture summary and source-of-truth owners |
| `04_DOMAIN_MODEL.template.md` | `project-kb/04_DOMAIN_MODEL.md` | Shared vocabulary and boundary rules |
| `05_IMPLEMENTATION_STATUS.template.md` | `project-kb/05_IMPLEMENTATION_STATUS.md` | Included, planned, excluded, released, and deprecated state |
| `06_WORKFLOW_AND_RULES.template.md` | `project-kb/06_WORKFLOW_AND_RULES.md` | Recovery-oriented workflow summary |
| `07_DECISIONS_LOG.template.md` | `project-kb/07_DECISIONS_LOG.md` | Accepted decisions and consequences |
| `08_CURRENT_STATE.template.md` | `project-kb/08_CURRENT_STATE.md` | Current recovery point and next work |
| `09_TASK_HISTORY.template.md` | `project-kb/09_TASK_HISTORY.md` | Durable task history after meaningful work |
| `10_REFERENCE.template.md` | `project-kb/10_REFERENCE.md` | Canonical reference map |

## Memory Levels

Use the smallest owner that can preserve recovery:

```text
Project Memory
-> Domain Memory
-> Module Memory
-> Subsystem Memory
-> Feature Memory
```

Root Project Memory should stay compact.

If a domain, module, subsystem, or feature becomes too detailed, move the details to a lower-level owner and link to it from root memory.

## Installation Rules

1. Replace placeholders such as `<PROJECT_NAME>`, `<OWNER_REPO>`, and `<BRANCH_NAME>`.
2. Remove sections that do not apply.
3. Keep status language truthful: `proposed`, `planned`, `included`, `implemented`, `released`, `deprecated`, or `excluded`.
4. Link to owner documents instead of copying their full content.
5. Do not store private chat history.
6. Do not store implementation claims without evidence.
7. Do not present planned work as implemented.

## Recovery Check

After installation, a fresh session must be able to answer:

- what repository this is;
- what the project is;
- what is included;
- what is planned;
- what is excluded;
- what current work is active;
- which owner documents govern the next task;
- what validation is required before work starts.

If a fresh session needs old chat history to continue, Project Memory is incomplete.
