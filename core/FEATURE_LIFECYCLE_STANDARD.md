# Blueprint Feature Lifecycle Standard

This standard defines how meaningful work moves from request to implementation in a repository that adopts Blueprint.

The goal is not bureaucracy. The goal is to prevent implementation from starting before scope, ownership, validation, and handoff are clear.

## Core Principle

Every meaningful feature must pass through clarification, planning, task breakdown, and Guardian validation before implementation.

Do not move directly to implementation from:

- chat;
- idea;
- note;
- ADR;
- informal discussion;
- visual mockup;
- branch snapshot.

## Lifecycle

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

Implementation begins only after required artifacts exist and critical open questions are resolved.

## Required Feature Directory

When feature artifacts exist, use:

```text
memory/project-kb/features/<feature-name>/
```

Required files:

```text
FEATURE.md
CLARIFICATION.md
PLAN.md
TASKS.md
```

Feature templates will be added later. Until then, the PR body may serve as the minimum lifecycle artifact for small meaningful documentation features.

## FEATURE.md

Purpose: define what must be built and why it matters.

Required sections:

- User Scenarios;
- User Stories P1/P2/P3;
- Edge Cases;
- Functional Requirements `FR-001...`;
- Key Entities;
- Success Criteria `SC-001...`;
- Assumptions.

Rules:

- user stories must be independently reviewable;
- functional requirements must be testable;
- success criteria must be concrete;
- assumptions must not hide critical unknowns.

## CLARIFICATION.md

Purpose: record questions, answers, decisions, and reasons before planning.

Required table:

| Question | Decision | Reason |
| --- | --- | --- |

Rules:

- critical open questions block `PLAN.md`;
- non-critical open questions may remain only if explicitly marked;
- clarification decisions must not become architecture decisions unless routed through the ADR process.

## PLAN.md

Purpose: define how the feature will be built.

Required sections:

- Summary;
- Technical Context;
- Governance Check;
- Research;
- Data Model or Document Model;
- Validation Strategy.

Rules:

- Technical Context must identify affected layers;
- Governance Check must reference relevant core and governance docs;
- Data Model or Document Model must identify owners and source of truth;
- Validation Strategy must list commands and manual checks.

## TASKS.md

Purpose: break the feature into small, reviewable, reversible work.

Suggested phases:

```text
Phase 1 - Setup
Phase 2 - Foundation
Phase 3 - Priority 1
Phase 4 - Priority 2
Phase 5 - Priority 3
Phase 6 - Polish
```

Rules:

- each task must be independently reviewable;
- tasks must not mix unrelated layers;
- API, UI, contract, documentation, template, and infrastructure changes should be separated when possible;
- migration tasks require a migration matrix.

## When The Lifecycle Is Required

Use the lifecycle for meaningful changes such as:

- new user-facing behavior;
- new backend behavior;
- new module;
- new service;
- new integration;
- architecture-impacting change;
- data migration;
- large refactor;
- new operating rule;
- new template bundle;
- new example bundle.

## When The Lifecycle Can Be Skipped

The full lifecycle is not required for:

- typo fixes;
- broken links;
- small formatting corrections;
- small wording improvements that do not change scope;
- mechanical reference updates.

Even when the full lifecycle is skipped, validation and truthful reporting still apply.

## Required Planning Questions

Before implementation, answer:

1. What problem is being solved?
2. Which operating layer owns the work?
3. Which paths are allowed?
4. Which paths are excluded?
5. What claims will be true after the change?
6. What validation proves those claims?
7. What follow-up work remains outside this PR?

## Suggested Artifacts

For large feature work, use these artifacts when templates are available:

- `FEATURE.md`
- `CLARIFICATION.md`
- `PLAN.md`
- `TASKS.md`

Until templates exist, a PR body with Problem, Solution, Scope, Validation, Risks, and Follow-ups is the minimum accepted lifecycle artifact.

## Guardian Integration

Before implementation, Guardian checks for:

- `FEATURE.md`;
- `CLARIFICATION.md`;
- `PLAN.md`;
- `TASKS.md`;
- resolved critical questions;
- relevant governance rules;
- relevant architecture decisions;
- security boundaries;
- validation plan.

If required artifacts are missing:

```text
VALIDATION FAILED
```

The agent must stop and produce or request the missing artifact before implementation.

## PR Requirements

A meaningful feature PR cannot be considered complete without:

- link or path to feature artifacts when they exist;
- Guardian validation result;
- validation evidence;
- memory or status update, or explicit reason not needed;
- clear included and excluded scope.

The PR must not use feature docs as proof of implementation. Repository files, tests, contracts, artifacts, and validation remain implementation evidence.

## Memory Update Rules

After implementation, check and update:

- implementation status, if implementation reality changed;
- current state, if current recovery point changed;
- decisions log, if new architecture or governance decisions were made;
- relevant owner documents;
- reference map, if navigation changed.

Do not invent implementation status from planned feature docs.

## Feature Lifecycle Ownership

Feature lifecycle documents are planning and execution artifacts.

They are not long-term source of truth after the feature is completed.

| Artifact | Long-term role |
| --- | --- |
| `FEATURE.md` | Archived requirements record |
| `CLARIFICATION.md` | Archived clarification trace |
| `PLAN.md` | Archived technical plan |
| `TASKS.md` | Archived execution checklist |

Completed feature artifacts may explain historical intent and execution history, but they must not override:

1. implementation status;
2. architecture decisions;
3. owner documents;
4. current state;
5. decisions log;
6. task history;
7. validation evidence.

## Feature Lifecycle Completion Rules

Feature lifecycle states:

```text
Planning
  -> Implementation
  -> Completed
  -> Archived
```

After a feature is completed:

1. update implementation status if implementation reality changed;
2. update current state;
3. update decisions log if new decisions were made;
4. update task history if the feature is milestone-worthy;
5. mark feature artifacts as `Completed` or `Archived`;
6. add links to relevant PRs, owner docs, or status docs when available.

Completed feature artifacts remain historical context only. They are no longer the active source of truth.

## Status Language

Documentation must distinguish:

- planned;
- proposed;
- included;
- implemented;
- released;
- deprecated;
- excluded.

Do not present planned work as implemented.

Do not present examples as required installation steps.

Do not present optional extensions as core.

## Scope Rules

One meaningful feature should map to one operating scope.

If a feature touches multiple scopes, split it into smaller PRs unless there is a clear reason to land the scopes together.

Examples:

- Core contract PR: `core/**` plus minimal root status updates.
- Governance PR: `governance/**` plus minimal root status updates.
- Template PR: `templates/**` plus manifest and usage docs.
- Example PR: `examples/**` plus manifest and README links.

## Validation

Validation should match the change.

For L1 docs-only work, use the compact validation path from `core/TASK_PROCESS_ROUTER.md`:

```bash
git diff --check
```

For public docs, also run:

- forbidden public wording scan;
- product-term scan;
- README local links check;
- bad commit wording scan;
- noisy AI phrase scan.

Run `make doctor` and `make smoke` when the change touches local preview files, environment files, release readiness, or claims about local validation behavior.

For future templates or examples, add installation or adoption validation once those assets exist.

## Definition Of Done

A meaningful feature is done when:

- the scope is clear;
- included and excluded paths are explicit;
- documentation is truthful;
- validation evidence is reported;
- the PR body can serve as handoff;
- no private product memory or source-specific data leaked;
- the next session can recover without old chat history.
