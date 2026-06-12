# Blueprint Context Export

Asset: context-export
Version: v0.9.0
Type: Local Command Workflow
Author: Blueprint Maintainers
Status: Release target

Context export creates ordered Markdown bundles from repository-owned source of
truth files.

Use it when you need to give another LLM, database, review tool, Codex chat, or
Cursor chat the current Blueprint context without depending on old chat history.

## Commands

Export the full external LLM context bundle:

```bash
make context-export
```

Default output:

```text
.blueprint/context/blueprint-context-bundle.md
```

Export the chat bootstrap bundle:

```bash
make context-chat
```

Default output:

```text
.blueprint/context/blueprint-chat-bootstrap.md
```

Validate the manifest without writing bundles:

```bash
python3 scripts/export_context.py check
```

## Profiles

| Profile | Purpose |
| --- | --- |
| `external-llm` | Full repository-owned context for an outside LLM, database, or review tool |
| `chat-bootstrap` | Fresh-chat context for Codex, Cursor, or another coding agent |

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
- add runtime behavior;
- replace Project Memory, release validation, or PR review.
