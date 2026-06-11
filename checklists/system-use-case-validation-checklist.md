# Blueprint System Use-Case Validation Checklist

Status: Checklist v0.8.0.

Use this checklist with `docs/validation/system-use-case-suite.md` before public packaging, release preparation, or branch cleanup.

## Repository And Scope

| Check | Result | Evidence |
| --- | --- | --- |
| Working repository is `antontvoretskiy/blueprint` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Work is on current `main` or a scoped/private maintainer branch | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
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

## Process-Level Regression Results

UC-03 is not complete until these scenarios have expected and actual process
levels recorded.

| Scenario | Expected level | Actual level | Result | Evidence |
| --- | --- | --- | --- | --- |
| RT-01 Answer-only repository question | L0 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-02 Clean repository status check | L0 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-03 Single Markdown typo fix | L0 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-04 Docs-only wording update | L1 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-05 Docs-only PR-ready handoff report | L1 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-06 Clean-start status report without state change | L1 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-07 Docs-only commit on scoped branch | L1 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-08 Small Project Memory status correction | L1 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-09 Checklist, template, or validation asset versioning | L2 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-10 Sanitized example project addition | L2 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-11 Core contract update without ownership change | L2 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-12 Rule ownership or source-of-truth boundary change | L4 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-13 Meaningful feature implementation | L3 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-14 New public workflow requiring feature artifacts | L3 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-15 Source-reference transfer | L4 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-16 Release version, tag, or release PR | L4 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-17 Merge, branch synchronization, or branch cleanup | L4 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| RT-18 Runtime, CLI, automation, dependency, or integration modification | L4 | `<LEVEL>` | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |

UC-03 fails when an L0 or L1 scenario escalates to L4 without a documented
escalation trigger.

## Dependency Results

| Check | Result | Evidence |
| --- | --- | --- |
| Manifest included files exist | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| New validation assets are linked from manifest and reference map | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
| Validation fixtures pass local fixture checker | `<PASS_FAIL_OR_NA>` | `<EVIDENCE>` |
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
| Validation fixture check | `<PASS_FAIL_OR_NOT_RUN>` | `<EVIDENCE>` |
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
- `<VALIDATION_BLOCKED_PROCESS_LEVEL_REGRESSION>`

Reason:

`<REASON>`
