# AI Product Branch Governance Example

Status: Example asset.
Version: v0.3.0.
Type: Sanitized adoption example.

This example shows branch governance for a hypothetical AI product repository.

Canonical branch rules live in `governance/docs/git-policy.md`. This file only demonstrates how an adopter can map those rules to project areas.

## Long-Lived Branches

| Branch | Role |
| --- | --- |
| `main` | Release-ready branch |
| `develop` | Integration branch |
| `release/vX.Y.Z` | Release candidate branch |

## Branch Families

| Branch family | Allowed scope |
| --- | --- |
| `feature/web-*` | Product surface changes under `apps/web/**` |
| `feature/api-*` | API changes under `apps/api/**` |
| `feature/model-*` | Model asset or model interface changes under `models/**` |
| `feature/prompt-*` | Prompt asset changes under `prompts/**` |
| `feature/eval-*` | Evaluation asset changes under `evals/**` |
| `docs/*` | Governance, Project Memory, examples, and documentation |
| `fix/*` | Focused defect repair |
| `hotfix/*` | Urgent release repair |
| `chore/*` | Maintenance with no product behavior change |

## Module Mapping

| Path | Branch family | Notes |
| --- | --- | --- |
| `apps/web/**` | `feature/web-*` | Product surface work |
| `apps/api/**` | `feature/api-*` | API contract work |
| `models/**` | `feature/model-*` | Model asset or interface work |
| `prompts/**` | `feature/prompt-*` | Prompt asset work |
| `evals/**` | `feature/eval-*` | Evaluation work |
| `docs/**` | `docs/*` | Governance and public docs |
| `project-kb/**` | `docs/*` | Project Memory updates |

## Scoped Branch Examples

| Branch | Scope | Acceptable when |
| --- | --- | --- |
| `docs/adopt-blueprint` | Governance and Project Memory setup | No product implementation is changed |
| `feature/eval-report-format` | Evaluation artifact format | Changes stay inside `evals/**` and related docs |
| `feature/prompt-library-index` | Prompt asset navigation | Changes stay inside `prompts/**` and required memory refs |
| `fix/api-validation-error` | Focused API defect repair | The PR contains one repair scope and validation evidence |

## Boundary Rules

- A branch maps to one project layer.
- A branch name maps to a scope, not a person.
- Do not pre-create future feature branches.
- Ordinary work starts from `develop`.
- Release work reaches `main` through a release PR.
- One PR should use one branch family and one scope.
- Cross-layer PRs require explicit reason, owner review, and validation evidence.

## Memory Update Guidance

Update Project Memory only when durable state changes.

Typical memory updates:

- a new branch family becomes official;
- a module owner changes;
- a feature reaches implemented or released state;
- a recovery point changes;
- an accepted architecture decision changes the project map.

Do not update Project Memory for every small commit.
