# Blueprint Governance Index

This index is the authority map for Blueprint governance.

Use it to find the canonical owner for each rule. Summary documents may link to an owner, but they must not redefine the rule.

## Governance Principle

One rule should have one owner.

If two documents conflict, use this index to identify the canonical owner, then update summaries to point back to that owner.

## Authority Map

| Area | Canonical owner | Purpose |
| --- | --- | --- |
| Agent entrypoint | `core/AGENTS.md` | How agents start, recover, validate, and hand off work |
| Task routing | `core/TASK_PROCESS_ROUTER.md` | How work is classified before implementation |
| Feature lifecycle | `core/FEATURE_LIFECYCLE_STANDARD.md` | How meaningful changes move from request to PR |
| PR handoff and clean start | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | How PRs stay reviewable and recoverable |
| Security baseline | `core/SECURITY.md` | Portable security expectations |
| Engineering governance | `governance/docs/engineering-governance.md` | Engineering operating model and ownership |
| Git policy | `governance/docs/git-policy.md` | Branch roles, branch naming, merge flow |
| PR standard | `governance/docs/pr-standard.md` | PR title, body, scope, review, merge rules |
| Verification standard | `governance/docs/verification-standard.md` | Validation language and evidence requirements |
| Documentation standard | `governance/docs/documentation-standard.md` | Documentation truthfulness and status language |
| ADR policy | `governance/docs/adr-policy.md` | Architecture decision record rules |
| Contribution rules | `CONTRIBUTING.md` | Public contribution process and hygiene |
| Bundle composition | `BUNDLE_MANIFEST.md` | What is included, planned, and excluded |
| Architecture boundary | `ARCHITECTURE.md` | Core, extension, and example layer boundaries |

## Ownership Rules

- Add new operating rules to the canonical owner document.
- Link from summaries instead of duplicating full standards.
- Update this index when a new governance owner is created.
- Keep owner documents portable and sanitized.
- Do not store private product history in governance files.

## Conflict Resolution

When rules conflict:

1. Identify the affected area.
2. Use the authority map to find the owner.
3. Treat the owner document as canonical.
4. Update non-owner documents so they summarize or link instead of redefining.
5. Report the conflict and fix in the PR body.

## Change Requirements

Governance changes must include:

- one clear scope;
- affected owner document;
- validation evidence;
- impact on README, architecture, or manifest when public claims change;
- explicit exclusions.

Governance PRs target `develop` by default. Release PRs target `main`.
