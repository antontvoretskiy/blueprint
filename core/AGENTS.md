# Blueprint Agent Operating Contract

This document is the portable entrypoint for humans and AI agents working in a repository that adopts Blueprint.

It defines how an agent starts work, recovers context, protects repository boundaries, validates claims, and hands off work without relying on chat history as durable state.

## Core Rule

The repository is the source of truth.

Chat history can provide session execution context, but durable rules, decisions, validation evidence, and current state must live in versioned repository files.

## Start Gate

Before changing files, an agent must confirm:

1. Repository identity.
2. Current branch and intended base branch.
3. Whether the task is audit-only, planning-only, or implementation.
4. Which paths are in scope.
5. Which paths are explicitly out of scope.
6. Whether any reference repository is read-only.
7. Whether the working tree already contains unrelated changes.

If the task names a reference repository, the agent may inspect it only as a source reference. The agent must not create branches, commits, PRs, issues, tags, or file changes in that reference repository unless the maintainer gives explicit approval.

## Mandatory First Checks

For any task that may change files, branches, PRs, release state, or public documentation, perform:

1. repository identity check;
2. branch and base branch check;
3. working tree check;
4. scope and forbidden-path check;
5. source-reference read-only check;
6. task classification through `core/TASK_PROCESS_ROUTER.md`;
7. validation plan check.

If any check fails, stop before editing and report the blocker.

For audit-only work, do not edit files and do not create branches or PRs.

## Recovery Path

For a fresh session, read:

1. `README.md`
2. `OPEN_SOURCE_SPEC.md`
3. `PRODUCT_MAP.md`
4. `ARCHITECTURE.md`
5. `BUNDLE_MANIFEST.md`
6. `memory/project-kb/00_INDEX.md`
7. `memory/project-kb/08_CURRENT_STATE.md`
8. `memory/project-kb/05_IMPLEMENTATION_STATUS.md`
9. `memory/project-kb/10_REFERENCE.md`
10. `core/TASK_PROCESS_ROUTER.md`
11. `CONTRIBUTING.md`

Load governance documents when the task changes rules, branch policy, PR standards, validation, documentation, or ADR policy.

Load `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` and `memory/project-kb/12_SYSTEM_RELATIONSHIP_MAP.md` when the task changes source-reference coverage, ownership, system relationships, process levels, project management, feature management, or transfer completeness.

## Source Of Truth Priority

Use this priority order when evidence conflicts:

1. repository files on the active branch;
2. merged PR history;
3. current open PR body and diff;
4. explicit maintainer instruction in the current task;
5. chat context.

Chat context may guide execution, but it must not override canonical repository files unless the maintainer explicitly asks to change those files.

When documentation and implementation conflict, report the conflict. Do not silently make implementation claims that documentation does not support.

## Task Flow

For every meaningful task:

1. Classify the task with `core/TASK_PROCESS_ROUTER.md`.
2. Identify the canonical owner document for the rule being changed.
3. Produce a short audit or implementation plan when scope is non-trivial.
4. Edit only approved paths.
5. Keep one PR to one scope.
6. Run the required validation.
7. Report results honestly.
8. Update handoff notes in the PR body.

Do not start implementation when the user asks for audit-only, planning-only, or read-only work.

## Source Reference Handling

When a task uses a source-reference repository:

- read only the files needed for the current scope;
- record the source branch and commit when relevant;
- classify each source file as include, parameterize, convert to template, review, or exclude;
- remove product-specific names, paths, release history, incidents, and private project memory;
- preserve portable rules and relationships;
- do not create branches, commits, tags, issues, or PRs in the source-reference repository.

## Scope Guard

Blueprint core may define operating rules for repositories that contain product code, services, applications, agents, providers, or infrastructure.

Blueprint core must not contain those product implementations.

Do not add to core:

- runtime framework;
- agent runtime;
- workflow engine;
- code generator;
- product UI;
- product API;
- product algorithms;
- private product memory;
- product-specific release history;
- private source-reference anchors.

## Sanitization Requirement

Any imported or adapted rule must be made portable.

Replace private names, domain names, product paths, incidents, PR numbers, milestones, owners, and release history with generic placeholders before the content enters Blueprint.

Use placeholders such as:

- `<PROJECT_NAME>`
- `<OWNER>/<REPO>`
- `<DOMAIN_A>`
- `<DOMAIN_B>`
- `<PROJECT_SPECIFIC_MODULE>`
- `<PROJECT_SPECIFIC_MILESTONE>`

## Validation Requirement

At minimum, run:

```bash
make doctor
make smoke
```

For public-facing documentation changes, also run:

- forbidden public wording scan;
- product-term scan;
- README local links check;
- markdown or whitespace check;
- `git diff --check`;
- commit and PR title quality check;
- noisy AI phrase scan.

Validation failures must be fixed or reported. Do not report a validation command as passing if it returned a false positive or masked an error.

## PR Handoff Requirement

Meaningful PRs must include:

- Problem;
- Solution;
- Scope;
- Validation;
- Risks;
- Follow-ups.

The PR body must make it clear what was included, what was deliberately excluded, and what validation evidence supports the change.

## Clean Start Requirement

After a PR is merged, the next session must be able to recover from repository state and PR history.

If a future agent needs old chat history to understand what happened, the handoff failed.

## Final Report Requirement

After completing implementation, report:

- repository;
- branch;
- base branch;
- files changed;
- validation results;
- PR link, when created;
- what was explicitly not changed;
- risks;
- next step.

For read-only audits, report the source commit inspected, target branch inspected, mapping gaps, and recommended next action.

## Agent Hygiene

Do not add noisy generation disclaimers, low-signal commit titles, accidental AI co-author trailers, or unreviewed generated output.

The contributor is accountable for the submitted repository state.
