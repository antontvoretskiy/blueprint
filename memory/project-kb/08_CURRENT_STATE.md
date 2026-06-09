# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Bootstrap presentation only until a release PR lands |
| `develop` | Integration branch | Contains bootstrap, core contracts, governance standards, self-hosting, Project Memory structure, and recovery templates |

## Current Work

Recovery templates are the current reusable template layer for Blueprint.

Next work should add Guardian templates in a separate scoped PR.

## Current Included Layers

- public repository presentation;
- local preview environment;
- core contracts;
- governance standards;
- self-hosting governance;
- Project Memory structure;
- recovery templates.

## Not Yet Included

- Guardian templates;
- checklists;
- examples;
- release PR into `main`;
- automation;
- CLI;
- installer;
- MCP integration;
- runtime;
- agent runtime;
- workflow engine;
- code generator.

## Next Recommended Work

Add Guardian templates in a separate scoped PR.

Do not move `develop` to `main` until a release PR is explicitly prepared.
