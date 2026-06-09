# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Bootstrap presentation only until a release PR lands |
| `develop` | Integration branch | Contains bootstrap, core contracts, governance standards, self-hosting, Project Memory structure, recovery templates, and source coverage maps |

## Current Work

Source coverage and relationship mapping are the current control layer for Blueprint.

Next work should close the remaining coverage gaps before public packaging.

## Current Included Layers

- public repository presentation;
- local preview environment;
- core contracts;
- governance standards;
- self-hosting governance;
- Project Memory structure;
- recovery templates;
- source coverage matrix;
- system relationship map.

## Not Yet Included

- Guardian templates;
- Project Memory templates;
- feature lifecycle templates;
- PR handoff templates;
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

Add missing Project Memory templates, feature lifecycle templates, PR handoff templates, and Guardian templates in separate scoped PRs.

Do not move `develop` to `main` until a release PR is explicitly prepared.
