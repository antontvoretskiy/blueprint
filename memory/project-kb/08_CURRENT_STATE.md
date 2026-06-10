# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Contains the released v0.3.0 public framework bundle |
| `develop` | Integration branch | Contains the validated v0.3.0 integration state and is the base for the next scoped work |

## Current Work

Blueprint v0.3.0 has been released from `develop` to `main`.

Current work is post-release recovery validation on `docs/dogfood-recovery-validation`. The goal is to prove that a fresh session can recover from repository files after release, without depending on old chat history.

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

Complete the post-release recovery validation PR into `develop`.

After that, select the next v0.4.0 scope through the task router before creating new templates, examples, automation, CLI, or integration work.
