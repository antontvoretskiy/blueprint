# Blueprint Architecture

Blueprint is an operating framework for AI-native software development.

The architecture is document-first in the bootstrap phase. Blueprint defines repository operating layers before it introduces templates, examples, automation, or tooling.

## Core Boundary

Blueprint core is the portable operating contract.

Core includes:

- governance;
- agent entrypoint;
- task routing;
- Project Memory;
- recovery;
- Guardian checks;
- branch governance;
- feature lifecycle;
- PR lifecycle;
- validation truthfulness;
- documentation boundaries.

Core excludes:

- runtime framework;
- code generator;
- agent runtime;
- workflow engine;
- MCP server;
- SaaS starter kit;
- product framework;
- UI framework;
- product runtime;
- product algorithms;
- product-specific history.

## Layer Model

Blueprint separates the repository into three layers.

| Layer | Purpose | Allowed content |
| --- | --- | --- |
| Core Layer | Defines the portable operating contract | Standards, rules, manifests, checklists, generic templates |
| Extension Layer | Adds optional tooling around the core | CLI, validators, GitHub Actions, MCP integrations, installers |
| Example Layer | Shows how to adapt Blueprint | Sanitized examples, walkthroughs, sample layouts |

Only the Core Layer defines canonical rules. Extensions and examples must not redefine core behavior.

## Operating Components

| Component | Responsibility |
| --- | --- |
| Governance | Rule ownership, source of truth, engineering policy, documentation policy |
| Project Memory | Durable project knowledge, current state, decisions, recovery inputs |
| Recovery | New-chat and handoff continuity from repository state |
| Guardian | Scope, boundary, source-leak, and truthfulness checks |
| Branch Governance | Branch roles, architecture mapping, merge sequencing |
| Feature Lifecycle | Intake, clarification, planning, tasks, implementation, validation |
| PR Lifecycle | PR scope, review readiness, validation evidence, clean start |

## Project Memory Documents

Blueprint Project Memory includes:

| Path | Purpose |
| --- | --- |
| `memory/project-kb/00_INDEX.md` | Memory entrypoint and recovery order |
| `memory/project-kb/05_IMPLEMENTATION_STATUS.md` | Included, planned, and excluded state |
| `memory/project-kb/06_WORKFLOW_AND_RULES.md` | Active workflow summary |
| `memory/project-kb/07_DECISIONS_LOG.md` | Durable accepted decisions |
| `memory/project-kb/08_CURRENT_STATE.md` | Current recovery point |
| `memory/project-kb/09_TASK_HISTORY.md` | Durable task history |
| `memory/project-kb/10_REFERENCE.md` | Canonical reference map |
| `memory/project-kb/current/CLEAN_START_BRIEF.md` | Short current handoff |

## Recovery Templates

Blueprint recovery templates include:

| Path | Purpose |
| --- | --- |
| `templates/recovery/README.md` | Recovery template bundle guide |
| `templates/recovery/RECOVERY_PATH.template.md` | Fresh-session recovery contract |
| `templates/recovery/CLEAN_START_BRIEF.template.md` | Single active clean-start brief format |
| `templates/recovery/RECOVERY_VALIDATION.template.md` | Manual validation that recovery works from repository files |

Recovery templates are reusable assets. They do not replace Project Memory, governance owner documents, PR review, or validation evidence.

## Source of Truth

The repository is the source of truth.

Chat history can help execution, but durable project rules, state, decisions, and validation expectations must live in versioned files.

Each rule should have one canonical owner. Summary files may link to an owner, but they must not redefine the rule.

## Core Documents

Blueprint core includes:

| Path | Purpose |
| --- | --- |
| `core/AGENTS.md` | Agent entrypoint rules |
| `core/TASK_PROCESS_ROUTER.md` | Task routing by operating layer |
| `core/FEATURE_LIFECYCLE_STANDARD.md` | Feature lifecycle standard |
| `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | PR handoff and post-merge clean start |
| `core/SECURITY.md` | Security baseline for agent-driven work |

These files define the portable operating contract. Detailed governance standards, memory templates, examples, checklists, and extensions are separate layers.

## Governance Documents

Blueprint governance includes:

| Path | Purpose |
| --- | --- |
| `governance/docs/governance-index.md` | Authority map for rules |
| `governance/docs/engineering-governance.md` | Engineering operating model |
| `governance/docs/git-policy.md` | Branch and merge policy |
| `governance/docs/pr-standard.md` | PR lifecycle standard |
| `governance/docs/verification-standard.md` | Validation truthfulness standard |
| `governance/docs/documentation-standard.md` | Documentation governance |
| `governance/docs/adr-policy.md` | Architecture decision record policy |

These files define the detailed governance layer. They do not add automation or enforcement tooling.

## Extension Layer

Extensions may be added only after the manual framework is stable.

Allowed future extensions:

- CLI installer;
- validation scripts;
- GitHub Actions;
- MCP integration;
- package publishing;
- docs deployment.

Extension rules:

- extensions must not define new core rules;
- extensions must preserve user modifications;
- extensions must be optional;
- extensions must report validation honestly.

## Example Layer

Examples are educational only.

Allowed future examples:

- AI product;
- SaaS;
- marketplace;
- CRM;
- regulated platform.

Example rules:

- examples must be sanitized;
- examples must not include product code from private projects;
- examples must not become source of truth;
- examples must not be required for installation.

## Non-Goals

Blueprint does not provide:

- product runtime implementation;
- generated application code;
- agent execution runtime;
- workflow execution engine;
- UI components;
- backend framework;
- algorithms;
- domain skills;
- private product memory;
- source-project PR history;
- product migration timeline.

Blueprint can govern repositories that contain these things, but Blueprint core must not contain them.
