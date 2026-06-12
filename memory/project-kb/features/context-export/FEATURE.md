# Context Export Feature

Feature: context-export
Version: v0.9.0
Status: Release target
Owner: Blueprint Maintainers

## User Scenarios

1. A maintainer wants to export the repository-owned truth for an external LLM,
   database, or review tool without manually collecting files.
2. A maintainer wants to start a new Codex or Cursor chat with the correct
   recovery context in the correct order.
3. A reviewer wants to verify that the exported context references existing
   repository files and does not depend on old chat history.

## User Stories

### P1

- As a maintainer, I can run one command to produce an ordered context bundle
  containing the canonical Blueprint documents.
- As a maintainer, I can run one command to produce a chat bootstrap bundle for
  Codex or Cursor.

### P2

- As a reviewer, I can inspect the manifest that defines export order and file
  membership.
- As a maintainer, I can validate the manifest and export commands through the
  existing quality gate.

### P3

- As an adopter, I can copy the pattern into another repository and adapt the
  manifest to that repository's own source-of-truth files.

## Edge Cases

- A manifest path is missing.
- A manifest profile has no documents.
- A document appears more than once in the same generated bundle.
- The generated output directory does not exist.
- A requested profile is unknown.
- A future repository has local/private files that must not be exported.

## Functional Requirements

- FR-001: The repository must define an ordered context export manifest.
- FR-002: The manifest must support at least `external-llm` and
  `chat-bootstrap` profiles.
- FR-003: The repository must provide a command that exports the external LLM
  context bundle.
- FR-004: The repository must provide a command that exports the chat bootstrap
  context bundle.
- FR-005: The export command must include file contents in manifest order.
- FR-006: The export command must validate that referenced files exist.
- FR-007: The export command must write generated bundles outside tracked
  source files by default.
- FR-008: The existing quality gate must validate the export manifest.
- FR-009: The feature must not start Codex, Cursor, or any external application.
- FR-010: The feature must not add a packaged CLI, installer, runtime, or
  external service integration.

## Key Entities

| Entity | Meaning |
| --- | --- |
| Context manifest | Ordered file list and profiles for context export |
| Context bundle | Markdown file containing repository-owned truth for external tools |
| Chat bootstrap bundle | Markdown file optimized for a fresh Codex or Cursor chat |
| Profile | Named subset of manifest documents |

## Success Criteria

- SC-001: `make context-export` produces a Markdown bundle in the default output
  directory.
- SC-002: `make context-chat` produces a Markdown chat bootstrap bundle.
- SC-003: `make quality` validates the context manifest and export script.
- SC-004: Generated bundles are ignored by Git.
- SC-005: Documentation tells maintainers which commands to run and what is not
  automated.

## Assumptions

- The repository remains the source of truth.
- Generated context bundles are artifacts, not canonical state.
- New-chat startup is represented as a generated bootstrap document because
  Codex and Cursor do not share one portable command for opening a new chat with
  local repository context.
