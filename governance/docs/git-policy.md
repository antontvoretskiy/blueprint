# Blueprint Git Policy

This policy defines branch roles, branch naming, and merge flow for Blueprint.

## Branch Roles

| Branch | Role |
| --- | --- |
| `main` | Release-ready public state |
| `develop` | Integration branch for unreleased framework work |
| `docs/<scope>` | Documentation or framework contract work |
| `fix/<scope>` | Small corrections or repair work |
| `chore/<scope>` | Repository maintenance without framework semantics |
| `release/vX.Y.Z` | Release preparation branch when needed |

`main` should not receive normal feature work directly.

## Default Flow

```text
main
  -> develop
  -> docs/<scope> or fix/<scope>
  -> PR into develop
  -> release PR into main
```

Create feature branches from `develop` unless the maintainer explicitly requests a release or hotfix branch.

## Branch Naming

Use names that describe the work, not the person.

Good examples:

- `docs/core-operating-contracts`
- `docs/governance-standards`
- `docs/project-memory-templates`
- `fix/manifest-links`
- `release/v0.2.0`

Avoid vague names, personal names, and work-in-progress labels.

## Scope Mapping

| Scope | Branch prefix |
| --- | --- |
| Core contracts | `docs/core-*` |
| Governance standards | `docs/governance-*` |
| Project Memory | `docs/memory-*` |
| Templates | `docs/templates-*` |
| Examples | `docs/examples-*` |
| Checklists | `docs/checklists-*` |
| Release preparation | `release/vX.Y.Z` |
| Small fixes | `fix/*` |

## Merge Rules

For integration PRs:

- base branch should be `develop`;
- squash merge is preferred;
- squash title should follow `CONTRIBUTING.md`;
- PR body should remain useful after merge.

For release PRs:

- base branch should be `main`;
- source branch should be `develop` or `release/vX.Y.Z`;
- release version must be clear;
- public claims must be revalidated.

## Protected Boundaries

Do not create branches in source-reference repositories.

Do not push private source-derived content into Blueprint.

Do not use `main` as a scratch branch.

Do not mix release preparation with unrelated framework changes.

## Cleanup

After a PR merges:

- sync the target branch locally;
- delete the feature branch when it is no longer needed;
- repeat relevant validation on the target branch;
- report the clean-start state.
