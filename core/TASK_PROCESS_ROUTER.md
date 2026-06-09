# Blueprint Task Process Router

This router classifies work before implementation starts.

Its purpose is to keep tasks scoped, route them to the right owner documents, and prevent a single PR from mixing unrelated operating layers.

## Routing Inputs

Before choosing a route, identify:

- user intent;
- repository and branch;
- requested paths;
- affected operating layer;
- whether the task is read-only;
- whether implementation is allowed;
- validation requirements;
- explicit exclusions.

## Task Classes

| Task class | Description | Default action |
| --- | --- | --- |
| Answer-only | The user asks a question and does not request changes | Answer with file or command evidence when useful |
| Audit-only | The user asks for review, plan, or assessment without changes | Inspect, report findings, do not edit files |
| Bootstrap docs | Root presentation, scope, architecture, manifest, contribution rules | Update root docs and public validation surface |
| Core contract | Portable agent, routing, lifecycle, handoff, or security rules | Update `core/**` and any truthful root status docs |
| Governance standard | Branch, PR, verification, documentation, ADR, or authority-map rules | Use `governance/**` after that layer exists |
| Project Memory | Current state, decisions, task history, recovery points | Use `memory/**` after that layer exists |
| Template bundle | Reusable installable artifacts | Use `templates/**` after templates are approved |
| Example project | Sanitized adoption example | Use `examples/**` after examples are approved |
| Checklist | Installation, recovery, branch, PR, or clean-start checklist | Use `checklists/**` after checklists are approved |
| Release | Version bump, manifest, release notes, release PR | Follow SemVer and release PR standards |

If a task spans multiple classes, split it unless the maintainer explicitly approves a combined PR.

## Work Size Levels

| Level | Meaning | Required process |
| --- | --- | --- |
| L0 | Tiny typo, link, or formatting fix | Direct edit and validation |
| L1 | Small scoped documentation change | Short plan, edit, validation |
| L2 | New document or operating rule | Audit, owner check, edit, validation, PR handoff |
| L3 | Cross-layer framework change | Split into smaller PRs unless explicitly approved |

## Start Conditions

Implementation may start only when:

- repository identity is confirmed;
- branch strategy is clear;
- scope is explicit;
- forbidden paths are known;
- source references are read-only;
- relevant owner documents are identified.

If any condition is unclear and the risk is material, stop and ask for clarification.

## Branch Routing

Default Blueprint development flow:

```text
main
  -> develop
  -> docs/<scope> or fix/<scope>
  -> PR into develop
  -> release PR into main
```

Use `main` for release-ready public state. Use `develop` for integration work before release.

Do not create branches in a reference repository.

## Path Routing

| Requested work | Allowed paths |
| --- | --- |
| Public positioning | `README.md`, `OPEN_SOURCE_SPEC.md`, `ARCHITECTURE.md`, `BUNDLE_MANIFEST.md`, `CONTRIBUTING.md`, `docs/benchmarks/**`, `media/**`, `public/**` |
| Core contracts | `core/**`, plus minimal root status updates |
| Governance standards | `governance/**`, plus minimal root status updates |
| Project Memory | `memory/**`, plus minimal root status updates |
| Templates | `templates/**`, plus manifest and docs updates |
| Examples | `examples/**`, plus manifest and docs updates |
| Checklists | `checklists/**`, plus manifest and docs updates |

Minimal root status updates are allowed when they keep README, architecture, or manifest claims truthful.

## Stop Conditions

Stop before implementation when:

- the user requested audit-only work;
- the requested branch or repository does not match the task;
- the task would modify a read-only reference repository;
- the task requires forbidden product-specific content;
- the task would add runtime, generator, automation, or integration support without approval;
- validation cannot be run and no honest fallback is available.

## Output Requirements

Every completed implementation should report:

- branch;
- base branch;
- files changed;
- validation results;
- PR link when a PR is created;
- risks;
- next step.
