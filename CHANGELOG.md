# Changelog

All notable Blueprint changes are tracked in this file.

Blueprint uses SemVer. Release entries describe public framework assets, templates, examples, documentation, and governance changes.

## Unreleased

### Changed

- Reworked the README opening funnel with emoji navigation, practical AI-agent
  use cases, and a clearer repository-first adoption path.
- Updated the public Blueprint logo asset.
- Added the first README use-case screenshot for fresh-chat recovery.

## v0.4.2 - 2026-06-11

### Added

- Added a v0.4.1 process-efficiency dogfood audit for process levels, context
  budgets, recovery budgets, and compact L0/L1 behavior.

### Changed

- Refreshed Project Memory and clean-start state after the dogfood audit merged
  into `develop`.

## v0.4.1 - 2026-06-10

### Changed

- Hardened process-level validation so UC-03 requires scenario evidence for
  L0, L1, L2, L3, and L4 routing instead of only checking that router rules
  exist.
- Clarified that docs-only commits on already scoped branches do not escalate
  to L4 unless a real release, merge, branch-state, architecture, migration, or
  implementation trigger is present.
- Marked the v0.4.0 UC-03 validation evidence as historical and insufficient
  for future public packaging without the process-level regression matrix.
- Recorded the first v0.4.1 process-level regression pass for RT-01 through
  RT-18 in the current validation ledger.
- Added context budgets for L0, L1, L2, L3, and L4 so small tasks limit both
  procedure and context loading.
- Added recovery budgets for L0, L1, L2, L3, and L4 so small tasks limit
  recovery-document loading.

## v0.4.0 - 2026-06-10

### Added

- Recorded a passing system use-case validation result for `develop`.
- Added a manual system use-case validation suite and checklist for v0.4.0 scope validation.
- Added compact L0/L1 process rules for docs-only work, handoffs, status checks, and scoped reports.

### Changed

- Aligned README and Project Memory with the current validation-suite development state.
- Post-release Project Memory and clean-start recovery state refreshed after v0.3.0.
- Post-merge clean-start state refreshed after recovery validation landed in `develop`.
- Source coverage next steps refreshed for v0.4.0 scope selection.
- Recorded completed branch cleanup after PRs #20 through #25.
- Routed docs-only validation by process level instead of requiring release-style validation for every small documentation task.

### Excluded

- Additional examples remain planned for later release scope selection.
- Optional extensions remain outside the current bundle.

## v0.3.0 - 2026-06-10

### Added

- Core operating contracts for agents, task routing, feature lifecycle, PR handoff, clean start, and security.
- Governance standards for engineering rules, branch policy, PR lifecycle, verification, documentation, and ADRs.
- Project Memory structure and reusable Project Memory templates.
- Feature Lifecycle templates.
- PR handoff templates.
- Guardian templates.
- Recovery templates.
- Installation, recovery, branch governance, PR readiness, and clean-start checklists.
- First sanitized AI product adoption example.
- Public release packaging, support, security, conduct, and contribution templates.

### Excluded

- CLI.
- Installer.
- GitHub Actions enforcement.
- Runtime integrations.
- Agent execution layer.
- Workflow execution layer.
- Code generator.

## v0.2.0

### Added

- Core governance and Project Memory templates.
- Feature Lifecycle template bundle.
- PR handoff template bundle.

## v0.1.0

### Added

- Public repository bootstrap.
- Product definition.
- Architecture boundary.
- Bundle manifest.
- Contribution policy.
- Local preview environment.
- Open-source presentation benchmark.
