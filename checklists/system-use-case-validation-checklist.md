# Blueprint System Use-Case Validation Checklist

Status: Checklist v0.4.0.

Use this checklist with `docs/validation/system-use-case-suite.md` before public packaging, release preparation, or branch cleanup.

## Repository And Scope

| Check | Result | Evidence |
| --- | --- | --- |
| Working repository is `antontvoretskiy/blueprint` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Work is on a scoped branch from `develop` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| `main` is not changed directly | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Source-reference repositories are not modified | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Runtime, CLI, automation, and integration layers are out of scope unless explicitly selected | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Use-Case Results

| Use case | Result | Evidence |
| --- | --- | --- |
| UC-01 Repository identity and start gate | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-02 Fresh recovery without chat history | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-03 Task routing by process level | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-04 Owner document resolution | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-05 Project Memory integrity | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-06 Clean start after merge | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-07 PR handoff readiness | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-08 Branch governance | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-09 Feature Lifecycle gate | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-10 Guardian boundary checks | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-11 Sanitization and leakage control | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-12 Documentation truthfulness | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-13 Release flow | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-14 Public quality gate | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| UC-15 Adoption path | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Dependency Results

| Check | Result | Evidence |
| --- | --- | --- |
| Manifest included files exist | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| New validation assets are linked from manifest and reference map | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Checklist index includes this checklist | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Memory files do not contradict manifest, changelog, release state, or clean-start state | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| No stale completed branch or PR is listed as current work | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Branch cleanup candidates are identified without deleting branches | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

## Command Results

| Command or scan | Result | Evidence |
| --- | --- | --- |
| `make doctor` | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| `make config` | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| `make smoke` | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| `git diff --check` | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Markdown local link check | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Forbidden public wording scan | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Product-term scan | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Stale recovery phrase scan | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Noisy wording scan | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
| Open PR check | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |

## Acceptance Decision

Selected result:

- `<VALIDATION_READY>`
- `<VALIDATION_BLOCKED_USE_CASE_FAILURE>`
- `<VALIDATION_BLOCKED_DEPENDENCY_FAILURE>`
- `<VALIDATION_BLOCKED_STALE_RECOVERY>`
- `<VALIDATION_BLOCKED_SCOPE_DRIFT>`

Reason:

`<REASON>`
