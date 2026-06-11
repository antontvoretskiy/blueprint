# Blueprint System Use-Case Validation Suite

Asset: system-use-case-validation-suite
Version: v0.8.0
Type: Validation Suite
Author: Blueprint Maintainers
Status: Release target

This suite validates the repository workflows Blueprint promises to manage.

It is a manual validation suite paired with versioned validation fixtures. It
does not add a CLI, installer, integration, release automation, runtime, or
execution layer.

## Purpose

Blueprint should be considered ready for public packaging only when its core use cases can be validated from repository files.

The suite answers:

- Can a new contributor recover without old chat history?
- Can small tasks avoid unnecessary process overhead?
- Can meaningful work be routed to the right owner documents?
- Can a merge end with a clean start?
- Can public claims be traced to existing files?
- Can release state move through the public `main` branch without stale memory?
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
9. `docs/validation/fixtures/README.md`
10. `docs/validation/fixtures/system-use-cases.json`
11. `docs/validation/fixtures/process-level-regression.json`
12. `docs/validation/fixtures/release-readiness.json`
13. `governance/docs/verification-standard.md`
14. `governance/docs/git-policy.md`
15. `governance/docs/pr-standard.md`

Load additional owner documents when a test touches that owner.

## Result Terms

| Result | Meaning |
| --- | --- |
| `PASS` | The scenario was tested and met expectations |
| `FAIL` | The scenario was tested and found a blocker |
| `NOT RUN` | The scenario was intentionally skipped with a reason |
| `N/A` | The scenario does not apply to the current branch or release scope |

Do not mark the suite complete when a required test is `FAIL`.

## Process-Level Validation Rule

UC-03 validates router behavior, not only router text.

Do not mark UC-03 as `PASS` when the only evidence is that
`core/TASK_PROCESS_ROUTER.md` defines L0-L4. A `PASS` result requires scenario
evidence showing that small tasks stay small and risky tasks escalate.

For each process-level scenario, record:

- scenario ID;
- input task;
- expected process level;
- actual selected process level;
- compact mode expectation;
- escalation trigger, if any;
- result.

If any required scenario selects L4 without a real L4 trigger, UC-03 is `FAIL`.

## Use-Case Matrix

| ID | Use case | Owner documents | Method | Pass criteria |
| --- | --- | --- | --- | --- |
| UC-01 | Repository identity and start gate | `core/AGENTS.md`, `VALIDATION_CHECKLIST.md` | Confirm remote, branch, target branch, dirty state, and forbidden paths | Repository is `antontvoretskiy/blueprint`; work starts from current `main` or a scoped/private maintainer branch; source references stay read-only |
| UC-02 | Fresh recovery without chat history | `memory/project-kb/00_INDEX.md`, `memory/project-kb/08_CURRENT_STATE.md`, `memory/project-kb/10_REFERENCE.md` | Follow the recovery path from repository files only | Current state, included state, planned state, excluded state, and next work are clear |
| UC-03 | Task routing by process level | `core/TASK_PROCESS_ROUTER.md`, `docs/validation/fixtures/process-level-regression.json` | Classify the process-level regression scenarios below | Small tasks stay L0/L1, scoped layer work stays L2, feature work reaches L3, and architecture, migration, release, merge, or branch-state work reaches L4 |
| UC-04 | Owner document resolution | `memory/project-kb/10_REFERENCE.md`, `memory/project-kb/12_SYSTEM_RELATIONSHIP_MAP.md` | Pick a rule and trace it to one owner | The rule has one canonical owner and summaries do not redefine it |
| UC-05 | Project Memory integrity | `memory/project-kb/05_IMPLEMENTATION_STATUS.md`, `memory/project-kb/08_CURRENT_STATE.md`, `BUNDLE_MANIFEST.md` | Compare included, planned, and excluded states | Memory, manifest, and release status agree |
| UC-06 | Clean start after merge | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md`, `memory/project-kb/current/CLEAN_START_BRIEF.md` | Inspect the latest merged PR and current clean-start brief | The next session does not need the previous chat or completed branch |
| UC-07 | PR handoff readiness | `governance/docs/pr-standard.md`, `templates/pr-handoff/PR_BODY.template.md` | Check a PR body against required sections | Problem, Solution, Scope, Validation, Risks, and Follow-ups are present |
| UC-08 | Branch governance | `governance/docs/git-policy.md` | Confirm branch family, base branch, target branch, and public branch list | The public repository exposes only `main`; scoped work starts from current `main` or private maintainer integration and publishes only reviewed state to `main` |
| UC-09 | Feature Lifecycle gate | `core/FEATURE_LIFECYCLE_STANDARD.md`, `templates/feature-lifecycle/**` | Classify meaningful feature work | Meaningful feature work requires feature artifacts before implementation |
| UC-10 | Guardian boundary checks | `memory/project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md`, `templates/guardian/**` | Run repository, change, architecture, memory, PR, and release guard questions | Scope, claims, memory need, validation evidence, and release readiness are checked |
| UC-11 | Sanitization and leakage control | `MIGRATION_GUIDE.md`, `core/AGENTS.md`, `BUNDLE_MANIFEST.md` | Run product-term and forbidden wording scans | Private source names, product domains, stage history, product memory, and private PR history are absent |
| UC-12 | Documentation truthfulness | `governance/docs/documentation-standard.md`, `BUNDLE_MANIFEST.md` | Compare public claims against files | Planned work is not described as included or released |
| UC-13 | Release flow | `RELEASE.md`, `CHANGELOG.md`, `VERSION`, `docs/validation/fixtures/release-readiness.json` | Validate release state, branch targets, tag target, and GitHub release state | Release files, `main`, tag, and GitHub Release agree; no public `develop` branch is required |
| UC-14 | Public quality gate | `docs/benchmarks/spec-kit-open-source-marketing-benchmark.md`, `README.md` | Review README, guides, checks, contribution flow, and trust signals | Public surface meets the active quality standard or lists gaps honestly |
| UC-15 | Adoption path | `ADAPTATION_GUIDE.md`, `OPEN_SOURCE_GUIDE.md`, `examples/ai-product/**` | Follow the install/adaptation path for one sanitized repository shape | A user can identify what to copy, what to customize, and what remains external |

## Process-Level Regression Matrix

Run this matrix whenever UC-03 is validated.

| Scenario | Input task | Expected level | Compact mode | Escalation trigger | Pass criteria |
| --- | --- | --- | --- | --- | --- |
| RT-01 | Answer a simple repository question without edits | L0 | Yes | None | Answer does not run full Guardian or release checks |
| RT-02 | Report clean repository status | L0 | Yes | None | Report includes repo, branch, status, risk, and next step only |
| RT-03 | Fix a single typo in one Markdown file | L0 | Yes | None | Validation is scoped to identity, dirty tree, scope, and `git diff --check` |
| RT-04 | Update docs-only wording without changing ownership or public claims | L1 | Yes | None | Owner/source-of-truth check runs; Feature Lifecycle and full Guardian are skipped |
| RT-05 | Prepare a PR-ready handoff report for docs-only work without creating the PR | L1 | Yes | None | Uses compact handoff and does not run release or merge gates |
| RT-06 | Produce a clean-start status report after a docs PR already merged | L1 | Yes | None when no branch or release state changes | Reports current state without re-running full release validation |
| RT-07 | Commit docs-only changes on an already scoped branch | L1 | Yes | None | Commit validation stays docs-only; ordinary branch HEAD movement is not treated as L4 |
| RT-08 | Update compact Project Memory after a small docs-only state correction | L1 | Yes | None | Memory update stays scoped and does not become architecture review |
| RT-09 | Add or version a checklist, template, or validation asset | L2 | No | Public asset versioned | Layer boundary and manifest/reference checks run |
| RT-10 | Add a sanitized example project | L2 | No | Example layer changes | Example boundaries and leakage checks run |
| RT-11 | Update a core contract without changing architecture ownership | L2 | No | Core layer changes | Core owner and adjacent standards are checked |
| RT-12 | Change rule ownership or source-of-truth boundaries | L4 | No | Architecture/source-of-truth boundary changes | Architecture review, owner map, and memory checks run |
| RT-13 | Start meaningful feature implementation | L3 | No | Feature implementation | Feature Lifecycle artifacts are required before implementation |
| RT-14 | Add a new public workflow that requires feature artifacts | L3 | No | Meaningful public workflow | FEATURE, CLARIFICATION, PLAN, and TASKS are present or implementation stops |
| RT-15 | Transfer material from a source-reference repository | L4 | No | Migration/source-reference transfer | Include/review/exclude matrix and sanitization checks run |
| RT-16 | Prepare release version, tag, or release PR into `main` | L4 | No | Release state changes | Release Guardian, version, changelog, and manifest checks run |
| RT-17 | Merge, branch synchronization, or branch cleanup | L4 | No | Merge or branch-state changes | Branch policy, clean start, and recovery state checks run |
| RT-18 | Modify runtime, CLI, automation, dependencies, or integrations | L4 | No | Implementation or integration surface changes | Stops unless explicitly approved and routed to the correct owner |

Required UC-03 evidence format:

```text
Process-Level Regression:
- RT-01 expected L0, actual <LEVEL>, result <PASS_FAIL>
- RT-02 expected L0, actual <LEVEL>, result <PASS_FAIL>
- RT-03 expected L0, actual <LEVEL>, result <PASS_FAIL>
- RT-04 expected L1, actual <LEVEL>, result <PASS_FAIL>
- RT-05 expected L1, actual <LEVEL>, result <PASS_FAIL>
- RT-06 expected L1, actual <LEVEL>, result <PASS_FAIL>
- RT-07 expected L1, actual <LEVEL>, result <PASS_FAIL>
- RT-08 expected L1, actual <LEVEL>, result <PASS_FAIL>
- RT-09 expected L2, actual <LEVEL>, result <PASS_FAIL>
- RT-10 expected L2, actual <LEVEL>, result <PASS_FAIL>
- RT-11 expected L2, actual <LEVEL>, result <PASS_FAIL>
- RT-12 expected L4, actual <LEVEL>, result <PASS_FAIL>
- RT-13 expected L3, actual <LEVEL>, result <PASS_FAIL>
- RT-14 expected L3, actual <LEVEL>, result <PASS_FAIL>
- RT-15 expected L4, actual <LEVEL>, result <PASS_FAIL>
- RT-16 expected L4, actual <LEVEL>, result <PASS_FAIL>
- RT-17 expected L4, actual <LEVEL>, result <PASS_FAIL>
- RT-18 expected L4, actual <LEVEL>, result <PASS_FAIL>
```

## Dependency Verification

Use this dependency pass after the use-case matrix:

| Dependency check | Expected result |
| --- | --- |
| Every included file in `BUNDLE_MANIFEST.md` exists | PASS |
| Every new validation asset is linked from `BUNDLE_MANIFEST.md` and `memory/project-kb/10_REFERENCE.md` | PASS |
| Validation fixtures pass `scripts/check_validation_fixtures.py` | PASS |
| Every checklist is linked from `checklists/README.md` | PASS |
| Every memory owner points to an existing file | PASS |
| `README.md`, `BUNDLE_MANIFEST.md`, `CHANGELOG.md`, `RELEASE.md`, and `memory/project-kb/08_CURRENT_STATE.md` agree on release state | PASS |
| `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` has no stale next step for completed work | PASS |
| `memory/project-kb/current/CLEAN_START_BRIEF.md` points to the current next action, not a merged branch | PASS |

## Required Commands

Run these commands when validating the suite:

```bash
make quality
make doctor
make config
make smoke
git diff --check
python3 -m py_compile scripts/check_validation_fixtures.py
```

Also run:

- markdown local link check;
- validation fixture check;
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
- UC-03 Task routing by process level: PASS, with process-level regression evidence attached
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
