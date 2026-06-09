# Blueprint Workflow And Rules

This file summarizes active workflow rules for recovery.

Canonical rules live in core and governance documents. This file should link to them instead of redefining them in full.

## Branch Flow

Current Blueprint flow:

```text
main
  -> develop
  -> docs/<scope> or fix/<scope>
  -> PR into develop
  -> release PR into main
```

`main` is release-ready public state.

`develop` is integration state for unreleased framework work.

## Self-Hosting Rule

Blueprint develops by using Blueprint.

New rules should be applied to this repository on `develop` before they are presented as release-ready on `main`.

Canonical rule owner: `governance/docs/engineering-governance.md`.

## PR Rules

Meaningful PRs use:

- Problem;
- Solution;
- Scope;
- Validation;
- Risks;
- Follow-ups.

One PR should have one scope.

## Current Layer Order

Recommended build order:

1. Bootstrap public repository presentation.
2. Core contracts.
3. Governance standards.
4. Project Memory structure.
5. Recovery templates.
6. Source coverage and relationship mapping.
7. Complete product map.
8. Project Memory templates.
9. Feature lifecycle templates.
10. PR handoff templates.
11. Guardian templates.
12. Checklists.
13. Sanitized examples.
14. Release PR into `main`.

## Canonical References

- Agent contract: `core/AGENTS.md`
- Task routing: `core/TASK_PROCESS_ROUTER.md`
- Feature lifecycle: `core/FEATURE_LIFECYCLE_STANDARD.md`
- PR handoff: `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md`
- Security: `core/SECURITY.md`
- Governance index: `governance/docs/governance-index.md`
- Git policy: `governance/docs/git-policy.md`
- PR standard: `governance/docs/pr-standard.md`
- Verification: `governance/docs/verification-standard.md`
- Documentation: `governance/docs/documentation-standard.md`
- ADR policy: `governance/docs/adr-policy.md`
- Recovery templates: `templates/recovery/README.md`
- Complete product map: `PRODUCT_MAP.md`
- Project Memory templates: `templates/project-memory/README.md`
- Feature Lifecycle templates: `templates/feature-lifecycle/README.md`
- Source coverage: `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md`
- System relationship map: `memory/project-kb/12_SYSTEM_RELATIONSHIP_MAP.md`
