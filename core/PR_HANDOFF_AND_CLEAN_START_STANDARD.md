# Blueprint PR Handoff And Clean Start Standard

This standard defines how a Blueprint PR stays reviewable and how work becomes recoverable after merge.

## PR Principle

One PR should have one scope, one branch family, and one review story.

If a PR mixes unrelated layers, reviewers cannot validate boundaries or recover context reliably.

## PR Handoff Flow

Before PR or merge, complete:

```text
Implementation
  -> Validation
  -> PR Handoff
  -> Memory Update Check
  -> Repository Update
  -> PR / Merge
  -> Clean Start
```

The handoff is not a replacement for Project Memory. It is a consistency checkpoint that verifies the repository contains enough context for review, merge, and the next session.

## Required PR Body

Meaningful PRs must use:

```text
## Problem

## Solution

## Scope

## Validation

## Risks

## Follow-ups
```

The PR body is a handoff artifact. It must explain what changed, what did not change, and how the change was validated.

## PR Handoff Summary

Before PR, prepare a concise handoff summary.

Required shape:

```text
### Repository Identity
- repository:
- branch:
- HEAD:

### Scope
- work performed:
- allowed scope:

### Changed
- files changed:
- files created:

### Not Changed
- runtime:
- contracts:
- tests:
- CI:
- dependencies:

### Validation
- build:
- tests:
- lint:
- typecheck:
- local review:
- visual review:

### Risks
- ...

### Next Step
- ...
```

Use `PASS`, `FAIL`, or `NOT RUN: reason` for validation results.

The handoff summary may live in a PR body, release report, or clean-start brief. It must not become a second source of truth.

## Scope Section

The Scope section should list:

- included paths;
- explicitly excluded paths;
- branch base;
- whether the PR targets `develop` or `main`;
- whether the change affects public release state.

For Blueprint itself, default development PRs target `develop`. Release PRs target `main`.

## Validation Section

Validation must include commands and outcomes.

Use `PASS`, `FAIL`, or `NOT RUN` with a reason.

Do not report a validation command as passing if it masked an error. If a command gives a false positive, fix the command or report the limitation.

Minimum compact validation for L1 docs-only PRs:

```bash
git diff --check
```

Also confirm:

- dirty worktree state was checked before staging;
- changed files match docs-only scope;
- no runtime, code, dependency, release-state, or branch-state changes are hidden in the diff;
- skipped validation is reported as `NOT RUN` or `N/A` with a reason.

Public-facing documentation should also include:

- forbidden public wording scan;
- product-term scan;
- README local links check;
- commit and PR title quality check;
- noisy AI phrase scan;
- bad commit wording scan.

Run `make doctor` and `make smoke` when local preview, release readiness, environment files, or validation claims depend on them. Do not require preview validation for a small docs-only handoff that does not touch preview behavior.

## Memory Update Check

Before PR, check whether the work requires updates to:

- current state;
- implementation status;
- decisions log;
- reference map;
- task history;
- active clean-start brief;
- relevant owner documents.

Rules:

```text
Do not update memory without a reason.
Do not leave meaningful changes only in chat.
```

Update memory only when repository state, implementation reality, accepted decisions, owner boundaries, recovery point, or navigation paths changed.

If no memory update is needed, the handoff must state why.

## Repository First Rule

After PR or merge, source of truth must be in repository documents.

Repository source of truth includes:

- core contracts;
- governance documents;
- Project Memory;
- architecture decisions;
- active feature lifecycle artifacts;
- implementation files and validation evidence when they prove implementation reality.

The following are not source of truth:

- chat;
- old handoff;
- old clean-start brief;
- model memory;
- unmerged local notes;
- screenshots without repository evidence.

If critical context exists only in chat, the task is not ready for PR or merge.

## Commit And PR Titles

Use the public title standard from `CONTRIBUTING.md`.

Default format:

```text
type(scope): concise outcome
```

Examples:

```text
docs(core): add portable operating contracts
docs(governance): add branch and PR standards
docs(memory): add project memory templates
fix(docs): repair manifest links
```

Do not use placeholder or low-signal titles.

## Handoff Checklist

Before requesting review:

- repository identity is confirmed;
- base branch is correct;
- changed files match scope;
- root docs and manifest remain truthful;
- private source terms are absent;
- validation results are current;
- risks and follow-ups are listed;
- commit title and PR title are clean.

## Merge Rules

For Blueprint itself:

```text
feature branch
  -> PR into develop
  -> reviewed integration
  -> release PR from develop into main
```

`main` represents release-ready public state. `develop` is the integration branch for unreleased work.

## Clean Start Rule

After merge, the next session should recover from:

- repository files;
- merged PR body;
- commit history;
- release or integration branch state.

Old chat history must not be required.

For repositories with Project Memory installed, standard recovery path:

```text
memory/project-kb/00_INDEX.md
  -> memory/project-kb/08_CURRENT_STATE.md
  -> memory/project-kb/05_IMPLEMENTATION_STATUS.md
  -> memory/project-kb/10_REFERENCE.md
  -> core/TASK_PROCESS_ROUTER.md
  -> Work
```

For architecture work, also load these files when present:

```text
memory/project-kb/07_DECISIONS_LOG.md
governance/docs/governance-index.md
governance/docs/adr-policy.md
```

For owner-specific work, load the relevant owner documents when present.

## Clean Start Brief

Only one active clean-start brief is allowed:

```text
memory/project-kb/current/CLEAN_START_BRIEF.md
```

The clean-start brief is a transition buffer. It is not Project Memory and must not become parallel history.

When a new clean start is needed, overwrite the existing brief.

Forbidden:

```text
CLEAN_START_001.md
CLEAN_START_002.md
CLEAN_START_003.md
```

The brief may contain:

- repository identity;
- merged PR or commit;
- current recovery point;
- next task;
- key owner documents;
- known risks;
- validation state.

The brief must point back to canonical repository documents. It must not store unique decisions or implementation claims that are absent from Project Memory, owner docs, architecture decisions, implementation files, or validation evidence.

## Feature Lifecycle Integration

If the next task is a new meaningful feature, `core/TASK_PROCESS_ROUTER.md` must classify it as Feature Implementation and require the artifacts defined by `core/FEATURE_LIFECYCLE_STANDARD.md`.

Do not use a handoff summary or clean-start brief as a substitute for Feature Lifecycle artifacts.

Completed feature artifacts remain historical context only.

## Guardian Integration

Guardian must check:

### Handoff Check

Confirm that a PR handoff exists for meaningful work and includes repository identity, scope, changed files, validation, risks, and next step.

### Memory Check

Confirm that required Project Memory or owner docs were updated, or that the handoff explains why no update was needed.

### Repository First Check

Confirm that critical context is not left only in chat.

### Clean Start Check

Confirm that the next session can recover from repository documents and that any clean-start brief is singular and points to canonical owners.

## Task Router Integration

Task Router decides how much process is required.

| Process level | Handoff expectation |
| --- | --- |
| L0 | Response summary is enough |
| L1 | Compact docs handoff when docs affect recovery, governance, or source of truth |
| L2 | Layer-specific validation and boundary handoff |
| L3 | Feature Lifecycle links plus PR handoff |
| L4 | Full Guardian, source-of-truth, memory update, and clean-start readiness |

Do not apply full handoff ceremony to trivial changes. Do require repository handoff when the next session or reviewer would lose important context without it.

### Compact L1 Handoff

Use this shape for docs-only commits, PR-ready handoffs, clean status checks, and post-merge sync reports when no release, merge, architecture, migration, runtime, code, dependency, or public asset version changed:

```text
Repo:
Branch:
Scope: docs-only
Changed:
Validation:
- dirty tree:
- scope check:
- no runtime/code changes:
- docs checks:
Risks:
Next:
```

Escalate from compact L1 handoff to the full handoff when the work changes release state, branch state, owner boundaries, architecture decisions, migrations, versioned public assets, or implementation claims.

## Conflict Resolution

This standard owns:

- PR handoff expectations;
- clean-start behavior after merge;
- clean-start brief rules;
- repository-first recovery expectation.

Adjacent owners remain authoritative:

| Area | Owner |
| --- | --- |
| PR title, body, and scope rules | `governance/docs/pr-standard.md` |
| Task classification | `core/TASK_PROCESS_ROUTER.md` |
| Feature planning artifacts | `core/FEATURE_LIFECYCLE_STANDARD.md` |
| Project Memory update rules | `memory/project-kb/06_WORKFLOW_AND_RULES.md` |
| Current recovery point | `memory/project-kb/08_CURRENT_STATE.md` |
| Guardian architecture | `memory/project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md` |
| Guardian validation scenarios | `memory/project-kb/GUARDIAN_VALIDATION_SCENARIOS.md` |

If a handoff conflicts with canonical repository docs, the canonical repository docs win and the handoff must be corrected.

## Forbidden Patterns

Do not:

- leave architecture decisions only in chat;
- leave implementation reality only in a handoff;
- create multiple clean-start briefs;
- use clean-start briefs as history files;
- use old chat summaries as source of truth;
- skip Project Memory checks before meaningful PRs;
- update Project Memory without a real repository-state reason;
- treat planned feature docs as implementation proof;
- treat architecture directions as implemented tooling.

## Clean Start Output

After merging a meaningful PR, report:

- merged PR link;
- merge commit or squash commit;
- target branch;
- deleted branches, if any;
- validation repeated after merge;
- next recommended branch;
- remaining risks.

When Project Memory exists, update the appropriate current-state or task-history files as part of the clean-start process.
