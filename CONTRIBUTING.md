# Contributing to Blueprint

Blueprint is an operating framework for AI-native software development. Contributions should improve repository governance, project memory, recovery, lifecycle management, branch governance, Guardian checks, or public open-source usability.

## Contribution Scope

Good contributions include:

- governance rules;
- memory and recovery templates;
- branch and PR lifecycle standards;
- validation and documentation standards;
- Guardian checklists;
- installation and adaptation guidance;
- example repositories that are generic and sanitized.

Out of scope:

- product runtime code;
- domain algorithms;
- product-specific histories;
- private project memory;
- admin UI;
- runtime, stage, admin, or product memory in core;
- generated package tooling before it is explicitly planned;
- examples that leak source-project names, PR numbers, milestones, owners, or incidents.

## Repository-First Rule

Rules that affect future work must live in the repository. Do not rely on chat-only instructions for durable project behavior.

When a contribution introduces or changes an operating rule, update the relevant authority document and any affected index or checklist in the same PR.

## Scope Rules

Use one PR for one operating scope.

Examples:

- Good: "add project memory template bundle"
- Good: "document branch governance standard"
- Good: "add clean-start checklist"
- Bad: "add memory templates, rewrite README, introduce CLI scaffolding, and add examples"

If a change touches multiple operating layers, explain why they must land together.

## Branch Strategy

Blueprint uses `main` for release-ready public state and `develop` for integration work before release.

Default flow:

```text
main
  -> develop
  -> docs/<scope> or fix/<scope>
  -> PR into develop
  -> release PR into main
```

Create feature branches from `develop` unless the maintainer explicitly requests a release or hotfix branch.

Do not create branches in source-reference repositories.

## Commit And PR Title Standard

Use clear, reviewable titles with the format:

```text
type(scope): concise outcome
```

The scope is optional for repository-wide changes.

Examples:

```text
docs: bootstrap blueprint public repository
docs(core): add agent operating contract
docs(governance): add branch and PR standards
docs(memory): add project memory templates
docs(guardian): add guardian review templates
docs(release): prepare blueprint v0.1.0
fix(docs): repair manifest links
```

For versioned public assets, title-style prefixes are allowed:

```text
[Template] Add project memory templates v0.2.0
[Checklist] Add recovery checklist v0.2.0
[Example] Add AI product adoption example v0.3.0
[Release] Prepare Blueprint v0.1.0
```

Commit history should stay compact and meaningful. Prefer one clean commit for one coherent documentation change, or a squash merge title that describes the actual outcome.

Do not use low-signal titles, placeholder titles, vague generated-change wording, or unreviewable work-in-progress labels.

Do not add AI co-author trailers unless the maintainer explicitly asks for them.

## Versioning Standard

Blueprint uses SemVer:

- `v0.1.0`
- `v0.2.0`
- `v0.3.0`

Patch changes are for typo fixes, broken links, formatting fixes, and small documentation corrections that do not change scope.

Minor changes are for new templates, new governance layers, new checklists, new examples, and new install or adaptation guides.

Major changes are for incompatible framework changes after `v1.0.0`.

Before `v1.0.0`:

| Version | Scope |
| --- | --- |
| `v0.1.0` | Public bootstrap, product definition, architecture, manifest |
| `v0.2.0` | Core governance and Project Memory templates |
| `v0.3.0` | Examples, checklists, and public polish |

If a PR changes a public package, preset, template, example bundle, checklist, or release artifact, include the version in the PR title or PR body.

## Pull Request Body Standard

Meaningful PRs should use this structure:

```text
## Problem

## Solution

## Scope

## Validation

## Risks

## Follow-ups
```

If a PR adds or changes a versioned public asset, include this metadata block:

```text
Asset:
Version:
Type:
Author:
Description:
Breaking Changes:
Validation:
```

Use `Breaking Changes: None` when the asset is backward-compatible.

## AI Hygiene Standard

AI assistance is acceptable when the contributor remains accountable for the result.

Do not submit unreviewed generated output. The contributor must check scope, references, validation, wording, and repository boundaries before opening a PR.

PRs and commits must not contain noisy generation disclaimers, placeholder uncertainty, low-signal fix labels, or accidental AI co-author trailers.

## Sanitization Rules

Blueprint must be reusable in any repository.

Before opening a PR, remove or replace:

- private project names;
- domain names;
- product PR numbers;
- product release history;
- stage or milestone names from a source project;
- implementation paths that only exist in one product;
- blockers, incidents, or decisions tied to a private project.

Prefer placeholders such as:

- `<PROJECT_NAME>`
- `<OWNER>/<REPO>`
- `<DOMAIN_A>`
- `<DOMAIN_B>`
- `<PROJECT_SPECIFIC_MODULE>`
- `<PROJECT_SPECIFIC_MILESTONE>`

## Documentation Standard

Documentation must distinguish between:

- what exists now;
- what is planned;
- what is an example;
- what is a template;
- what is intentionally out of scope.

Do not claim automation, enforcement, installation, or integration support unless the repository contains working proof for it.

## Validation

At minimum, run:

```bash
make doctor
make smoke
```

For documentation-only changes, also run a product-term scan before release. Keep the denylist local if it contains private source-project terms:

```bash
rg -n -f /path/to/local-private-denylist.txt .
```

Any matches must be justified, sanitized, or removed before public release.

For public-facing changes, do not claim maturity, automation, examples, integrations, or community surfaces that are not implemented in the repository.

## Pull Request Checklist

Before submitting a PR:

- The PR has one clear scope.
- The PR title and commit title follow the public title standard.
- The PR body includes Problem, Solution, Scope, Validation, Risks, and Follow-ups when the change is meaningful.
- Versioned public assets include a metadata block.
- The README and manifest remain truthful.
- No product-specific source memory was copied as-is.
- All examples are generic or clearly marked as placeholders.
- New operating rules have one clear owner document.
- Validation results are reported honestly.
- No noisy AI phrases or bad commit wording appear in the PR title, PR body, or commit messages.

## License

By contributing, you agree that your contribution is licensed under the MIT License.
