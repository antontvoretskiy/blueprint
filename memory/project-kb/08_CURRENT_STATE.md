# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Contains the released v0.7.0 public framework bundle after publication |
| local/private integration branches | Maintainer-only work | May exist outside the public GitHub branch list |

## Current Work

Blueprint v0.7.0 is the current prepared release state.

The previous GitHub Release `v0.6.1` was published from public `main`.
Publishing a GitHub Release or tag for `v0.7.0` remains a separate
approval-gated step.

The public GitHub repository exposes only `main` as the release-ready
distribution branch. The former public `develop` branch and merged release,
sync, and docs branches were removed after maintainer approval.

Local or private integration branches may still be used by maintainers before
publication, but they are not part of the public distribution contract.

Release `v0.5.1` publishes documentation alignment for the public branch model:

- clarify public main-only release distribution;
- clarify local/private maintainer integration branches;
- add explicit adoption copy maps;
- align governance, release, router, and memory documents with the public branch model.

Release `v0.6.1` keeps documentation quality gates on public `main` while
removing the Dependabot configuration that created extra public maintenance
branches.

Release `v0.7.0` adds the documentation navigation layer:

- `docs/index.md`;
- `docs/nav.md`;
- `docs/quickstart.md`;
- `docs/concepts/repository-first.md`;
- `docs/reference/templates.md`;
- `docs/reference/governance.md`;
- `docs/community.md`.

The active quality-gate surface is:

- `make quality`;
- `scripts/check_quality.py`;
- `.github/workflows/docs-quality.yml`;

These checks are validation tooling only. They are not a CLI, installer,
runtime, workflow engine, or code generator.

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
- v0.5.1 public README, branch model alignment, adoption copy map, and practical AI-agent use-case media in
  `main`.
- v0.6.1 documentation quality workflow and scripts.
- v0.7.0 documentation navigation, quickstart, concept, reference, and community pages.

## Not Yet Included

- additional examples;
- release automation;
- CLI;
- installer;
- MCP integration;
- runtime;
- agent runtime;
- workflow engine;
- code generator.

## Next Recommended Work

Select the next release scope after v0.7.0.

Do not start additional examples, validation fixtures, CLI, installer, release
automation, or integration work until the next scope is selected.
