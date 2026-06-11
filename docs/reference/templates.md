# Template Reference

Blueprint templates are reusable starting points for adopter repositories.

Templates are not rule owners by themselves. The target repository must adapt
them, replace placeholders, and make the resulting files truthful.

## Template Families

| Family | Path | Use when |
| --- | --- | --- |
| Project Memory | [templates/project-memory](../../templates/project-memory/README.md) | A repository needs durable recovery files |
| Feature Lifecycle | [templates/feature-lifecycle](../../templates/feature-lifecycle/README.md) | Meaningful feature work needs specification, clarification, plan, and tasks |
| PR handoff | [templates/pr-handoff](../../templates/pr-handoff/README.md) | A PR needs reviewable scope, validation, risks, and clean-start notes |
| Guardian | [templates/guardian](../../templates/guardian/README.md) | A change needs scope, memory, architecture, PR, or release checks |
| Recovery | [templates/recovery](../../templates/recovery/README.md) | A repository needs fresh-session recovery and clean-start briefs |

## When To Use Each Family

| Need | Template family |
| --- | --- |
| Recover current state in a new session | Project Memory and Recovery |
| Start a meaningful feature safely | Feature Lifecycle |
| Validate scope and claims before review | Guardian |
| Prepare a PR for review | PR handoff |
| Close a merge without old-chat dependency | PR handoff and Recovery |

## Copy Rules

When copying templates into another repository:

1. Copy only the template family needed for the scope.
2. Replace placeholders such as `<PROJECT_NAME>` and `<OWNER>/<REPO>`.
3. Remove irrelevant sections.
4. Link the adapted file from that repository's reference map.
5. Do not copy private product state or private release history.
6. Do not describe template content as implemented product behavior.

## Placeholder Rules

Use placeholder names that are explicit and portable:

```text
<PROJECT_NAME>
<OWNER>/<REPO>
<DOMAIN_A>
<DOMAIN_B>
<PROJECT_SPECIFIC_MODULE>
<PROJECT_SPECIFIC_MILESTONE>
```

Do not use real private names as placeholders.

## Validation

Template changes should pass:

- manifest path checks;
- template index checks;
- markdown link checks;
- documentation truthfulness review.

In this repository, `make quality` runs the automated parts of those checks.
