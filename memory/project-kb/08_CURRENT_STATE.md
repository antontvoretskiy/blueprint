# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Bootstrap presentation only until a release PR lands |
| `develop` | Integration branch | Contains bootstrap, core contracts, governance standards, self-hosting, and Project Memory structure |

## Current Work

Project Memory structure is the current recovery layer for Blueprint.

Next work should add recovery and Guardian templates in separate scoped PRs.

## Current Included Layers

- public repository presentation;
- local preview environment;
- core contracts;
- governance standards;
- self-hosting governance;
- Project Memory structure.

## Not Yet Included

- recovery templates;
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

Add recovery and Guardian templates in separate scoped PRs.

Do not move `develop` to `main` until a release PR is explicitly prepared.
