# Blueprint Current State

This file records the current recovery point for Blueprint.

## Repository State

| Branch | Role | Current meaning |
| --- | --- | --- |
| `main` | Release-ready public state | Contains the released v0.11.1 public framework bundle |
| local/private integration branches | Maintainer-only work | May exist outside the public GitHub branch list |

## Current Work

Blueprint v0.11.1 is released on public `main`.

The GitHub Release `v0.11.1` is published and points to the v0.11.1 release
commit on `main`.

The next release target is v0.12.0 for ZIP context export bundles.

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

Release `v0.8.0` adds the validation fixture layer:

- `docs/validation/fixtures/README.md`;
- `docs/validation/fixtures/system-use-cases.json`;
- `docs/validation/fixtures/process-level-regression.json`;
- `docs/validation/fixtures/release-readiness.json`;
- `scripts/check_validation_fixtures.py`.

Release `v0.9.0` adds the context export layer:

- `context/README.md`;
- `context/export-manifest.json`;
- `scripts/export_context.py`;
- `make context-export`;
- `make context-chat`;
- ignored generated output under `.blueprint/context/`.

Release `v0.10.0` extends context export with explicit profiles:

- `codex`;
- `cursor`;
- `database-ingest`;
- `make context-codex`;
- `make context-cursor`;
- `make context-database`.

Release `v0.11.0` extends context export with JSONL output:

- `default_jsonl_outputs` in `context/export-manifest.json`;
- `python3 scripts/export_context.py jsonl`;
- `make context-jsonl`;
- one JSON object per source document for database/RAG ingestion.

Release `v0.11.1` aligns release-state truthfulness after publication:

- README current release state;
- `RELEASE.md` last released and next target state;
- Project Memory current-state and validation state;
- stronger release consistency checks in `scripts/check_quality.py`.

The active quality-gate surface is:

- `make quality`;
- `scripts/check_quality.py`;
- `scripts/check_validation_fixtures.py`;
- `scripts/export_context.py`;
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
- validation fixtures;
- context export commands;
- profile-specific context export commands;
- JSONL context export command;
- AI product example;
- public release packaging;
- support, security, and conduct files;
- GitHub contribution templates;
- v0.5.1 public README, branch model alignment, adoption copy map, and practical AI-agent use-case media in
  `main`.
- v0.6.1 documentation quality workflow and scripts.
- v0.7.0 documentation navigation, quickstart, concept, reference, and community pages.
- v0.8.0 validation fixtures, fixture checker, and main-only validation state refresh.
- v0.9.0 context export commands for external LLMs and fresh chats.
- v0.10.0 profile-specific context exports.
- v0.11.0 JSONL context export.
- v0.11.1 release-state truthfulness and stronger release consistency checks.

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

Validate and publish the v0.12.0 ZIP context export bundle scope.

Required validation before any new release publication:

- `make quality`;
- `make doctor`;
- `make config`;
- `make smoke`;
- `git diff --check`;
- Python compile checks for validation scripts;
- `make context-export`;
- `make context-chat`;
- `make context-codex`;
- `make context-cursor`;
- `make context-database`;
- `make context-jsonl`;
- public branch and open PR checks.

Do not start additional examples, CLI, installer, release automation, or
integration work until the v0.12.0 scope is selected and validated.
