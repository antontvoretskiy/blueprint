# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Contains the released v0.3.0 public framework bundle |
| `develop` | Integration branch | Contains unreleased v0.4.0 validation work and is the base for the next scoped work |

## Current Work

Blueprint v0.3.0 has been released from `develop` to `main`.

Post-release recovery validation has landed in `develop`.

The system use-case validation suite has landed in `develop`.

System use-case validation has passed on `develop`.

Post-validation branch cleanup is complete. The merged docs branches were removed locally and remotely, and the durable branch baseline is `main` plus `develop`.

Current work is v0.4.0 scope selection or release packaging preparation.

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

Select the next v0.4.0 scope through `core/TASK_PROCESS_ROUTER.md`, or prepare release packaging if maintainers decide the validated `develop` state is ready for `main`.

Do not start new public assets until the next scope is classified and approved.
