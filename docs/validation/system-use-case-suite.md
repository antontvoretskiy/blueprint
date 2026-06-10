# Blueprint System Use-Case Validation Suite

Asset: system-use-case-validation-suite
Version: v0.4.0
Type: Validation Suite
Author: Blueprint Maintainers
Status: Unreleased on `develop`

This suite validates the repository workflows Blueprint promises to manage.

It is a manual validation suite. It does not add automation, a CLI, an installer, an integration, or an execution layer.

## Purpose

Blueprint should be considered ready for public packaging only when its core use cases can be validated from repository files.

The suite answers:

- Can a new contributor recover without old chat history?
- Can small tasks avoid unnecessary process overhead?
- Can meaningful work be routed to the right owner documents?
- Can a merge end with a clean start?
- Can public claims be traced to existing files?
- Can release state move from `develop` to `main` without stale memory?
- Can private or product-specific content be kept out of the public framework?

## Router Classification

```text
Detected Task Type: Checklist and Project Memory validation
Detected Process Level: L2 scoped layer change
Required Rules: core/AGENTS.md, core/TASK_PROCESS_ROUTER.md, governance/docs/verification-standard.md, memory/project-kb/10_REFERENCE.md
Required Artifacts: validation suite, checklist, manifest/reference links
Skipped Rules: Feature Lifecycle, release process, runtime validation
Reason: this is a manual validation asset, not a new product feature, release, runtime, CLI, or automation layer
```

## Required Inputs

Read these files before running the suite:

1. `core/AGENTS.md`
2. `core/TASK_PROCESS_ROUTER.md`
3. `memory/project-kb/00_INDEX.md`
4. `memory/project-kb/08_CURRENT_STATE.md`
5. `memory/project-kb/05_IMPLEMENTATION_STATUS.md`
6. `memory/project-kb/10_REFERENCE.md`
7. `BUNDLE_MANIFEST.md`
8. `VALIDATION_CHECKLIST.md`
9. `governance/docs/verification-standard.md`
10. `governance/docs/git-policy.md`
11. `governance/docs/pr-standard.md`

Load additional owner documents when a test touches that owner.

## Result Terms

| Result | Meaning |
| --- | --- |
| `PASS` | The scenario was tested and met expectations |
| `FAIL` | The scenario was tested and found a blocker |
| `NOT RUN` | The scenario was intentionally skipped with a reason |
| `N/A` | The scenario does not apply to the current branch or release scope |

Do not mark the suite complete when a required test is `FAIL`.

## Use-Case Matrix

| ID | Use case | Owner documents | Method | Pass criteria |
| --- | --- | --- | --- | --- |
| UC-01 | Repository identity and start gate | `core/AGENTS.md`, `VALIDATION_CHECKLIST.md` | Confirm remote, branch, base branch, dirty state, and forbidden paths | Repository is `antontvoretskiy/blueprint`; work starts from a scoped branch; source references stay read-only |
| UC-02 | Fresh recovery without chat history | `memory/project-kb/00_INDEX.md`, `memory/project-kb/08_CURRENT_STATE.md`, `memory/project-kb/10_REFERENCE.md` | Follow the recovery path from repository files only | Current state, included state, planned state, excluded state, and next work are clear |
| UC-03 | Task routing by process level | `core/TASK_PROCESS_ROUTER.md` | Classify sample L0, L1, L2, L3, and L4 tasks | Small tasks do not trigger full ceremony; risky work gets the correct gates |
| UC-04 | Owner document resolution | `memory/project-kb/10_REFERENCE.md`, `memory/project-kb/12_SYSTEM_RELATIONSHIP_MAP.md` | Pick a rule and trace it to one owner | The rule has one canonical owner and summaries do not redefine it |
| UC-05 | Project Memory integrity | `memory/project-kb/05_IMPLEMENTATION_STATUS.md`, `memory/project-kb/08_CURRENT_STATE.md`, `BUNDLE_MANIFEST.md` | Compare included, planned, and excluded states | Memory, manifest, and release status agree |
| UC-06 | Clean start after merge | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md`, `memory/project-kb/current/CLEAN_START_BRIEF.md` | Inspect the latest merged PR and current clean-start brief | The next session does not need the previous chat or completed branch |
| UC-07 | PR handoff readiness | `governance/docs/pr-standard.md`, `templates/pr-handoff/PR_BODY.template.md` | Check a PR body against required sections | Problem, Solution, Scope, Validation, Risks, and Follow-ups are present |
| UC-08 | Branch governance | `governance/docs/git-policy.md` | Confirm branch family, base branch, and target branch | `develop` is used for integration; `main` changes only through release PRs |
| UC-09 | Feature Lifecycle gate | `core/FEATURE_LIFECYCLE_STANDARD.md`, `templates/feature-lifecycle/**` | Classify meaningful feature work | Meaningful feature work requires feature artifacts before implementation |
| UC-10 | Guardian boundary checks | `memory/project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md`, `templates/guardian/**` | Run repository, change, architecture, memory, PR, and release guard questions | Scope, claims, memory need, validation evidence, and release readiness are checked |
| UC-11 | Sanitization and leakage control | `MIGRATION_GUIDE.md`, `core/AGENTS.md`, `BUNDLE_MANIFEST.md` | Run product-term and forbidden wording scans | Private source names, product domains, stage history, product memory, and private PR history are absent |
| UC-12 | Documentation truthfulness | `governance/docs/documentation-standard.md`, `BUNDLE_MANIFEST.md` | Compare public claims against files | Planned work is not described as included or released |
| UC-13 | Release flow | `RELEASE.md`, `CHANGELOG.md`, `VERSION` | Validate release state and branch targets | `develop` contains unreleased work; `main` receives only release-ready snapshots |
| UC-14 | Public quality gate | `docs/benchmarks/spec-kit-open-source-marketing-benchmark.md`, `README.md` | Review README, guides, checks, contribution flow, and trust signals | Public surface meets the active quality standard or lists gaps honestly |
| UC-15 | Adoption path | `ADAPTATION_GUIDE.md`, `OPEN_SOURCE_GUIDE.md`, `examples/ai-product/**` | Follow the install/adaptation path for one sanitized repository shape | A user can identify what to copy, what to customize, and what remains external |

## Dependency Verification

Use this dependency pass after the use-case matrix:

| Dependency check | Expected result |
| --- | --- |
| Every included file in `BUNDLE_MANIFEST.md` exists | PASS |
| Every new validation asset is linked from `BUNDLE_MANIFEST.md` and `memory/project-kb/10_REFERENCE.md` | PASS |
| Every checklist is linked from `checklists/README.md` | PASS |
| Every memory owner points to an existing file | PASS |
| `README.md`, `BUNDLE_MANIFEST.md`, `CHANGELOG.md`, `RELEASE.md`, and `memory/project-kb/08_CURRENT_STATE.md` agree on release state | PASS |
| `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` has no stale next step for completed work | PASS |
| `memory/project-kb/current/CLEAN_START_BRIEF.md` points to the current next action, not a merged branch | PASS |

## Required Commands

Run these commands when validating the suite:

```bash
make doctor
make config
make smoke
git diff --check
```

Also run:

- markdown local link check;
- forbidden public wording scan;
- product-term scan;
- stale recovery phrase scan;
- noisy wording scan;
- open PR check;
- branch cleanup candidate check.

If a command is not run, report it as `NOT RUN: <reason>`.

## Evidence Format

Use this format in PR bodies and release validation notes:

```text
System Use-Case Validation:
- UC-01 Repository identity and start gate: PASS
- UC-02 Fresh recovery without chat history: PASS
- UC-03 Task routing by process level: PASS
- UC-04 Owner document resolution: PASS
- UC-05 Project Memory integrity: PASS
- UC-06 Clean start after merge: PASS
- UC-07 PR handoff readiness: PASS
- UC-08 Branch governance: PASS
- UC-09 Feature Lifecycle gate: PASS
- UC-10 Guardian boundary checks: PASS
- UC-11 Sanitization and leakage control: PASS
- UC-12 Documentation truthfulness: PASS
- UC-13 Release flow: PASS
- UC-14 Public quality gate: PASS
- UC-15 Adoption path: PASS
```

Attach short evidence for each `FAIL` or `NOT RUN`.

## Failure Handling

When a use case fails:

1. Identify the owner document.
2. Confirm whether the failure is stale memory, missing linkage, missing asset, contradictory claim, or missing process.
3. Open one scoped PR for the failing layer.
4. Re-run the failed scenario and dependency checks.
5. Update clean-start memory only when the next session would otherwise recover incorrectly.

Do not compensate for a failed use case by relying on old chat history.

## Explicit Exclusions

This suite does not add:

- runtime framework;
- agent runtime;
- workflow engine;
- code generator;
- CLI;
- installer;
- GitHub Actions;
- MCP integration;
- product implementation;
- private source memory.

Those areas can be governed by Blueprint, but they are not part of this validation asset.
