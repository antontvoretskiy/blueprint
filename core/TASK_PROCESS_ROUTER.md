# Blueprint Task Process Router

This router classifies work before implementation starts.

Its purpose is to keep tasks scoped, route them to the right owner documents, and prevent a single PR from mixing unrelated operating layers.

## Router Output Format

Before any meaningful task, the agent must output or internally record:

```text
Detected Task Type:
Detected Process Level:
Required Rules:
Required Artifacts:
Skipped Rules:
Reason:
```

For tiny answer-only tasks, this can remain internal.

For file changes, broad tasks, risky tasks, migrations, architecture changes, PR work, or release work, include the router output in the plan or first user-facing update.

## Routing Inputs

Before choosing a route, identify:

- user intent;
- repository and branch;
- requested paths;
- affected operating layer;
- whether the task is read-only;
- whether implementation is allowed;
- validation requirements;
- explicit exclusions.

## Process Levels

| Level | Meaning | Typical checks |
| --- | --- | --- |
| L0 | Trivial change | Repository identity when editing, scope check, `git diff --check` |
| L1 | Documentation or small scoped change | Ownership check, source-of-truth check, docs validation |
| L2 | Scoped layer change | Layer governance, boundary checks, relevant validation |
| L3 | Meaningful feature implementation | Feature Lifecycle required before implementation |
| L4 | Architecture, migration, release, or merge | Full Guardian, source-of-truth, memory, release, or migration gates |

Do not apply L4 ceremony to L0/L1 tasks. The router exists to reduce governance overload, not add bureaucracy.

## Process Efficiency Rule

Use the lightest process level that protects the repository.

If a task is docs-only, answer-only, status-only, or a small scoped report, default to L0 or L1 unless it changes a source-of-truth model, release state, branch state, architecture boundary, migration plan, public asset version, or implementation behavior.

Process level is a control, not a status symbol.

Escalate only when the task adds real risk. Do not escalate because the repository has strict governance.

An ordinary commit on an already scoped work branch is not a branch-state
change by itself. Treat branch state as changed only when the task changes the
branch strategy, base branch, target branch, merge state, release branch, tag,
branch cleanup, branch synchronization, or published remote state.

## Context Budget By Process Level

Process levels limit both procedure and context loading.

Do not spend L4 context on L0/L1 work. If the task is narrower than the report,
the process level was wrong.

Root docs are loaded once per meaningful work session, not before every L0 or
L1 action. Do not reload context that is already represented by
`memory/project-kb/08_CURRENT_STATE.md` unless the task needs the original
owner document.

For L0 and L1, cite or mention only the specific file or command that changed
the decision.

### L0 Context Budget

Use L0 for status checks, clean checks, read-only branch checks, answer-only
repository questions, and sync checks that do not change branch state.

Allowed context:

- current command output;
- `git status`;
- current branch;
- current task instruction.

Forbidden context:

- do not read the full Project Memory;
- do not read architecture docs;
- do not read the governance bundle;
- do not write a full final report.

Maximum response:

```text
3-5 lines
```

Template:

```text
Status: ...
Validation: ...
Next: ...
```

### L1 Context Budget

Use L1 for docs-only commits, PR-ready handoff reports, small memory updates,
and scoped documentation fixes without ownership, release, branch-state,
architecture, migration, public asset, or implementation triggers.

Allowed context:

- touched file list;
- relevant owner document only when needed;
- `git diff` or `git status`;
- direct user instruction.

Forbidden context:

- do not reread all root docs;
- do not repeat the full forbidden-scope list;
- do not write a long `Not Changed` block.

Maximum response:

```text
10 lines
```

Template:

```text
Summary: ...
Files: ...
Validation: ...
Next: ...
```

### L2 Context Budget

Use L2 for scoped layer changes that affect a specific owner document or layer
but do not change architecture ownership, release state, branch state,
migration state, or implementation behavior.

Allowed context:

- owner document;
- touched domain or layer docs;
- validation commands.

Maximum response:

```text
20 lines unless FAIL/risk.
```

### L3 And L4 Context Budget

Use full process only for:

- new architecture decision;
- migration;
- runtime behavior change;
- extraction implementation with broad scope;
- release or merge conflicts;
- cross-domain work.

Branch synchronization, merge, branch cleanup, push-to-release, tag, and release
PR work remain L4 because they change branch or release state.

## Compact Mode For L0 And L1

Compact mode is required for L0 and L1 tasks unless the maintainer explicitly asks for a full audit.

Compact mode keeps the safety gates but removes repeated ceremony.

Required compact checks:

- repository identity when editing or reporting repository state;
- current branch and dirty worktree check;
- owner or scope check;
- no hidden runtime, code, dependency, or release-state changes;
- validation honesty with `PASS`, `FAIL`, `NOT RUN`, or `N/A`;
- repository files remain the source of truth.

Allowed compact output:

```text
Repo:
Branch:
Scope:
Changed:
Validation:
Risks:
Next:
```

For L0/L1 tasks, do not repeat the full forbidden-action list when:

- the repository identity is correct;
- the work is explicitly docs-only or read-only;
- no source-reference repository is being modified;
- the diff contains no runtime, code, dependency, release, or branch-state changes.

### L0 Compact Template

Use for clean status checks, typo fixes, tiny formatting changes, and answer-only repository checks.

```text
Repo: <owner>/<repo>
Branch: <branch>
Status: <clean/dirty>
Validation: <git diff --check or N/A>
Risk: <none/short>
Next: <one action>
```

### L1 Docs-Only Compact Template

Use for docs-only architecture wording, PR-ready handoff, clean-start report, small memory/status updates, and docs-only commits.

```text
Repo: <owner>/<repo>
Branch: <branch> -> <base>
Scope: docs-only
Changed: <files>
Validation:
- dirty tree before: <clean/dirty>
- scope check: PASS
- no runtime/code changes: PASS
- docs checks: <PASS/NOT RUN with reason>
Risks: <short>
Next: <commit/PR/merge/wait>
```

### Compact Escalation Triggers

Move out of compact mode when any of these are true:

- architecture ownership or source-of-truth boundaries change;
- release state, version, tag, merge, or branch policy changes;
- migration, source-reference transfer, or branch snapshot movement is involved;
- a public template, example, checklist, or installable bundle is added or versioned;
- implementation, runtime, CLI, automation, dependency, or integration files change;
- a docs claim requires runtime or product evidence;
- the task spans multiple operating layers.

Do not escalate L0 or L1 work to L4 only because the repository contains strict
governance. L4 requires a real architecture, migration, release, merge, or
branch-state trigger.

### Process-Level Regression Guard

When validating the router itself, a `PASS` result requires sample tasks, the
expected process level, the actual selected process level, and a mismatch
result.

Do not mark process-level routing as validated by checking only that L0-L4
rules exist in this file.

Router regression validation must prove:

- L0 tasks stay L0 unless an escalation trigger is present;
- L1 docs-only tasks stay L1 unless an escalation trigger is present;
- PR-ready handoff reports do not become release or merge work by default;
- clean status checks stay L0;
- docs-only commits on scoped branches stay L1;
- meaningful feature work escalates to L3;
- architecture, migration, release, merge, and branch synchronization work
  escalates to L4.

## Task Classes

| Task class | Description | Default action |
| --- | --- | --- |
| Answer-only | The user asks a question and does not request changes | Answer with file or command evidence when useful |
| Audit-only | The user asks for review, plan, or assessment without changes | Inspect, report findings, do not edit files |
| Bootstrap docs | Root presentation, scope, architecture, manifest, contribution rules | Update root docs and public validation surface |
| Core contract | Portable agent, routing, lifecycle, handoff, or security rules | Update `core/**` and any truthful root status docs |
| Governance standard | Branch, PR, verification, documentation, ADR, or authority-map rules | Use `governance/**` after that layer exists |
| Project Memory | Current state, decisions, task history, recovery points | Use `memory/**` after that layer exists |
| Template bundle | Reusable installable artifacts | Use `templates/**` after templates are approved |
| Example project | Sanitized adoption example | Use `examples/**` after examples are approved |
| Checklist | Installation, recovery, branch, PR, or clean-start checklist | Use `checklists/**` after checklists are approved |
| Architecture change | Layer boundary, ownership, source-of-truth, or long-term compatibility change | Require architecture review and decision logging when needed |
| Migration | Large transfer, import, conversion, or branch snapshot movement | Require source/target anchors, matrix, exclusions, rollback, and validation plan |
| Release | Version bump, manifest, release notes, release PR | Follow SemVer and release PR standards |

If a task spans multiple classes, split it unless the maintainer explicitly approves a combined PR.

## Class Processes

### 1. Trivial Change

Examples:

- typo;
- copy edit;
- small formatting fix;
- single-line non-behavior change.

Process:

- confirm repository identity if editing;
- confirm scope;
- inspect changed files;
- run `git diff --check` when files changed;
- use L0 compact output.

Skipped by default:

- full Guardian;
- Feature Lifecycle;
- architecture review;
- migration matrix.

### 2. Documentation Change

Examples:

- docs update;
- governance update;
- audit report;
- memory or status update.

Process:

- confirm repository identity;
- identify owner document;
- check source-of-truth ownership;
- confirm docs-only scope;
- run docs validation that matches the changed files;
- use L1 compact output unless the task hits a compact escalation trigger.

Product or runtime validation is not required unless the docs claim product behavior, implementation status, or release readiness changed.

### 3. Scoped Layer Change

Examples:

- core contract update;
- governance standard update;
- Project Memory update;
- template bundle after approval;
- example or checklist after approval.

Process:

- identify layer owner;
- verify allowed paths;
- verify forbidden future layers are absent;
- run layer-specific validation;
- update root status docs only when public claims change.

Feature Lifecycle is required only when the change is a meaningful feature, new installable bundle, new public surface, or cross-layer workflow.

### 4. Feature Implementation

Examples:

- new meaningful feature;
- new service;
- new module;
- new integration;
- significant user-facing or repository-facing workflow.

Process:

- follow `core/FEATURE_LIFECYCLE_STANDARD.md`;
- prepare required feature artifacts before implementation;
- run Guardian validation before implementation;
- report validation evidence in the PR.

If required artifacts are missing:

```text
VALIDATION FAILED
```

Do not implement until missing artifacts are prepared or the maintainer explicitly scopes the work down.

### 5. Architecture Change

Examples:

- new layer;
- new owner document;
- new source-of-truth model;
- incompatible framework decision;
- branch or release strategy change.

Process:

- run architecture review;
- identify source-of-truth impact;
- create or update an ADR when needed;
- update governance index when ownership changes;
- update current state when recovery changes;
- run full Guardian.

Architecture direction must not be presented as implemented tooling.

### 6. Migration

Examples:

- source-reference transfer;
- branch snapshot transfer;
- repository import;
- large structured conversion.

Process:

- identify source branch, commit, and target branch;
- build include, review, and exclude matrices;
- define rollback plan;
- define validation plan;
- run full Guardian.

Do not import private product memory or product-specific implementation details into portable Blueprint files.

### 7. Release / PR / Merge

Examples:

- PR creation;
- merge preparation;
- release PR;
- post-merge clean start;
- final validation.

Process:

- use `core/AGENTS.md`;
- use `governance/docs/pr-standard.md`;
- use `governance/docs/git-policy.md`;
- use `governance/docs/verification-standard.md`;
- use `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md`;
- update current state or task history when meaningful;
- report final state.

Never push, create a PR, or merge without explicit approval.

## Router Decision Table

| Task type | Process level | Feature Lifecycle | Full Guardian |
| --- | --- | --- |
| Trivial change | L0 | No | No |
| Documentation change | L1 | No | Only if source-of-truth or architecture changes |
| Scoped layer change | L2 | Only if meaningful public workflow changes | Layer Guardian |
| Feature implementation | L3 | Yes | Yes |
| Architecture change | L4 | Maybe, if it leads to implementation | Yes |
| Migration | L4 | No by default; use migration process | Yes |
| Release / PR / merge | L4 | No | PR or Release Guardian |

## Skipped Rules Must Be Explicit

When skipping major rules, state why.

Example:

```text
Skipped Rules:
- Feature Lifecycle: not required, docs-only governance update.
- Runtime validation: not required, no product runtime claims or code changes.
- Example validation: not required, no example files changed.
```

## Failure Modes

| Failure | Router response |
| --- | --- |
| Task type unclear | Classify as higher risk and decompose |
| Meaningful feature lacks artifacts | Stop: Feature Lifecycle required |
| Migration lacks matrix | Stop: migration process required |
| Architecture change lacks source-of-truth analysis | Stop: architecture review required |
| Simple task is being overloaded | Downgrade to L0/L1 and explain skipped rules |
| Scope crosses layers accidentally | Stop and ask for explicit approval or decomposition |
| Reference repository would be modified | Stop unless explicit approval changes the rule |

## Start Conditions

Implementation may start only when:

- repository identity is confirmed;
- branch strategy is clear;
- scope is explicit;
- forbidden paths are known;
- source references are read-only;
- relevant owner documents are identified.

If any condition is unclear and the risk is material, stop and ask for clarification.

## Branch Routing

Default Blueprint development flow:

```text
main
  -> develop
  -> docs/<scope> or fix/<scope>
  -> PR into develop
  -> release PR into main
```

Use `main` for release-ready public state. Use `develop` for integration work before release.

Do not create branches in a reference repository.

## Path Routing

| Requested work | Allowed paths |
| --- | --- |
| Public positioning | `README.md`, `OPEN_SOURCE_SPEC.md`, `ARCHITECTURE.md`, `BUNDLE_MANIFEST.md`, `CONTRIBUTING.md`, `docs/benchmarks/**`, `media/**`, `public/**` |
| Core contracts | `core/**`, plus minimal root status updates |
| Governance standards | `governance/**`, plus minimal root status updates |
| Project Memory | `memory/**`, plus minimal root status updates |
| Templates | `templates/**`, plus manifest and docs updates |
| Examples | `examples/**`, plus manifest and docs updates |
| Checklists | `checklists/**`, plus manifest and docs updates |

Minimal root status updates are allowed when they keep README, architecture, or manifest claims truthful.

## Stop Conditions

Stop before implementation when:

- the user requested audit-only work;
- the requested branch or repository does not match the task;
- the task would modify a read-only reference repository;
- the task requires forbidden product-specific content;
- the task would add runtime, generator, automation, or integration support without approval;
- validation cannot be run and no honest fallback is available.

## Output Requirements

Every completed implementation should report:

- branch;
- base branch;
- files changed;
- validation results;
- PR link when a PR is created;
- risks;
- next step.
