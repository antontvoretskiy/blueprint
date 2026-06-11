# Blueprint Clean Start Brief

This brief helps the next session start quickly.

It is not a second memory system. Canonical state lives in Project Memory, core, governance, and root documents.

## Current Recovery Point

Blueprint v0.7.0 is the current prepared release state.

The prepared bundle includes bootstrap presentation, complete product map, core contracts, governance standards, self-hosting governance, Project Memory structure, Project Memory templates, Feature Lifecycle templates, PR handoff templates, Guardian templates, checklists, recovery templates, source coverage matrix, system relationship map, AI product example, public release packaging, the system use-case validation suite, process-level regression evidence, context budgets, recovery budgets, the process-efficiency dogfood audit, completed post-validation branch cleanup, documentation quality gates, and documentation navigation pages.

GitHub Release `v0.6.1` was published from `main`. Publishing a GitHub Release
or tag for `v0.7.0` remains a separate approval-gated step.

The public GitHub repository now exposes only `main` as the release-ready
distribution branch. Local or private maintainer integration branches may exist,
but they are not part of the public branch list.

Release `v0.5.1` aligns the public main-only distribution model and adds clearer
adoption copy maps.

Release `v0.6.1` keeps documentation quality gates with `make quality`,
`scripts/check_quality.py`, and a docs-quality GitHub Actions workflow while
removing Dependabot from the public repository.

Release `v0.7.0` adds `docs/index.md`, `docs/nav.md`, `docs/quickstart.md`,
`docs/concepts/repository-first.md`, `docs/reference/templates.md`,
`docs/reference/governance.md`, and `docs/community.md`.

## Read First

1. `memory/project-kb/00_INDEX.md`
2. `memory/project-kb/08_CURRENT_STATE.md`
3. `memory/project-kb/05_IMPLEMENTATION_STATUS.md`
4. `memory/project-kb/10_REFERENCE.md`
5. `PRODUCT_MAP.md`
6. `core/TASK_PROCESS_ROUTER.md`

## Active Branch Model

Public distribution targets `main`.

Maintainers may use local or private integration branches before publication.

Adopting repositories may choose `main` only or `main` plus an integration
branch, but the chosen model must be documented in their Git policy and Project
Memory.

## Current Next Step

Select the next release scope after v0.7.0.

Recommended next scoped work:

1. Run final release validation for the v0.7.0 docs navigation branch.
2. Confirm that the public branch list remains `main` only after publication.
3. Decide whether the next scope is validation fixtures, examples catalog, or CI expansion.

## Do Not Do

- Do not modify source-reference repositories.
- Do not mix unrelated template families in one PR.
- Do not publish local or private integration branches to the public repository unless explicitly approved.
- Do not start CLI, installer, release automation, integration, or execution-layer work without explicit scope approval.
- Do not create a new tag or GitHub Release without maintainer approval.
- Do not delete branches without explicit maintainer approval.
