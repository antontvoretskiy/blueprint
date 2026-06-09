# AI Product Adoption Map

Status: Example asset.
Version: v0.3.0.
Type: Sanitized adoption example.

This map shows how an AI product repository can install Blueprint documents while keeping product implementation outside Blueprint.

## Blueprint Asset Mapping

| Blueprint asset | Example adopter path | Purpose |
| --- | --- | --- |
| `core/AGENTS.md` | `AGENTS.md` | Agent entrypoint and recovery rules |
| `core/TASK_PROCESS_ROUTER.md` | `TASK_PROCESS_ROUTER.md` | Task classification and process levels |
| `core/FEATURE_LIFECYCLE_STANDARD.md` | `FEATURE_LIFECYCLE_STANDARD.md` | Meaningful feature lifecycle |
| `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | `PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | PR handoff and clean-start rules |
| `core/SECURITY.md` | `SECURITY.md` | Security baseline |
| `governance/docs/**` | `docs/**` | Governance standards |
| `templates/project-memory/**` | `project-kb/**` | Project Memory starter files |
| `templates/feature-lifecycle/**` | `project-kb/features/<feature>/` | Feature planning artifacts |
| `templates/guardian/**` | `project-kb/guardian/` or review notes | Guardian review artifacts |
| `templates/recovery/**` | `project-kb/current/` and recovery notes | Fresh-session recovery artifacts |
| `templates/pr-handoff/**` | PR description or handoff notes | PR review and handoff artifacts |
| `checklists/**` | `docs/checklists/` or PR review notes | Acceptance criteria |

## Example Project Areas

| Project area | Example path | Branch family | Memory owner |
| --- | --- | --- | --- |
| Product surface | `apps/web/**` | `feature/web-*` | `project-kb/domains/product-surface/` when needed |
| API surface | `apps/api/**` | `feature/api-*` | `project-kb/domains/api/` when needed |
| Model assets | `models/**` | `feature/model-*` | `project-kb/domains/model/` when needed |
| Prompt assets | `prompts/**` | `feature/prompt-*` | `project-kb/domains/prompt/` when needed |
| Evaluation assets | `evals/**` | `feature/eval-*` | `project-kb/domains/evaluation/` when needed |
| Governance docs | `docs/**` | `docs/*` | `project-kb/06_WORKFLOW_AND_RULES.md` |
| Project Memory | `project-kb/**` | `docs/*` | `project-kb/00_INDEX.md` |

## Process Level Examples

| Example task | Level | Required path |
| --- | --- | --- |
| Fix a broken documentation link | L0 | Identity check, owner lookup, link validation |
| Update a branch mapping table | L1 | Governance owner lookup, docs validation, memory update if durable state changed |
| Add an evaluation report format | L2 | Layer owner, allowed paths, validation evidence, PR handoff |
| Add a new user-facing evaluation workflow | L3 | Feature Lifecycle, Guardian review, PR handoff, memory update decision |
| Change repository governance or release policy | L4 | Full owner review, Guardian review, validation evidence, clean start |

## Source Of Truth In The Adopter Repository

| Question | Owner |
| --- | --- |
| What project is this? | `project-kb/00_INDEX.md` |
| What is implemented? | `project-kb/05_IMPLEMENTATION_STATUS.md` |
| What is the current recovery point? | `project-kb/08_CURRENT_STATE.md` |
| What rules apply? | `docs/governance-index.md` and owner documents |
| What branch family should be used? | `docs/git-policy.md` |
| Is Feature Lifecycle required? | `TASK_PROCESS_ROUTER.md` and `FEATURE_LIFECYCLE_STANDARD.md` |
| Is a memory update required? | `PR_HANDOFF_AND_CLEAN_START_STANDARD.md` and `project-kb/08_CURRENT_STATE.md` |

## Adoption Acceptance

The example adoption is acceptable when:

- repository identity is defined;
- branch families map to project areas;
- governance owners are registered;
- Project Memory has current status and references;
- recovery works from repository files;
- validation language is evidence-based;
- PR handoff can end old chat dependency after merge;
- product implementation remains outside Blueprint assets.
