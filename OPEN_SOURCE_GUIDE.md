# Blueprint Open Source Guide

Blueprint is a public operating framework for AI-native software development.

This guide explains how the repository should present itself to external users and contributors.

## Public Promise

Blueprint helps a repository keep governance, Project Memory, task routing, recovery, Guardian checks, branch governance, Feature Lifecycle, PR Lifecycle, and clean start in versioned files.

It does not provide product implementation, runtime integrations, application scaffolding, or automation in the current bundle.

## Public Entry Points

| Entry point | Purpose |
| --- | --- |
| `README.md` | First public landing page |
| `OPEN_SOURCE_SPEC.md` | Product definition and boundaries |
| `PRODUCT_MAP.md` | Complete framework shape and subsystem map |
| `ARCHITECTURE.md` | Core, extension, and example layer model |
| `BUNDLE_MANIFEST.md` | Included, planned, and excluded assets |
| `ADAPTATION_GUIDE.md` | How an adopter applies Blueprint |
| `MIGRATION_GUIDE.md` | How to migrate from an existing internal system |
| `VALIDATION_CHECKLIST.md` | Manual release and adoption checks |
| `CONTRIBUTING.md` | Contribution rules |
| `SUPPORT.md` | Support boundaries and channels |
| `SECURITY.md` | Public security reporting guidance |

## Public Status Language

Use these labels consistently:

| Label | Meaning |
| --- | --- |
| Included | File or layer exists in the repository |
| Planned | File or layer is intentionally not included yet |
| Example | Educational artifact, not a rule owner |
| Template | Reusable artifact for adopters |
| Excluded | Intentionally outside Blueprint core |

Do not describe planned, example, or template content as implemented product behavior.

## Public Quality Rules

Public-facing changes must:

- keep README and manifest truthful;
- preserve one owner per rule;
- use SemVer for versioned public assets;
- keep PR and commit titles reviewable;
- include validation evidence;
- avoid private product names, private release history, and private PR timelines;
- avoid noisy generated-change wording;
- avoid claiming automation or integrations that do not exist.

## What To Read First

New users should read:

1. `README.md`
2. `OPEN_SOURCE_SPEC.md`
3. `ADAPTATION_GUIDE.md`
4. `BUNDLE_MANIFEST.md`
5. `examples/ai-product/README.md`

Maintainers should also read:

1. `PRODUCT_MAP.md`
2. `governance/docs/governance-index.md`
3. `memory/project-kb/08_CURRENT_STATE.md`
4. `RELEASE.md`
5. `VALIDATION_CHECKLIST.md`
