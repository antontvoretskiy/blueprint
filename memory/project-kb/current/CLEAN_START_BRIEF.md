# Blueprint Clean Start Brief

This brief helps the next session start quickly.

It is not a second memory system. Canonical state lives in Project Memory, core, governance, and root documents.

## Current Recovery Point

Blueprint v0.5.0 is released on `main`.

The released bundle includes bootstrap presentation, complete product map, core contracts, governance standards, self-hosting governance, Project Memory structure, Project Memory templates, Feature Lifecycle templates, PR handoff templates, Guardian templates, checklists, recovery templates, source coverage matrix, system relationship map, AI product example, public release packaging, the system use-case validation suite, process-level regression evidence, context budgets, recovery budgets, the process-efficiency dogfood audit, and completed post-validation branch cleanup.

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

Release `v0.4.2` publishes PR #36 and PR #37 from validated `develop` state to
`main`.

PR #41 merged the v0.5.0 README public funnel into `develop`.

The merged scope includes the refreshed README funnel, updated Blueprint logo,
practical AI-agent use-case screenshots, bundle manifest updates, changelog
updates, and v0.5.0 release target notes.

Post-merge validation on `develop` passed for `make doctor`, `make config`,
`make smoke`, `git diff --check`, README local links/images, forbidden public
wording scan, noisy wording scan, and bad commit wording scan.

Release `v0.5.0` publishes the README public funnel, Blueprint logo refresh,
practical AI-agent use-case screenshots, bundle manifest updates, changelog
updates, release target notes, and post-funnel clean-start state from validated
`develop` state to `main`.

The next recovery step is post-release sync from `main` back to `develop`.

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

Sync `develop` from `main` after the v0.5.0 release PR merges.

Recommended next scoped PRs:

1. Post-release sync from `main` to `develop`.
2. Post-release Project Memory refresh only if durable recovery state changed.
3. Additional examples or adoption polish only after post-release state is confirmed.

## Do Not Do

- Do not modify source-reference repositories.
- Do not mix unrelated template families in one PR.
- Do not move `develop` to `main` without a release PR.
- Do not start automation, CLI, installer, integration, or execution-layer work without explicit scope approval.
- Do not create the v0.5.0 tag or GitHub Release without maintainer approval.
- Do not delete branches without explicit maintainer approval.
