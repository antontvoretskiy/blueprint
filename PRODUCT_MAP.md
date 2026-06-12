# Blueprint Product Map

This document defines the complete Blueprint product shape before additional templates, examples, checklists, or automation are added.

It is the product-level map for what Blueprint manages, how its parts work together, and which artifacts must exist before Blueprint can be packaged as a complete public release.

## Product Definition

Blueprint is an operating framework for AI-native software development.

It helps repositories manage:

- governance;
- task routing;
- process levels;
- feature lifecycle;
- Project Memory;
- recovery between work sessions;
- Guardian checks;
- branch governance;
- PR lifecycle;
- PR handoff;
- clean start after merge.

Blueprint is repository-first.

Chat can help execution, but the repository owns durable state, rules, decisions, templates, validation evidence, and recovery points.

## Product Boundary

Blueprint governs project work.

Blueprint does not implement product work.

Blueprint core must not contain:

- runtime framework implementation;
- agent runtime implementation;
- workflow engine implementation;
- code generator implementation;
- MCP server implementation;
- SaaS starter kit implementation;
- product framework implementation;
- UI framework implementation;
- product-specific memory;
- product-specific release history;
- product-specific PR timeline;
- private source-reference anchors.

Blueprint may provide templates that help another repository govern those areas, but Blueprint core must not contain their implementation or private state.

## Complete Product Loop

Blueprint work moves through this loop:

```text
request
-> repository identity check
-> recovery path
-> task routing
-> process level selection
-> owner document lookup
-> scoped work
-> validation evidence
-> PR handoff when needed
-> Project Memory update when durable state changed
-> PR into the selected integration or release branch
-> merge
-> clean start
-> next recovery from repository
```

The loop is intentionally scalable. Small tasks do not pay the cost of full process. Meaningful, risky, architectural, or release work does.

## Public Distribution Model

The public Blueprint repository publishes release-ready framework state from `main`.

Maintainers may use local or private integration branches while preparing a release. Those branches are workflow details, not public distribution requirements.

Adopting repositories may choose:

- `main` only, with short-lived scoped branches;
- `main` plus an integration branch, when the team needs a staging branch before release.

The selected branch model must be recorded in the adopter repository Git policy and Project Memory.

## Subsystem Map

| Subsystem | Purpose | Canonical owner | Required now |
| --- | --- | --- | --- |
| Public positioning | Explain what Blueprint is, who it serves, and what is included | `README.md`, `OPEN_SOURCE_SPEC.md` | Yes |
| Product map | Define the complete product shape and missing system pieces | `PRODUCT_MAP.md` | Yes |
| Architecture boundary | Define core, extension, and example layers | `ARCHITECTURE.md` | Yes |
| Bundle manifest | Declare included, planned, and excluded assets | `BUNDLE_MANIFEST.md` | Yes |
| Release packaging | Prepare public release files and manual release gates | `VERSION`, `CHANGELOG.md`, `RELEASE.md`, `VALIDATION_CHECKLIST.md` | Yes |
| Documentation navigation | Route users from README into quickstart, concepts, reference, governance, validation, and community docs | `docs/index.md`, `docs/nav.md`, `docs/quickstart.md` | Yes |
| Documentation quality gates | Validate repository links, manifest paths, public wording, templates, and release consistency | `scripts/check_quality.py`, `.github/workflows/docs-quality.yml` | Yes |
| Validation fixtures | Define versioned UC, RT, and release-readiness expectations for quality gates | `docs/validation/fixtures/**`, `scripts/check_validation_fixtures.py` | Yes |
| Context export | Export ordered repository-owned Markdown and JSONL context bundles for agents, databases, and review tools | `context/export-manifest.json`, `scripts/export_context.py` | Yes |
| Open-source support | Define public support, conduct, and security boundaries | `SUPPORT.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` | Yes |
| GitHub contribution templates | Structure public issues and PRs | `.github/**` | Yes |
| Agent entrypoint | Define how agents start and recover | `core/AGENTS.md` | Yes |
| Task router | Classify work before implementation | `core/TASK_PROCESS_ROUTER.md` | Yes |
| Process levels | Scale required procedure to task size | `core/TASK_PROCESS_ROUTER.md` | Yes |
| Feature lifecycle | Move meaningful work from request to implementation safely | `core/FEATURE_LIFECYCLE_STANDARD.md` | Yes |
| PR handoff and clean start | Keep PRs reviewable and end old chat dependency after merge | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | Yes |
| Security baseline | Define portable security expectations | `core/SECURITY.md` | Yes |
| Governance authority | Map every rule to one owner | `governance/docs/governance-index.md` | Yes |
| Branch governance | Keep branches aligned with scope and release flow | `governance/docs/git-policy.md` | Yes |
| PR lifecycle | Define PR title, body, scope, review, and merge rules | `governance/docs/pr-standard.md` | Yes |
| Verification | Define validation language and evidence levels | `governance/docs/verification-standard.md` | Yes |
| Documentation truthfulness | Prevent planned work from being described as implemented | `governance/docs/documentation-standard.md` | Yes |
| ADR process | Capture durable architecture decisions | `governance/docs/adr-policy.md` | Yes |
| Project Memory | Store compact durable recovery state | `memory/project-kb/**` | Yes |
| Recovery templates | Provide reusable recovery artifacts | `templates/recovery/**` | Yes |
| Project Memory templates | Provide reusable memory files for adopters | `templates/project-memory/**` | Yes |
| Feature lifecycle templates | Provide reusable `FEATURE`, `CLARIFICATION`, `PLAN`, and `TASKS` artifacts | `templates/feature-lifecycle/**` | Yes |
| PR handoff templates | Provide reusable PR handoff and memory-update artifacts | `templates/pr-handoff/**` | Yes |
| Guardian templates | Provide reusable Guardian review artifacts | `templates/guardian/**` | Yes |
| Checklists | Provide installation, recovery, branch, PR, and clean-start acceptance criteria | `checklists/**` | Yes |
| Examples | Show sanitized adoption patterns | `examples/**` | First example included |
| Optional extensions | Provide future automation outside core | Extension repositories or future extension layer | Not core |

## Process Levels

Blueprint uses process levels to avoid unnecessary ceremony.

| Level | Meaning | Required procedure | Skipped by default | Owner |
| --- | --- | --- | --- | --- |
| L0 | Trivial task | Repository identity when editing, scope check, `git diff --check` when files changed | Feature Lifecycle, full Guardian, architecture review, migration matrix | `core/TASK_PROCESS_ROUTER.md` |
| L1 | Documentation or small scoped change | Owner lookup, source-of-truth check, compact docs validation | Feature Lifecycle, full Guardian, release validation unless escalation triggers apply | `core/TASK_PROCESS_ROUTER.md` |
| L2 | Scoped layer change | Layer owner, allowed paths, boundary checks, relevant validation | Full release gates unless release work | `core/TASK_PROCESS_ROUTER.md` |
| L3 | Meaningful feature implementation | Feature Lifecycle, Guardian validation, PR handoff | None of the feature planning gates | `core/FEATURE_LIFECYCLE_STANDARD.md` |
| L4 | Architecture, migration, release, or merge | Full Guardian, source-of-truth analysis, memory and release gates | No major process gates | `core/TASK_PROCESS_ROUTER.md` |

Rule:

```text
Do not apply L4 procedure to L0 or L1 work.
```

If a small task is being overloaded, downgrade it and explain which rules are skipped.

For L0 and L1 work, use compact mode:

```text
repo identity
-> dirty tree
-> scope check
-> changed files
-> relevant validation
-> risks
-> next step
```

Escalate only when the task changes source-of-truth boundaries, release state, branch state, architecture, migration, versioned public assets, implementation claims, runtime, code, dependencies, or multiple operating layers.

If a task is unclear, risky, cross-layer, or changes public claims, classify it higher and decompose it.

## Project Management Model

Blueprint manages project state through Project Memory.

Project Memory is not a transcript. It is compact repository-owned recovery state.

### Memory Levels

| Level | Purpose | Typical owner path | When to create |
| --- | --- | --- | --- |
| Project Memory | Repository identity, current status, rules, recovery, references | `memory/project-kb/**` | Always for full installation |
| Domain Memory | Durable state for a product or business domain | `memory/project-kb/domains/<domain>/` in adopter repositories | When a domain becomes too large for root memory |
| Module Memory | Durable state for a major module inside a domain | `memory/project-kb/domains/<domain>/modules/<module>/` | When a module has its own implementation reality |
| Subsystem Memory | Durable state for specialized internals | `memory/project-kb/domains/<domain>/modules/<module>/subsystems/<subsystem>/` | When subsystem details would overload module memory |
| Feature Memory | Planning and execution artifacts for meaningful feature work | `memory/project-kb/features/<feature>/` | When Feature Lifecycle is required |

Root Project Memory stays compact and points to owners.

Detailed knowledge moves down to the lowest stable owner that can preserve recovery without overloading root memory.

### Root Memory Files

| File | What it stores | Long-term role |
| --- | --- | --- |
| `00_INDEX.md` | Recovery entrypoint and memory navigation | Active recovery index |
| `01_PROJECT_CONTEXT.md` | Project identity, audience, current direction | Template included |
| `02_PROJECT_MAP.md` | Product or repository area map | Template included |
| `03_SYSTEM_ARCHITECTURE.md` | Architecture summary and owner map | Template included |
| `04_DOMAIN_MODEL.md` | Shared vocabulary and domain boundaries | Template included |
| `05_IMPLEMENTATION_STATUS.md` | What is included, planned, excluded, released, or deprecated | Active status owner |
| `06_WORKFLOW_AND_RULES.md` | Workflow summary and recovery-relevant rules | Active memory summary |
| `07_DECISIONS_LOG.md` | Accepted decisions and consequences | Active decision memory |
| `08_CURRENT_STATE.md` | Current recovery point and next recommended work | Active state owner |
| `09_TASK_HISTORY.md` | Durable task history after meaningful work | Active history owner |
| `10_REFERENCE.md` | Canonical navigation map | Active reference owner |
| `current/CLEAN_START_BRIEF.md` | Short transition brief for the next session | Temporary recovery aid |

Templates for `01` through `10` are included in `templates/project-memory/**`.

## Feature Management Model

Blueprint feature management is modeled after a specification-first workflow, but it is broader than feature delivery.

It exists to prevent implementation from starting before scope, ownership, validation, and handoff are clear.

### Feature Lifecycle Flow

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

### Required Feature Artifacts

When Feature Lifecycle is required, the feature owns:

```text
memory/project-kb/features/<feature-name>/
  FEATURE.md
  CLARIFICATION.md
  PLAN.md
  TASKS.md
```

| Artifact | Purpose | Must contain |
| --- | --- | --- |
| `FEATURE.md` | Define what must be built and why it matters | user scenarios, user stories, edge cases, functional requirements, entities, success criteria, assumptions |
| `CLARIFICATION.md` | Record questions, answers, decisions, and reasons before planning | question, decision, reason, open-question status |
| `PLAN.md` | Define how the feature will be built | summary, technical context, governance check, research, data or document model, validation strategy |
| `TASKS.md` | Break implementation into small reviewable work | phases, tasks, dependencies, validation, explicit exclusions |

Feature artifacts are required for meaningful features, new public surfaces, new installable bundles, large refactors, migrations, or cross-layer workflow changes.

Feature artifacts are not required for typos, broken links, small formatting corrections, mechanical reference updates, or small scoped documentation edits.

### Feature Artifacts Are Not Final Truth

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

If feature docs say one thing and implementation evidence says another, implementation status and owner documents must be updated first.

## Recovery Model

A new session should recover without old chat history.

Standard recovery reads:

```text
core/AGENTS.md
-> memory/project-kb/00_INDEX.md
-> memory/project-kb/08_CURRENT_STATE.md
-> memory/project-kb/05_IMPLEMENTATION_STATUS.md
-> memory/project-kb/10_REFERENCE.md
-> core/TASK_PROCESS_ROUTER.md
```

For product-shape work, also read:

```text
PRODUCT_MAP.md
-> memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md
-> memory/project-kb/12_SYSTEM_RELATIONSHIP_MAP.md
```

For feature work, also read:

```text
core/FEATURE_LIFECYCLE_STANDARD.md
-> memory/project-kb/features/<feature-name>/
```

Recovery succeeds only when the repository contains enough current state to continue.

## Guardian Model

Guardian is a process control layer.

It is not a service, CI replacement, or separate agent runtime.

Guardian checks:

- repository identity;
- branch and HEAD;
- dirty worktree;
- allowed scope;
- forbidden paths;
- architecture boundaries;
- documentation truthfulness;
- source-of-truth conflicts;
- memory update need;
- PR handoff readiness;
- clean-start readiness;
- validation evidence.

Guardian work must scale by process level. L0 and L1 do not require the same depth as L3 and L4.

## Installation Shapes

Blueprint supports two installation shapes.

### Minimal Installation

Minimal installation gives a repository:

- agent entrypoint;
- task routing;
- PR and branch policy;
- validation reporting;
- recovery path;
- current state;
- implementation status;
- reference map;
- Guardian checks.

Minimum owner set:

```text
AGENTS.md
TASK_PROCESS_ROUTER.md
PR_HANDOFF_AND_CLEAN_START_STANDARD.md
docs/governance-index.md
docs/git-policy.md
docs/pr-standard.md
docs/verification-standard.md
project-kb/00_INDEX.md
project-kb/05_IMPLEMENTATION_STATUS.md
project-kb/08_CURRENT_STATE.md
project-kb/10_REFERENCE.md
project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md
```

### Full Installation

Full installation adds:

- feature lifecycle;
- full governance standards;
- Project Memory templates;
- decisions log;
- task history;
- clean start;
- Guardian validation scenarios;
- documentation lifecycle;
- ADR process;
- security baseline.

Full installation is covered by the included owner documents, templates, Guardian assets, and checklists.

Public release packaging is covered by release docs, validation checklist, support, security, conduct, and GitHub contribution templates.

The v0.4.0 release PR into `main` has landed. Future releases remain separate approval-gated PRs.

## Completion Gates Before Future Public Packaging

Do not treat future release scopes as complete until:

1. `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` has no unresolved `Partial` or `Planned` system items unless they are explicitly excluded.
2. Example scope exists or is explicitly deferred from the release scope.
3. Public docs distinguish included, planned, excluded, and released states.
4. Local validation, link checks, wording scans, and contribution hygiene checks pass.
5. Release docs, changelog, version, support, security, and conduct files agree.

## Next Build Order

Build the remaining system in this order:

1. Select each next release scope through `core/TASK_PROCESS_ROUTER.md`.
2. Add additional examples only if selected for a later release scope.
3. Add release automation only after the manual release process repeats enough to automate safely.
4. Prepare release PRs into `main` only after the selected scope is validated.

This order protects the system from losing core logic while converting source-reference behavior into portable open-source artifacts.
