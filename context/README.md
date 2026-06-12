# Blueprint Context Export

Asset: context-export
Version: v0.10.0
Type: Local Command Workflow
Author: Blueprint Maintainers
Status: Release target

Context export creates ordered Markdown bundles from repository-owned source of
truth files.

Use it when you need to give Codex, Cursor, a database, a review tool, or
another LLM the current Blueprint context without depending on old chat history.

## Commands

Export the database/RAG ingest context bundle:

```bash
make context-export
```

Default output:

```text
.blueprint/context/blueprint-database-ingest.md
```

Export the Codex chat bootstrap bundle:

```bash
make context-chat
```

Default output:

```text
.blueprint/context/blueprint-codex-context.md
```

Export explicit profiles:

```bash
make context-codex
make context-cursor
make context-database
```

Validate the manifest without writing bundles:

```bash
python3 scripts/export_context.py check
```

## Profiles

| Profile | Purpose |
| --- | --- |
| `codex` | Fresh Codex chat context for recovery, current state, active scope, rules, and validation |
| `cursor` | Fresh Cursor chat context for recovery, current state, active scope, implementation boundaries, and docs navigation |
| `database-ingest` | Broader Markdown corpus for database, RAG, retrieval, audit, or external review ingestion |

## Why These Documents

Each exported document must answer at least one recovery or ingestion question:

| Question | Documents that answer it |
| --- | --- |
| What is this project? | `README.md`, `PRODUCT_MAP.md`, `OPEN_SOURCE_SPEC.md` |
| Where is the source of truth? | `memory/project-kb/00_INDEX.md`, `memory/project-kb/10_REFERENCE.md`, `context/export-manifest.json` |
| What is the current state? | `memory/project-kb/current/CLEAN_START_BRIEF.md`, `memory/project-kb/08_CURRENT_STATE.md`, `memory/project-kb/05_IMPLEMENTATION_STATUS.md` |
| What rules must an agent follow? | `core/AGENTS.md`, `core/TASK_PROCESS_ROUTER.md`, governance standards |
| What work is active or recently changed? | feature artifacts, task history, decisions log |
| How should changes be validated? | `VALIDATION_CHECKLIST.md`, `RELEASE.md`, `governance/docs/verification-standard.md` |

The Codex and Cursor profiles stay narrow so a new chat starts with the files
needed to recover and work safely. The database-ingest profile is broader
because retrieval systems need history, decisions, architecture, and coverage
documents to answer later questions.

## Source Of Truth

The export order is owned by:

```text
context/export-manifest.json
```

Generated bundles are artifacts. They are not source of truth and are ignored by
Git under:

```text
.blueprint/context/
```

## Boundaries

This workflow does not:

- start Codex, Cursor, or another editor;
- call external services;
- install Blueprint into another repository;
- create a packaged CLI;
- create JSONL output;
- create ZIP bundles;
- add runtime behavior;
- replace Project Memory, release validation, or PR review.
