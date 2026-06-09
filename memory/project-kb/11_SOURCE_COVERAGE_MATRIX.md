# Blueprint Source Coverage Matrix

This document tracks whether portable system logic from the read-only source reference has a Blueprint owner.

It exists to prevent silent loss during adaptation.

## Coverage Rule

Blueprint does not copy source documents one-to-one.

Blueprint adapts portable system logic and removes private product state.

Each source-reference system document must resolve to one of these outcomes:

| Status | Meaning |
| --- | --- |
| Covered | Blueprint has an active owner document for the portable logic |
| Covered by template | Blueprint has a reusable template for the portable artifact |
| Partial | Blueprint has active logic, but reusable templates or detailed owner coverage are still missing |
| Planned | The item belongs in Blueprint, but has not been adapted yet |
| Excluded | The item is product-specific and must not be imported into Blueprint |

Do not mark the transfer complete while any system item is `Partial` or `Planned`.

## Current Coverage Summary

| Area | Source items | Covered | Partial | Planned | Excluded |
| --- | ---: | ---: | ---: | ---: | ---: |
| Product model and process levels | 2 | 2 | 0 | 0 | 0 |
| Core contracts | 5 | 5 | 0 | 0 | 0 |
| Governance standards | 7 | 7 | 0 | 0 | 0 |
| Project Memory root files | 11 | 11 | 0 | 0 | 0 |
| Clean start | 1 | 1 | 0 | 0 | 0 |
| Guardian memory docs | 2 | 2 | 0 | 0 | 0 |
| Feature lifecycle artifacts | 4 | 4 | 0 | 0 | 0 |
| Recovery reusable templates | 3 | 3 | 0 | 0 | 0 |
| Product-specific memory and history | Variable | 0 | 0 | 0 | Variable |

Current conclusion: product model, process levels, core, governance, Project Memory templates, and Feature Lifecycle templates are covered; PR handoff templates and Guardian templates are not complete yet.

## Product Model And Process-Level Coverage

| System item | Blueprint owner | Status | Notes |
| --- | --- | --- | --- |
| Complete product shape | `PRODUCT_MAP.md` | Covered | Defines subsystems, ownership, project/feature management, and packaging gates |
| L0-L4 process levels | `core/TASK_PROCESS_ROUTER.md` | Covered | Defines task-size routing so small work does not require full procedure |

## Core Contract Coverage

| Source-reference document | Blueprint owner | Status | Notes |
| --- | --- | --- | --- |
| `AGENTS.md` | `core/AGENTS.md` | Covered | Adapted as the agent operating contract |
| `TASK_PROCESS_ROUTER.md` | `core/TASK_PROCESS_ROUTER.md` | Covered | Adapted with Blueprint layer routing |
| `FEATURE_LIFECYCLE_STANDARD.md` | `core/FEATURE_LIFECYCLE_STANDARD.md` | Covered | Active lifecycle standard exists |
| `PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | Covered | Active handoff and clean-start standard exists |
| `SECURITY.md` | `core/SECURITY.md` | Covered | Adapted as portable security baseline |

## Governance Coverage

| Source-reference document | Blueprint owner | Status | Notes |
| --- | --- | --- | --- |
| `docs/governance-index.md` | `governance/docs/governance-index.md` | Covered | Authority map adapted and sanitized |
| `docs/engineering-governance.md` | `governance/docs/engineering-governance.md` | Covered | Includes self-hosting governance |
| `docs/git-policy.md` | `governance/docs/git-policy.md` | Covered | Branch, commit, merge, stale branch, cleanup logic covered |
| `docs/pr-standard.md` | `governance/docs/pr-standard.md` | Covered | PR title, body, scope, review, merge logic covered |
| `docs/verification-standard.md` | `governance/docs/verification-standard.md` | Covered | Evidence language and verification model covered |
| `docs/documentation-standard.md` | `governance/docs/documentation-standard.md` | Covered | Truthfulness, lifecycle, ownership, status language covered |
| `docs/adr-policy.md` | `governance/docs/adr-policy.md` | Covered | ADR lifecycle, status, review, supersession logic covered |

Product-specific source sections inside governance docs were not copied. Portable rules were adapted.

## Project Memory Coverage

| Source-reference document | Blueprint owner | Status | Notes |
| --- | --- | --- | --- |
| `project-kb/00_INDEX.md` | `memory/project-kb/00_INDEX.md`, `templates/project-memory/00_INDEX.template.md` | Covered | Active Blueprint memory entrypoint and reusable template exist |
| `project-kb/01_PROJECT_CONTEXT.md` | `templates/project-memory/01_PROJECT_CONTEXT.template.md` | Covered | Reusable template exists |
| `project-kb/02_PRODUCT_MAP.md` | `templates/project-memory/02_PROJECT_MAP.template.md` | Covered | Reusable template exists |
| `project-kb/03_SYSTEM_ARCHITECTURE.md` | `ARCHITECTURE.md`, `templates/project-memory/03_SYSTEM_ARCHITECTURE.template.md` | Covered | Active architecture and reusable memory template exist |
| `project-kb/04_DOMAIN_MODEL.md` | `templates/project-memory/04_DOMAIN_MODEL.template.md` | Covered | Reusable template exists |
| `project-kb/05_IMPLEMENTATION_STATUS.md` | `memory/project-kb/05_IMPLEMENTATION_STATUS.md`, `templates/project-memory/05_IMPLEMENTATION_STATUS.template.md` | Covered | Active Blueprint implementation status and reusable template exist |
| `project-kb/06_WORKFLOW_AND_RULES.md` | `memory/project-kb/06_WORKFLOW_AND_RULES.md`, `templates/project-memory/06_WORKFLOW_AND_RULES.template.md` | Covered | Active recovery summary and reusable template exist |
| `project-kb/07_DECISIONS_LOG.md` | `memory/project-kb/07_DECISIONS_LOG.md`, `templates/project-memory/07_DECISIONS_LOG.template.md` | Covered | Active decisions log and reusable template exist |
| `project-kb/08_CURRENT_STATE.md` | `memory/project-kb/08_CURRENT_STATE.md`, `templates/project-memory/08_CURRENT_STATE.template.md` | Covered | Active current recovery state and reusable template exist |
| `project-kb/09_TASK_HISTORY.md` | `memory/project-kb/09_TASK_HISTORY.md`, `templates/project-memory/09_TASK_HISTORY.template.md` | Covered | Active task history and reusable template exist |
| `project-kb/10_REFERENCE.md` | `memory/project-kb/10_REFERENCE.md`, `templates/project-memory/10_REFERENCE.template.md` | Covered | Active reference map and reusable template exist |

The source `01` through `04` documents were converted into reusable templates instead of active Blueprint memory because their source content was product-specific.

## Clean Start And Recovery Coverage

| Source-reference item | Blueprint owner | Status | Notes |
| --- | --- | --- | --- |
| `project-kb/current/CLEAN_START_BRIEF.md` | `memory/project-kb/current/CLEAN_START_BRIEF.md` | Covered | Active clean-start brief exists |
| Clean-start brief reusable format | `templates/recovery/CLEAN_START_BRIEF.template.md` | Covered by template | Portable template exists |
| Recovery path reusable format | `templates/recovery/RECOVERY_PATH.template.md` | Covered by template | Portable template exists |
| Recovery validation reusable format | `templates/recovery/RECOVERY_VALIDATION.template.md` | Covered by template | Portable template exists |

## Guardian Coverage

| Source-reference item | Blueprint owner | Status | Notes |
| --- | --- | --- | --- |
| `project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md` | `memory/project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md` | Covered | Active architecture summary exists |
| `project-kb/GUARDIAN_VALIDATION_SCENARIOS.md` | `memory/project-kb/GUARDIAN_VALIDATION_SCENARIOS.md` | Covered | Generic validation scenarios exist |
| Guardian reusable templates | None yet | Planned | Must become `templates/guardian/**` |

Guardian process logic exists, but reusable Guardian templates are not complete yet.

## Feature Lifecycle Artifact Coverage

| Source-reference item | Blueprint owner | Status | Notes |
| --- | --- | --- | --- |
| `project-kb/features/<feature>/FEATURE.md` | `templates/feature-lifecycle/FEATURE.template.md` | Covered | Reusable template exists |
| `project-kb/features/<feature>/CLARIFICATION.md` | `templates/feature-lifecycle/CLARIFICATION.template.md` | Covered | Reusable template exists |
| `project-kb/features/<feature>/PLAN.md` | `templates/feature-lifecycle/PLAN.template.md` | Covered | Reusable template exists |
| `project-kb/features/<feature>/TASKS.md` | `templates/feature-lifecycle/TASKS.template.md` | Covered | Reusable template exists |

The active standard exists in `core/FEATURE_LIFECYCLE_STANDARD.md`, and reusable feature artifacts now exist in `templates/feature-lifecycle/**`.

## PR Handoff Template Coverage

| Source-reference item | Blueprint owner | Status | Notes |
| --- | --- | --- | --- |
| PR handoff summary format | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | Covered | Active standard exists |
| Reusable PR handoff template | None yet | Planned | Must become `templates/pr-handoff/**` |
| Reusable clean-start template | `templates/recovery/CLEAN_START_BRIEF.template.md` | Covered by template | Template exists |

## Explicit Exclusions

The following source-reference areas must not be imported into Blueprint core:

- runtime implementation;
- product-specific stage history;
- product UI;
- product API;
- product algorithms;
- product release history;
- product PR timeline;
- product-specific decisions;
- private project memory;
- private domain memory.

Blueprint may provide templates that help another project govern those areas, but Blueprint must not contain their implementation or private state.

## Required Next Steps

1. Add PR handoff templates.
2. Add Guardian templates.
3. Add checklists for recovery, branch governance, PR readiness, and clean start.
4. Re-run this matrix and change `Partial` or `Planned` only when the target files exist.

Do not start public packaging while this matrix contains `Partial` or `Planned` system items.
