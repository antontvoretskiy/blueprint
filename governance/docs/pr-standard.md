# Blueprint Pull Request Standard

This standard defines how Blueprint PRs are titled, scoped, reviewed, validated, and merged.

## Purpose

The PR standard keeps changes reviewable and recoverable.

It ensures a reviewer can answer:

- what changed;
- why it changed;
- which paths are in scope;
- which paths are excluded;
- what public claims changed;
- how the change was validated;
- what remains later.

## Ownership

This document owns:

- PR title structure;
- PR body structure;
- one PR, one responsibility;
- PR size expectations;
- validation reporting requirements;
- docs-only PR rules;
- release PR rules;
- forbidden PR patterns.

Branch mechanics are owned by `governance/docs/git-policy.md`.

Validation terminology is owned by `governance/docs/verification-standard.md`.

## Dependencies

This standard depends on:

- `CONTRIBUTING.md` for public contribution expectations;
- `governance/docs/git-policy.md` for branch roles and commit naming;
- `governance/docs/verification-standard.md` for evidence language;
- `governance/docs/documentation-standard.md` for documentation truthfulness;
- `BUNDLE_MANIFEST.md` for public included, planned, and excluded status;
- `governance/docs/governance-index.md` for rule ownership.

## PR Naming Standard

Use the public title standard from `CONTRIBUTING.md`.

Default format:

```text
type(scope): concise outcome
```

Examples:

```text
docs(core): add portable operating contracts
docs(governance): add branch and PR standards
docs(memory): add project memory templates
fix(docs): repair manifest links
docs(release): prepare blueprint v0.1.0
```

For versioned public assets, use the title-style formats defined in `CONTRIBUTING.md`.

PR titles must describe the durable outcome, not the activity.

## One PR = One Responsibility

One PR should have one review story.

A PR is one responsibility when:

- it has one primary owner document or layer;
- its branch name matches the changed paths;
- the reviewer can validate it with one coherent checklist;
- the PR body can state one purpose without exceptions.

A PR is probably too broad when it combines:

- governance changes with examples;
- templates with release preparation;
- root presentation with unrelated framework layers;
- documentation changes with unapproved tooling;
- multiple public asset versions;
- unrelated repairs.

Split broad work before review unless maintainers explicitly approve the combined scope.

## PR Size Policy

Prefer small, complete PRs.

A PR should be large enough to leave the repository coherent, but small enough that:

- changed paths can be reviewed in one pass;
- validation evidence belongs to this PR;
- follow-up work is clearly separated;
- no future layer is described as already included.

Large framework migrations should be decomposed into ordered PRs.

## Required PR Sections

Meaningful PRs must include:

```text
## Problem

## Solution

## Scope

## Validation

## Risks

## Follow-ups
```

The Scope section must list:

- included paths;
- explicitly excluded paths;
- base branch;
- whether `main` changes;
- whether release state changes.

The Validation section must report commands, scans, and outcomes.

## Public Asset Metadata

If a PR adds or changes a versioned public asset, include:

```text
Asset:
Version:
Type:
Author:
Description:
Breaking Changes:
Validation:
```

Use full SemVer for Blueprint versions.

## Validation Reporting Policy

Use:

- `PASS`;
- `FAIL`;
- `NOT RUN`, with a reason;
- `N/A`, when the check does not apply.

Minimum documentation validation:

```bash
make doctor
make smoke
git diff --check
```

Public-facing PRs should also report:

- forbidden public wording scan;
- product-term scan;
- markdown links check;
- commit title quality check;
- PR title quality check;
- noisy phrase scan for PR and commit text;
- bad commit wording scan.

Do not claim validation that did not run.

## Docs-Only PR Rules

Documentation PRs may change repository presentation, governance, templates, examples, or checklists.

Documentation PRs must not:

- add executable tooling without approval;
- imply automation exists before it exists;
- include private source details;
- copy product-specific memory;
- change release state unless the PR is a release PR;
- combine documentation with unrelated local environment changes.

If a docs PR changes public status, update the manifest and relevant root docs in the same PR.

## Boundary And Contract Change Rules

If a PR changes a reusable contract, boundary, or installable public asset, it must state:

- which contract changed;
- whether the change is compatible;
- which documents link to the contract;
- whether examples or templates need follow-up updates;
- whether a version bump is needed.

Project-specific implementation behavior stays outside Blueprint core.

## Release PR Rules

Release PRs:

- target `main`;
- include a version in title and body;
- summarize changes since the previous release;
- verify README, architecture, manifest, and contribution rules;
- include release validation evidence;
- list known follow-ups.

Integration PRs into `develop` are not release PRs.

## Forbidden PR Patterns

Do not open PRs that:

- have vague titles;
- mix unrelated layers;
- stage unrelated local files;
- include private source names or private product history;
- claim future work as included;
- add unapproved automation;
- change release state accidentally;
- omit validation for meaningful changes;
- include noisy tool provenance in commit or PR text;
- add unapproved co-author trailers.

## Relationship To Adjacent Standards

| Area | Owner |
| --- | --- |
| Branch roles and cleanup | `governance/docs/git-policy.md` |
| Validation language | `governance/docs/verification-standard.md` |
| Documentation truthfulness | `governance/docs/documentation-standard.md` |
| ADR requirements | `governance/docs/adr-policy.md` |
| Rule authority | `governance/docs/governance-index.md` |
| Public contribution flow | `CONTRIBUTING.md` |

## Review Checklist

Before requesting review, confirm:

- branch base is correct;
- PR title follows the standard;
- PR body contains all required sections;
- one PR maps to one scope;
- changed paths match the branch purpose;
- owner documents are updated;
- root docs remain truthful;
- planned work is not described as included;
- source-specific details are absent;
- validation evidence is current;
- risks and follow-ups are explicit;
- merge title will produce professional public history.

## Merge Standard

Use squash merge unless maintainers request otherwise.

The squash title becomes the public history line and must follow the title standard.

The squash body should preserve:

- Problem;
- Solution;
- Scope summary;
- Validation summary;
- Risks;
- Follow-ups.

Do not add accidental tool provenance or unapproved co-author trailers.

## After Merge

After merge:

1. Sync the target branch.
2. Delete the merged feature branch if appropriate.
3. Run relevant validation on the target branch.
4. Report the clean-start state.
5. Start the next branch from the updated target branch.
