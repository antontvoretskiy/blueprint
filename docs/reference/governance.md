# Governance Reference

Use this reference to find the canonical owner for Blueprint rules.

If this page and an owner document disagree, use the owner document and update
this page.

## Owner Map

| Need | Owner |
| --- | --- |
| Know which document owns a rule | [Governance index](../../governance/docs/governance-index.md) |
| Check repository identity or branch policy | [Git policy](../../governance/docs/git-policy.md) |
| Scope, title, and review a PR | [PR standard](../../governance/docs/pr-standard.md) |
| Report validation evidence | [Verification standard](../../governance/docs/verification-standard.md) |
| Keep docs truthful | [Documentation standard](../../governance/docs/documentation-standard.md) |
| Record architecture decisions | [ADR policy](../../governance/docs/adr-policy.md) |
| Understand engineering operating rules | [Engineering governance](../../governance/docs/engineering-governance.md) |

## Branch Model

The public Blueprint repository publishes release-ready state from `main`.

Maintainers may use local or private integration branches before publication.
Those branches are workflow details, not public distribution branches.

Adopting repositories may use:

- `main` only with short-lived scoped branches;
- `main` plus an integration branch.

The selected model must be documented in the adopter repository Git policy and
Project Memory.

## PR Shape

Meaningful PRs use:

```text
Problem
Solution
Scope
Validation
Risks
Follow-ups
```

One PR should have one review story. Split changes that mix governance,
templates, examples, release preparation, or automation unless the maintainer
explicitly approves the combined scope.

## Validation Language

Use these terms:

| Term | Meaning |
| --- | --- |
| `PASS` | The check ran and met expectations |
| `FAIL` | The check ran and found a problem |
| `NOT RUN` | The check was not run, with a reason |
| `N/A` | The check does not apply to this scope |

Do not claim validation passed unless command output, scan output, manual
inspection, cross-document review, or external confirmation supports it.

## Release Boundary

Release work is separate from feature, template, checklist, example, and
automation work.

Release PRs target `main`, must not add unrelated features, and must not add
automation unless automation is the explicit release scope.
