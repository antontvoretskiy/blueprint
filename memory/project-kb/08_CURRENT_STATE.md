# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Bootstrap presentation only until a release PR lands |
| `develop` | Integration branch | Contains bootstrap, core contracts, and governance standards |

## Current Work

Project Memory structure is being added on a feature branch from `develop`.

## Current Included Layers

- public repository presentation;
- local preview environment;
- core contracts;
- governance standards;
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

After Project Memory structure is reviewed and merged into `develop`, add recovery and Guardian templates in a separate PR.

Do not move `develop` to `main` until a release PR is explicitly prepared.
