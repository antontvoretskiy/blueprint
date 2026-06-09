# Blueprint Verification Standard

This standard defines how Blueprint reports validation evidence.

## Verification Principle

Validation is not a slogan. It is evidence.

A PR should not claim a check passed unless the command, scan, review, or manual inspection supports that claim.

## Status Terms

Use these terms consistently:

| Term | Meaning |
| --- | --- |
| `PASS` | The check ran and met expectations |
| `FAIL` | The check ran and found a problem |
| `NOT RUN` | The check was not run, with a reason |
| `N/A` | The check does not apply to this scope |

Do not use vague substitutes such as "looks good" when a check can be named.

## Minimum Local Validation

For Blueprint documentation PRs:

```bash
make doctor
make smoke
git diff --check
```

`make smoke` must fail when a required endpoint returns a failing response.

If a check gives a false positive, fix the check or report the limitation.

## Public Documentation Scans

Public-facing PRs should run:

```bash
rg -n --hidden -g '!/.git/**' -g '!.env.local' -f /path/to/public-denylist.txt .
```

The public denylist should include reserved positioning terms and source-specific terms that must not appear in public files. A local source-specific denylist may be stricter. Keep private terms out of public docs.

## Link Checks

Check local markdown links for public entrypoints such as:

- `README.md`;
- `ARCHITECTURE.md`;
- `BUNDLE_MANIFEST.md`;
- `CONTRIBUTING.md`;
- current layer documents.

External links should be reviewed when they are central to the change.

## Scope Checks

For layer-specific PRs, confirm forbidden future layers were not created.

Examples:

- core PR should not add `governance/**`, `memory/**`, `templates/**`, `examples/**`, or `checklists/**`;
- governance PR should not add `memory/**`, `templates/**`, `examples/**`, or `checklists/**`;
- template PR should not add implementation automation unless approved.

## Title And Hygiene Checks

Check:

- commit title quality;
- PR title quality;
- required PR body sections;
- noisy AI phrases;
- bad commit wording.

The check should cover commit messages and PR text. Repository content may contain ordinary words that are not title-quality issues, so use judgment and report the exact scope of the scan.

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

## Verification Non-Goals

This standard does not replace:

- tests for future executable tooling;
- CI;
- security review;
- human review;
- release approval.

It defines the minimum language and evidence discipline for Blueprint PRs.
