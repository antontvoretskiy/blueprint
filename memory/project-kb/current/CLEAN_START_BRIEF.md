# Blueprint Clean Start Brief

This brief helps the next session start quickly.

It is not a second memory system. Canonical state lives in Project Memory, core, governance, and root documents.

## Current Recovery Point

Blueprint v0.3.0 is released on `main`.

The released bundle includes bootstrap presentation, complete product map, core contracts, governance standards, self-hosting governance, Project Memory structure, Project Memory templates, Feature Lifecycle templates, PR handoff templates, Guardian templates, checklists, recovery templates, source coverage matrix, system relationship map, AI product example, and public release packaging.

The `develop` branch also includes the unreleased system use-case validation suite, a passing system use-case validation result, and completed post-validation branch cleanup.

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

Select the next v0.4.0 scope through `core/TASK_PROCESS_ROUTER.md`, or prepare release packaging if maintainers decide the validated `develop` state is ready for `main`.

Recommended next scoped PRs:

1. v0.4.0 scope planning.
2. Public packaging or release preparation if the validation bundle should move to `main`.
3. Additional examples or public polish only after the next scope is selected.

## Do Not Do

- Do not modify source-reference repositories.
- Do not mix unrelated template families in one PR.
- Do not move `develop` to `main` without a release PR.
- Do not start automation, CLI, installer, integration, or execution-layer work without explicit scope approval.
- Do not delete branches without explicit maintainer approval.
