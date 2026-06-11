# Blueprint Release Process

Last released version: v0.5.1.

Next release target: v0.6.0.

This document defines the manual release process for Blueprint.

Release work is separate from feature, template, checklist, and example work.

The public Blueprint repository uses `main` as the release-ready distribution branch. Maintainers may prepare release content on local or private integration branches, but only validated release state is published to the public repository.

## Release Branch Model

| Branch | Role |
| --- | --- |
| `main` | Release-ready public branch |
| `docs/<scope>` | Scoped documentation or packaging branch before publication |
| `release/vX.Y.Z` | Optional release candidate branch when needed |
| local/private integration branch | Maintainer-only work before public release |

## Release Readiness Gates

Before a release PR into `main`, confirm:

- `VERSION` matches the intended release.
- `CHANGELOG.md` has an entry for the intended release.
- `BUNDLE_MANIFEST.md` lists every included public asset.
- `README.md` matches current included and planned status.
- `PRODUCT_MAP.md` has no unresolved required system gaps.
- `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` has no unresolved required system gaps.
- `VALIDATION_CHECKLIST.md` passes or records honest not-run evidence.
- Support, conduct, and security files exist at the repository root.
- GitHub contribution templates exist and match `CONTRIBUTING.md`.

## Required Validation

Run:

```bash
make doctor
make config
make smoke
git diff --check
```

Also run:

- markdown link check;
- forbidden public wording scan;
- product-term scan;
- noisy phrase scan;
- commit and PR title quality check;
- PR body structure check.

## Release PR Body

Use this structure:

```text
Problem

Solution

Scope

Validation

Risks

Follow-ups
```

For a release PR, include:

```text
Asset: blueprint-release
Version: vX.Y.Z
Type: Release
Author: Blueprint Maintainers
Description:
Breaking Changes:
Validation:
```

## Release Rules

- Release PRs target `main`.
- Release PRs should come from a validated local/private integration branch, a scoped docs branch, or a release branch.
- Release PRs must not add unrelated features.
- Release PRs must not introduce product implementation.
- Release PRs must not introduce automation unless that automation is the explicit release scope.
- Branch deletion happens only after separate maintainer approval.

## After Merge

After a release PR merges:

1. Confirm `main` contains the intended release files.
2. Confirm README, manifest, changelog, and version agree.
3. Create a GitHub release or tag only when explicitly approved.
4. Update Project Memory if the release changes durable state.
5. Start the next scoped branch from the current release baseline.
