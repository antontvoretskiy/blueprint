# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Contains the released v0.5.0 public framework bundle |
| local/private integration branches | Maintainer-only work | May exist outside the public GitHub branch list |

## Current Work

Blueprint v0.5.0 is released on public `main`.

The GitHub Release `v0.5.0` is published and points to the v0.5.0 release
commit on `main`.

The public GitHub repository exposes only `main` as the release-ready
distribution branch. The former public `develop` branch and merged release,
sync, and docs branches were removed after maintainer approval.

Local or private integration branches may still be used by maintainers before
publication, but they are not part of the public distribution contract.

Current scoped work is v0.5.1 documentation alignment:

- clarify public main-only release distribution;
- clarify local/private maintainer integration branches;
- add explicit adoption copy maps;
- align governance, release, router, and memory documents with the public branch model.

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
- GitHub contribution templates;
- v0.5.0 public README and practical AI-agent use-case media in
  `main`.

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

Complete the v0.5.1 docs-only alignment, validate it from a fresh clone, then
publish it to public `main` only after maintainer approval.

Do not start additional examples, automation, CLI, installer, or integration
work until the public branch model and adoption path are aligned.
