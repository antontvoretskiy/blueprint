# Feature Lifecycle Templates

Status: Template Bundle v0.2.0.

This bundle provides reusable Feature Lifecycle templates for repositories adopting Blueprint.

Feature Lifecycle artifacts prevent implementation from starting before scope, ownership, validation, and handoff are clear.

## Install Target

When installed into another repository, render these templates into:

```text
project-kb/features/<feature-name>/
```

Blueprint keeps reusable templates under:

```text
templates/feature-lifecycle/
```

## Template Files

| Template | Rendered file | Purpose |
| --- | --- | --- |
| `FEATURE.template.md` | `FEATURE.md` | Defines what must be built and why it matters |
| `CLARIFICATION.template.md` | `CLARIFICATION.md` | Records questions, decisions, and reasons before planning |
| `PLAN.template.md` | `PLAN.md` | Defines how the feature will be built |
| `TASKS.template.md` | `TASKS.md` | Breaks the feature into small, reviewable work |

## Lifecycle Flow

```text
Idea
-> Feature Specification
-> Clarification
-> Technical Planning
-> Task Breakdown
-> Guardian Validation
-> Implementation
-> PR Review
-> Repository State Update
-> Clean Start
```

## When To Use

Use these templates for:

- meaningful user-facing behavior;
- meaningful backend behavior;
- new modules;
- new services;
- new integrations;
- architecture-impacting changes;
- data migrations;
- large refactors;
- new operating rules;
- new template bundles;
- new example bundles;
- cross-layer workflows.

Do not require the full lifecycle for:

- typos;
- broken links;
- small formatting corrections;
- small wording improvements that do not change scope;
- mechanical reference updates.

Even when the full lifecycle is skipped, validation and truthful reporting still apply.

## Artifact Ownership

Feature artifacts are planning and execution records.

After completion, they become historical context.

They must not override:

1. implementation status;
2. architecture decisions;
3. owner documents;
4. current state;
5. decisions log;
6. task history;
7. validation evidence.

## Installation Rules

1. Replace placeholders such as `<FEATURE_NAME>`, `<OWNER_PATH>`, and `<VALIDATION_COMMAND>`.
2. Remove sections that do not apply.
3. Keep functional requirements testable.
4. Keep success criteria concrete.
5. Resolve critical open questions before implementation.
6. Keep tasks small, reviewable, and scoped to one operating layer when possible.
7. Update Project Memory only when durable state changes.
8. Do not present feature docs as implementation proof.
