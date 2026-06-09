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

## Planned Governance Documents

| Path | Purpose |
| --- | --- |
| `governance/docs/governance-index.md` | Authority map for rules |
| `governance/docs/engineering-governance.md` | Engineering operating model |
| `governance/docs/git-policy.md` | Branch and merge policy |
| `governance/docs/pr-standard.md` | PR lifecycle standard |
| `governance/docs/verification-standard.md` | Validation truthfulness standard |
| `governance/docs/documentation-standard.md` | Documentation governance |
| `governance/docs/adr-policy.md` | Architecture decision record policy |

These files are planned. They are not part of the bootstrap PR.

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
