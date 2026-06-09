# Blueprint Verification Standard

This standard defines how Blueprint reports validation evidence.

## Purpose

Verification keeps public claims tied to evidence.

It prevents:

- claiming implementation before files exist;
- reporting checks without running them;
- treating plans as shipped behavior;
- hiding skipped validation;
- relying on old chat context as evidence;
- merging governance changes without checking their scope.

## Ownership

This document owns:

- validation terminology;
- evidence levels;
- validation freshness;
- validation completeness;
- verification debt;
- scope-specific validation expectations;
- reporting format.

Branch and PR mechanics are owned by `governance/docs/git-policy.md` and `governance/docs/pr-standard.md`.

Documentation status terms are owned by `governance/docs/documentation-standard.md`.

## Dependencies

This standard depends on:

- `Makefile` for local validation commands that exist now;
- `CONTRIBUTING.md` for contributor-facing validation expectations;
- `governance/docs/pr-standard.md` for PR reporting sections;
- `governance/docs/documentation-standard.md` for truthfulness rules;
- `BUNDLE_MANIFEST.md` for included, planned, and excluded public status;
- `governance/docs/governance-index.md` for rule ownership.

## Verification Philosophy

Validation is not a slogan. It is evidence.

A PR should not claim a check passed unless a command, scan, review, or manual inspection supports that claim.

Blueprint prefers honest `NOT RUN` reporting over unsupported confidence.

## Verification Ownership Model

Each claim needs an owner:

| Claim type | Evidence owner |
| --- | --- |
| Public positioning | `README.md`, `OPEN_SOURCE_SPEC.md`, `ARCHITECTURE.md` |
| Included bundle content | `BUNDLE_MANIFEST.md` |
| Contribution workflow | `CONTRIBUTING.md` |
| Branch and PR rules | `governance/docs/git-policy.md`, `governance/docs/pr-standard.md` |
| Validation language | `governance/docs/verification-standard.md` |
| Documentation status | `governance/docs/documentation-standard.md` |
| Decision records | `governance/docs/adr-policy.md` |

If evidence and owner documents disagree, fix the owner document or the public claim.

## Verification Evidence Levels

Use the strongest evidence available for the scope:

| Level | Evidence | Use when |
| --- | --- | --- |
| Command | A local command ran and returned an outcome | Local tooling, formatting, smoke checks |
| Scan | A repository search or denylist scan ran | Forbidden terms, noisy PR wording, broken scope |
| Manual inspection | A maintainer inspected the relevant files | Architecture, documentation, public positioning |
| Cross-document review | Related owner documents were compared | Governance and documentation consistency |
| External confirmation | A remote service or GitHub state was checked | PR state, branch state, release state |

Do not upgrade weak evidence into a stronger claim.

## Verification Reporting Standard

Use these terms consistently:

| Term | Meaning |
| --- | --- |
| `PASS` | The check ran and met expectations |
| `FAIL` | The check ran and found a problem |
| `NOT RUN` | The check was not run, with a reason |
| `N/A` | The check does not apply to this scope |

Do not use vague substitutes such as "looks good" when a check can be named.

## Verification Claim Rule

A claim is valid only when:

- the owner document supports it;
- repository contents support it;
- validation evidence supports it;
- the PR body reports the evidence clearly.

If a claim is planned but not present, label it as planned.

If a claim belongs to a future layer, exclude it from the current PR.

## Evidence Rule

Evidence should be specific enough that another reviewer can reproduce or inspect it.

Good evidence:

```text
- make doctor: PASS
- make smoke: PASS
- git diff --check: PASS
- forbidden public wording scan: PASS
- markdown links check: PASS
```

Weak evidence:

```text
- docs checked
- should be fine
- validated manually
```

Manual inspection is acceptable when it states what was inspected.

## Verification Freshness Rule

Validation evidence should be current for the diff under review.

Re-run validation when:

- files changed after the last check;
- the target branch moved;
- a stale branch was refreshed;
- generated assets changed;
- public claims changed;
- release state changed.

Report stale evidence as `NOT RUN` or re-run it.

## Verification Completeness Rule

Validation must match the scope.

Examples:

- a governance PR should check governance owner documents and scope boundaries;
- a public docs PR should check README links and reserved public wording;
- a template PR should check template paths and install instructions;
- a release PR should check public status, versioning, and release notes.

Do not use a narrow check to validate a broader claim.

## Verification Debt

Verification debt exists when a useful check is missing, manual, incomplete, or blocked.

Report debt explicitly:

```text
- template install test: NOT RUN, templates are not included in this PR
- external link scan: NOT RUN, no external links changed
```

Do not hide verification debt in follow-up prose.

## Verification Inheritance Rule

A PR may reference earlier validation only when:

- the earlier validation applies to the same unchanged files;
- the target branch has not moved in a relevant way;
- the PR body identifies what is inherited and why it is still valid.

When unsure, re-run validation.

## Verification By Scope

| Scope | Required validation focus |
| --- | --- |
| Bootstrap docs | Public positioning, links, reserved wording, local preview commands |
| Core contracts | Rule ownership, recovery path, excluded future layers |
| Governance standards | Ownership map, cross-document consistency, scope boundaries |
| Project Memory materials | recovery usefulness, compactness, status language |
| Templates | copyability, placeholder safety, install instructions |
| Examples | educational clarity, non-core status, no private source leakage |
| Checklists | acceptance criteria, non-duplication, owner links |
| Release | version, manifest, README, architecture, contribution flow |

## Required Verification Matrix

For meaningful Blueprint documentation PRs:

| Check | Required |
| --- | --- |
| `make doctor` | Yes |
| `make smoke` | Yes when the local preview is expected to run |
| `git diff --check` | Yes |
| forbidden public wording scan | Yes for public-facing docs |
| product-term scan | Yes for source-derived work |
| markdown links check | Yes when markdown links are changed |
| scope boundary scan | Yes for layer-specific PRs |
| title quality check | Yes for commits and PR title |
| PR body structure check | Yes for meaningful PRs |
| noisy phrase scan | Yes for commit and PR text |

If a required check cannot run, report `NOT RUN` with the reason.

## Docs-Only Verification

Docs-only PRs should confirm:

- no executable tooling was added unless approved;
- no future layers were created accidentally;
- public claims match repository contents;
- status terms are accurate;
- links are valid;
- private source details are absent.

## Governance Verification

Governance PRs should confirm:

- each rule has one owner;
- summaries do not redefine owner documents;
- changed standards link to adjacent standards;
- branch and PR scope remain aligned;
- validation evidence uses the standard terms;
- no private product history entered governance files.

## Contract Verification

Reusable contracts should confirm:

- the contract owner is clear;
- compatibility impact is described;
- dependent docs are updated or listed as follow-ups;
- examples or templates do not claim support before they exist.

## Documentation Verification

Documentation changes should confirm:

- status labels are accurate;
- included and planned items are separated;
- public-facing pages do not overclaim;
- root docs and manifest agree;
- private source details are absent.

## Local Preview Verification

When public preview files or local environment files are changed, run:

```bash
make doctor
make smoke
```

`make doctor` checks local port and namespace isolation.

`make smoke` checks the local preview endpoints when the preview stack is running.

## Release Verification

Release PRs should confirm:

- release version uses SemVer;
- README, architecture, manifest, and contribution docs agree;
- included assets exist;
- planned assets are not presented as included;
- local validation passed or exceptions are reported;
- known risks and follow-ups are listed.

## Future Automation Map

Blueprint may add optional validation automation later.

Until automation exists, this standard is enforced through PR discipline and maintainer review.

Future automation must not redefine the validation rules. It should implement checks already owned by this document or another canonical owner.

## Forbidden Verification Claims

Do not claim:

- a check passed when it did not run;
- a feature exists because it is planned;
- a template exists before files are present;
- an example exists before files are present;
- automation exists before a working checker exists;
- a release is ready without release validation;
- private source validation applies to Blueprint without portable review.

## Reporting Format

In PR bodies, report validation as:

```text
- make doctor: PASS
- make smoke: PASS
- git diff --check: PASS
- forbidden public wording scan: PASS
- markdown links check: PASS
```

If a check was skipped:

```text
- sample project validation: NOT RUN, no example project exists in this scope
```

## Review Checklist

Before requesting review, confirm:

- validation terms use `PASS`, `FAIL`, `NOT RUN`, or `N/A`;
- commands and scans are named;
- skipped checks include reasons;
- evidence matches the scope;
- public claims match repository contents;
- stale evidence was refreshed or reported;
- verification debt is explicit;
- root docs remain truthful;
- release claims are not made from integration work.
