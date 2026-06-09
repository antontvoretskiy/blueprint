# Blueprint Recovery Templates

Asset: recovery-templates
Version: v0.3.0
Type: Template Bundle
Author: Blueprint Maintainers
Status: Included

These templates help a repository recover work from versioned files instead of old chat history.

They are portable starting points. Adapt placeholders before using them in another repository.

## Included Templates

| Template | Purpose |
| --- | --- |
| `RECOVERY_PATH.template.md` | Defines how a new session recovers repository state |
| `CLEAN_START_BRIEF.template.md` | Provides the single active clean-start brief format |
| `RECOVERY_VALIDATION.template.md` | Checks whether recovery works without old chat history |

## Install Target

Recommended target paths:

| Template | Target path |
| --- | --- |
| `RECOVERY_PATH.template.md` | `project-kb/current/RECOVERY_PATH.md` or a linked section in `project-kb/00_INDEX.md` |
| `CLEAN_START_BRIEF.template.md` | `project-kb/current/CLEAN_START_BRIEF.md` |
| `RECOVERY_VALIDATION.template.md` | `project-kb/current/RECOVERY_VALIDATION.md` or a PR validation artifact |

Use one active clean-start brief at a time.

Do not create numbered clean-start brief files.

## Adaptation Rules

When adapting these templates:

1. Replace every placeholder.
2. Keep repository identity explicit.
3. Link to canonical owner documents instead of duplicating full standards.
4. Mark planned work as planned.
5. Keep private product history out of reusable templates.
6. Run a recovery validation from a fresh session.

## Non-Goals

These templates do not provide:

- automation;
- CLI commands;
- runtime behavior;
- agent runtime;
- workflow engine;
- code generation;
- external service integration.

They define a manual recovery contract that can be automated later.
