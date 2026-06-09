# PR Handoff Templates

Status: Template Bundle v0.2.0.

This bundle provides reusable PR handoff templates for repositories adopting Blueprint.

PR handoff keeps work reviewable, recoverable, and scoped before merge. It is not a replacement for Project Memory, owner documents, validation evidence, or feature artifacts.

## Install Target

When installed into another repository, render these templates into a location owned by the adopting project, such as:

```text
project-kb/templates/pr-handoff/
```

Blueprint keeps reusable templates under:

```text
templates/pr-handoff/
```

## Template Files

| Template | Purpose |
| --- | --- |
| `PR_BODY.template.md` | Standard meaningful PR body |
| `PR_HANDOFF.template.md` | Pre-review handoff summary |
| `MEMORY_UPDATE_DECISION.template.md` | Decision record for whether Project Memory or owner docs need updates |
| `CLEAN_START_TRANSITION.template.md` | Post-merge transition summary for the next session |

## When To Use

Use these templates for:

- meaningful documentation changes;
- template bundles;
- governance changes;
- feature implementation PRs;
- architecture changes;
- migrations;
- release preparation;
- any PR where the next reviewer or session would lose context without handoff.

For L0 tasks, a response summary is enough.

For L1 tasks, use a docs handoff only when the docs affect recovery, governance, or source of truth.

## Handoff Flow

```text
Implementation
-> Validation
-> PR Handoff
-> Memory Update Decision
-> Repository Update
-> PR / Merge
-> Clean Start Transition
```

## Installation Rules

1. Replace placeholders such as `<OWNER_REPO>`, `<BRANCH_NAME>`, and `<VALIDATION_COMMAND>`.
2. Remove sections that do not apply.
3. Use `PASS`, `FAIL`, or `NOT RUN: <reason>` for validation.
4. Keep included and excluded scope explicit.
5. Do not leave meaningful state only in chat.
6. Do not update Project Memory without a durable state reason.
7. Do not use the clean-start transition as a parallel memory system.
