# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Bootstrap presentation only until a release PR lands |
| `develop` | Integration branch | Contains bootstrap, complete product map, core contracts, governance standards, self-hosting, Project Memory structure, Project Memory templates, Feature Lifecycle templates, PR handoff templates, Guardian templates, checklists, recovery templates, source coverage maps, and the AI product example |

## Current Work

The complete product map, source coverage matrix, relationship map, and first sanitized example are the current control layer for Blueprint.

Next work should prepare release packaging or add explicitly selected additional examples.

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
- AI product example.

## Not Yet Included

- additional examples;
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

Use `PRODUCT_MAP.md` and the coverage matrix to prepare release packaging, or add additional examples only if they are selected for the release scope.

Do not move `develop` to `main` until a release PR is explicitly prepared.
