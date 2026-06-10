# Blueprint Clean Start Brief

This brief helps the next session start quickly.

It is not a second memory system. Canonical state lives in Project Memory, core, governance, and root documents.

## Current Recovery Point

Blueprint v0.4.1 is released on `main`.

The released bundle includes bootstrap presentation, complete product map, core contracts, governance standards, self-hosting governance, Project Memory structure, Project Memory templates, Feature Lifecycle templates, PR handoff templates, Guardian templates, checklists, recovery templates, source coverage matrix, system relationship map, AI product example, public release packaging, the system use-case validation suite, process-level regression evidence, context budgets, recovery budgets, and completed post-validation branch cleanup.

After v0.4.0, PR #30 landed process-level regression hardening in `develop`.
UC-03 now requires RT-01 through RT-18 scenario evidence before future
packaging can claim task-routing validation.

PR #32 landed router context and recovery budgets in `develop`.
L0/L1 work now has explicit limits for response length, context loading, and
recovery-document loading.

PR #36 landed the v0.4.1 process-efficiency dogfood audit in `develop`.
The audit records that L0/L1/L2 routing budgets can be applied to Blueprint
itself without full-process escalation for simple docs-only work.

The merged dogfood audit branch was removed locally and remotely after PR #36.

The `develop` branch remains the base for the next scoped framework work.

## Read First

1. `memory/project-kb/00_INDEX.md`
2. `memory/project-kb/08_CURRENT_STATE.md`
3. `memory/project-kb/05_IMPLEMENTATION_STATUS.md`
4. `memory/project-kb/10_REFERENCE.md`
5. `PRODUCT_MAP.md`
6. `core/TASK_PROCESS_ROUTER.md`

## Active Branch Model

Feature work targets `develop`.

Release work targets `main` only through an explicit release PR.

## Current Next Step

Select the next release scope through `core/TASK_PROCESS_ROUTER.md`.

Recommended next scoped PRs:

1. Next release scope planning.
2. Public packaging or release preparation only after the next scope is selected.
3. Additional examples or public polish only after the next scope is selected.

## Do Not Do

- Do not modify source-reference repositories.
- Do not mix unrelated template families in one PR.
- Do not move `develop` to `main` without a release PR.
- Do not start automation, CLI, installer, integration, or execution-layer work without explicit scope approval.
- Do not delete branches without explicit maintainer approval.
