# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Contains the released v0.4.1 public framework bundle |
| `develop` | Integration branch | Base branch for the next scoped framework work |

## Current Work

Blueprint v0.4.1 has been released from validated `develop` state to `main`.

Post-release recovery validation has landed in `develop`.

The system use-case validation suite has landed in `develop`.

System use-case validation passed for the v0.4.0 release baseline.

After v0.4.0, UC-03 process-level routing evidence was found too weak because
it checked that L0-L4 rules existed, not that realistic tasks selected the
right level. The v0.4.1 validation hardening adds process-level regression
scenarios.

The first v0.4.1 process-level regression pass is recorded in
`memory/project-kb/current/SYSTEM_USE_CASE_VALIDATION.md`.

Post-validation branch cleanup is complete. The merged docs branches were removed locally and remotely, and the durable branch baseline is `main` plus `develop`.

PR #30 merged the process-level regression hardening into `develop`.

PR #32 merged context and recovery budgets into `develop` so L0/L1 work limits
both response size and recovery-document loading.

PR #36 merged the v0.4.1 process-efficiency dogfood audit into `develop`.
The audit validates that simple L0/L1 docs-only and status tasks can stay
compact without full recovery reloads.

Post-dogfood branch cleanup is complete for the merged PR #36 branch.

Current work is next-scope selection for the release after v0.4.1.

## Current Included Layers

- public repository presentation;
- local preview environment;
- complete product map;
- core contracts;
- governance standards;
- self-hosting governance;
- Project Memory structure;
- Project Memory templates;
- Feature Lifecycle templates;
- PR handoff templates;
- Guardian templates;
- checklists;
- recovery templates;
- source coverage matrix;
- system relationship map;
- system use-case validation suite;
- system use-case validation result;
- AI product example;
- public release packaging;
- support, security, and conduct files;
- GitHub contribution templates.

## Not Yet Included

- additional examples;
- automation;
- CLI;
- installer;
- MCP integration;
- runtime;
- agent runtime;
- workflow engine;
- code generator.

## Next Recommended Work

Select the next release scope through `core/TASK_PROCESS_ROUTER.md`.

Do not start new public assets until the next scope is classified and approved.
