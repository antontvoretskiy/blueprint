# Blueprint Feature Lifecycle Standard

This standard defines how meaningful work moves from request to implementation in a repository that adopts Blueprint.

The goal is not bureaucracy. The goal is to prevent implementation from starting before scope, ownership, validation, and handoff are clear.

## Lifecycle

```text
Idea
  -> Clarification
  -> Plan
  -> Tasks
  -> Implementation
  -> Validation
  -> PR
  -> Merge
  -> Repository state update
  -> Clean start
```

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

At minimum:

```bash
make doctor
make smoke
git diff --check
```

For public docs, also run:

- forbidden public wording scan;
- product-term scan;
- README local links check;
- bad commit wording scan;
- noisy AI phrase scan.

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
