# Guardian Templates

Asset: guardian-templates
Version: v0.3.0
Type: Template Bundle
Author: Blueprint Maintainers
Status: Included

These templates provide reusable Guardian review artifacts for repositories adopting Blueprint.

Guardian is a process-control layer. It checks repository identity, scope, architecture boundaries, memory update need, PR readiness, and release readiness.

Guardian is not a service, not CI, not a separate agent, and not a replacement for tests, review, or validation evidence.

## Install Target

When installed into another repository, render these templates into a location owned by the adopting project, such as:

```text
project-kb/templates/guardian/
```

Blueprint keeps reusable templates under:

```text
templates/guardian/
```

## Template Files

| Template | Purpose |
| --- | --- |
| `REPOSITORY_GUARDIAN.template.md` | Repository identity, branch, base branch, and source-reference guard |
| `CHANGE_GUARDIAN.template.md` | Scope, allowed paths, forbidden paths, and public-claim guard |
| `ARCHITECTURE_GUARDIAN.template.md` | Layer boundary and non-goal guard |
| `MEMORY_GUARDIAN.template.md` | Project Memory and owner document update guard |
| `PR_GUARDIAN.template.md` | PR title, body, validation, and handoff guard |
| `RELEASE_GUARDIAN.template.md` | Release readiness guard before integration state moves to release-ready state |

## When To Use

Use Guardian templates for:

- L2 scoped layer changes;
- L3 meaningful feature work;
- L4 architecture, migration, PR, merge, or release work;
- public status changes;
- source-reference adaptation;
- any change where scope drift or false documentation claims are likely.

For L0 tasks, repository identity and `git diff --check` are usually enough.

For L1 tasks, use only the Guardian checks that match the changed owner document.

## Guardian Flow

```text
Repository Guardian
-> Change Guardian
-> Architecture Guardian
-> Memory Guardian
-> PR Guardian
-> Release Guardian when release state changes
```

Run only the layers required by task risk and process level.

## Adaptation Rules

1. Replace placeholders such as `<OWNER_REPO>`, `<BRANCH_NAME>`, and `<BASE_BRANCH>`.
2. Use `PASS`, `FAIL`, or `NOT RUN: <reason>` for each check.
3. Link to canonical owner documents instead of redefining their rules.
4. Keep included, planned, excluded, and released states distinct.
5. Record explicit exclusions for paths and layers.
6. Treat validation evidence as required for PR readiness.
7. Keep Guardian as process control, not product implementation.
