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

## Recovery Path

For a fresh session, read:

1. `README.md`
2. `OPEN_SOURCE_SPEC.md`
3. `ARCHITECTURE.md`
4. `BUNDLE_MANIFEST.md`
5. `CONTRIBUTING.md`
6. `core/TASK_PROCESS_ROUTER.md`

When Project Memory is added later, the recovery path will also load the memory index and current-state files. Until then, the root specification and core contracts are the recovery baseline.

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

## Agent Hygiene

Do not add noisy generation disclaimers, low-signal commit titles, accidental AI co-author trailers, or unreviewed generated output.

The contributor is accountable for the submitted repository state.
