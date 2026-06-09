# Blueprint Governance Index

This index is the authority map for Blueprint governance.

Use it to find the canonical owner for each rule. Summary documents may link to an owner, but they must not redefine the rule.

## Purpose

The governance index prevents duplicate ownership.

It answers:

- which document owns each rule;
- which document wins when rules conflict;
- which naming standard applies;
- which documents depend on each other;
- when this index must be updated.

## Governance Principle

One rule should have one owner.

If two documents conflict, use this index to identify the canonical owner, then update summaries to point back to that owner.

## Governance Levels

Blueprint governance is organized into levels:

| Level | Purpose | Current status |
| --- | --- | --- |
| Public entrypoint | Explain what Blueprint is and how to start | Included |
| Product boundary | Define what belongs inside and outside Blueprint | Included |
| Architecture boundary | Define core, extension, and example layers | Included |
| Core contracts | Define agent entry, task routing, lifecycle, handoff, security baseline | Included |
| Governance standards | Define branch, PR, verification, documentation, ADR, and engineering rules | Included |
| Project Memory materials | Define recovery-oriented state files | Planned |
| Templates | Provide reusable installation artifacts | Planned |
| Examples | Show adoption patterns | Planned |
| Checklists | Provide acceptance criteria | Planned |

Planned levels are not included until their files exist in the repository.

## Source-Of-Truth Ownership Map

| Area | Canonical owner | Purpose |
| --- | --- | --- |
| Public positioning | `README.md` | Landing page, promise, status, quick start |
| Product definition | `OPEN_SOURCE_SPEC.md` | Scope, audience, problem, non-goals |
| Architecture boundary | `ARCHITECTURE.md` | Core, extension, and example layers |
| Bundle composition | `BUNDLE_MANIFEST.md` | Included, planned, and excluded content |
| Contribution rules | `CONTRIBUTING.md` | Public contribution process and hygiene |
| Agent entrypoint | `core/AGENTS.md` | How agents start, recover, validate, and hand off work |
| Task routing | `core/TASK_PROCESS_ROUTER.md` | How work is classified before implementation |
| Feature lifecycle | `core/FEATURE_LIFECYCLE_STANDARD.md` | How meaningful changes move from request to PR |
| PR handoff and clean start | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | How PRs stay reviewable and recoverable |
| Security baseline | `core/SECURITY.md` | Portable security expectations |
| Engineering governance | `governance/docs/engineering-governance.md` | Engineering operating model and ownership |
| Git policy | `governance/docs/git-policy.md` | Repository identity, branches, commits, merge, cleanup |
| PR standard | `governance/docs/pr-standard.md` | PR title, body, scope, review, merge rules |
| Verification standard | `governance/docs/verification-standard.md` | Validation language and evidence requirements |
| Documentation standard | `governance/docs/documentation-standard.md` | Documentation truthfulness, lifecycle, and portability |
| ADR policy | `governance/docs/adr-policy.md` | Architecture decision record rules |

## Planned Ownership Map

These areas are planned, but they are not active owners until their files are added:

| Planned area | Intended owner pattern |
| --- | --- |
| Project Memory index | `memory/project-kb/00_INDEX.md` |
| Implementation status template | `memory/project-kb/05_IMPLEMENTATION_STATUS.md` |
| Current recovery state | `memory/project-kb/08_CURRENT_STATE.md` |
| Reference map | `memory/project-kb/10_REFERENCE.md` |
| Guardian architecture | `memory/project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md` |
| Template bundles | `templates/**` |
| Example projects | `examples/**` |
| Checklists | `checklists/**` |

Do not cite planned owners as included assets before the files exist.

## Authority Resolution

When rules conflict:

1. Identify the affected area.
2. Use the ownership map to find the canonical owner.
3. Treat the owner document as active policy.
4. Update non-owner documents so they summarize or link instead of redefining.
5. Report the conflict and fix in the PR body.

If no owner exists, add one in the same PR that introduces the rule.

## Naming Authority Map

| Naming area | Owner |
| --- | --- |
| Repository name and public description | `README.md`, `OPEN_SOURCE_SPEC.md` |
| Version numbers | `CONTRIBUTING.md`, release PR body |
| Branch names | `governance/docs/git-policy.md` |
| Commit titles | `governance/docs/git-policy.md`, `CONTRIBUTING.md` |
| PR titles | `governance/docs/pr-standard.md`, `CONTRIBUTING.md` |
| ADR filenames | `governance/docs/adr-policy.md` |
| Documentation status labels | `governance/docs/documentation-standard.md` |
| Validation terms | `governance/docs/verification-standard.md` |

Do not introduce a new naming standard in a summary document.

## Dependency Graph

```text
README.md
  -> OPEN_SOURCE_SPEC.md
  -> ARCHITECTURE.md
  -> BUNDLE_MANIFEST.md
  -> CONTRIBUTING.md
  -> governance/docs/governance-index.md

governance/docs/governance-index.md
  -> governance/docs/engineering-governance.md
  -> governance/docs/git-policy.md
  -> governance/docs/pr-standard.md
  -> governance/docs/verification-standard.md
  -> governance/docs/documentation-standard.md
  -> governance/docs/adr-policy.md

core/AGENTS.md
  -> core/TASK_PROCESS_ROUTER.md
  -> core/FEATURE_LIFECYCLE_STANDARD.md
  -> core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md
  -> core/SECURITY.md
```

Dependency direction means "summarizes, links to, or relies on".

It does not mean the dependent document may redefine the owner.

## Conflict Prevention Rules

- Add rules to owner documents, not summaries.
- Link from summaries instead of duplicating full standards.
- Update this index when a new governance owner is created.
- Keep owner documents portable and sanitized.
- Do not store private product history in governance files.
- Keep planned layers clearly marked as planned until files exist.

## Governance Change Rule

Governance changes must include:

- one clear scope;
- affected owner document;
- validation evidence;
- impact on README, architecture, or manifest when public claims change;
- explicit exclusions.

Governance PRs target `develop` by default.

Release PRs target `main`.

## Known Governance Gaps

Current planned gaps:

- Project Memory files are planned for a later phase.
- Template bundles are planned for a later phase.
- Example projects are planned for a later phase.
- Checklists are planned for a later phase.
- Optional automation is not included.

These gaps should not be described as included assets.

## Update Process

Update this index when:

- a new rule owner is added;
- a rule owner moves;
- a new layer becomes included;
- a planned owner becomes real;
- a conflict is resolved by changing ownership;
- public naming authority changes.

Do not update this index for minor wording fixes that do not affect ownership.

## Review Checklist

Before merging governance index changes, confirm:

- each listed current owner file exists;
- planned owners are clearly marked as planned;
- naming authorities point to one owner;
- dependencies do not imply duplicate ownership;
- public status agrees with `BUNDLE_MANIFEST.md`;
- no private source details are included.
