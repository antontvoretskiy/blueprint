# Blueprint Adaptation Guide

This guide explains how to apply Blueprint to another repository.

Use it with `BUNDLE_MANIFEST.md`, `templates/**`, `checklists/**`, and the AI product example.

## Public Repository Model

The public Blueprint repository exposes `main` as the release-ready distribution branch.

Maintainers may use local or private integration branches before publishing a release, but those branches are not required for public adoption.

Adopting repositories may choose either:

| Model | Use when | Branch shape |
| --- | --- | --- |
| Main-only | Small teams, early adoption, or public framework distribution | `main` plus short-lived scoped branches |
| Main plus integration | Teams that need a staging branch before release | `main`, `develop`, and short-lived scoped branches |

Blueprint governs both models. The adopting repository must document which model it uses in its Git policy and Project Memory.

## Adaptation Goal

After adaptation, a repository should answer:

- what rules govern the project;
- where durable project memory lives;
- how a new session recovers state;
- which task level applies;
- which branch family owns the work;
- what makes a PR ready;
- when memory must be updated;
- when old chat context can be discarded.

## Installation Shape

### Minimal

Use minimal installation for small teams or early adoption.

Minimum owner set:

```text
AGENTS.md
TASK_PROCESS_ROUTER.md
PR_HANDOFF_AND_CLEAN_START_STANDARD.md
docs/governance-index.md
docs/git-policy.md
docs/pr-standard.md
docs/verification-standard.md
project-kb/00_INDEX.md
project-kb/05_IMPLEMENTATION_STATUS.md
project-kb/08_CURRENT_STATE.md
project-kb/10_REFERENCE.md
project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md
```

### Full

Use full installation when the repository needs feature lifecycle, decisions, task history, clean start, Guardian templates, and checklists.

Full installation adds:

- `FEATURE_LIFECYCLE_STANDARD.md`;
- `SECURITY.md`;
- complete governance docs;
- complete Project Memory files;
- Guardian validation scenarios;
- reusable templates;
- checklists.

## Adaptation Steps

1. Define repository identity.
2. Choose minimal or full installation.
3. Copy the selected Blueprint assets.
4. Replace placeholders with project-specific names and paths.
5. Register rule owners in the governance index.
6. Map modules to branch families.
7. Create initial Project Memory.
8. Run recovery from a new session.
9. Run validation checks.
10. Open one scoped PR for the adaptation.

## Minimal Copy Map

Use this map when a repository wants the smallest working Blueprint adoption.

| Blueprint source | Target in adopter repository |
| --- | --- |
| `core/AGENTS.md` | `AGENTS.md` |
| `core/TASK_PROCESS_ROUTER.md` | `TASK_PROCESS_ROUTER.md` |
| `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | `PR_HANDOFF_AND_CLEAN_START_STANDARD.md` |
| `governance/docs/governance-index.md` | `docs/governance-index.md` |
| `governance/docs/git-policy.md` | `docs/git-policy.md` |
| `governance/docs/pr-standard.md` | `docs/pr-standard.md` |
| `governance/docs/verification-standard.md` | `docs/verification-standard.md` |
| `templates/project-memory/00_INDEX.template.md` | `project-kb/00_INDEX.md` |
| `templates/project-memory/05_IMPLEMENTATION_STATUS.template.md` | `project-kb/05_IMPLEMENTATION_STATUS.md` |
| `templates/project-memory/08_CURRENT_STATE.template.md` | `project-kb/08_CURRENT_STATE.md` |
| `templates/project-memory/10_REFERENCE.template.md` | `project-kb/10_REFERENCE.md` |
| `templates/recovery/RECOVERY_PATH.template.md` | `project-kb/current/RECOVERY_PATH.md` or a linked section in `project-kb/00_INDEX.md` |
| `templates/recovery/CLEAN_START_BRIEF.template.md` | `project-kb/current/CLEAN_START_BRIEF.md` |
| `memory/project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md` | `project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md` |

After copying, replace placeholders, remove irrelevant sections, and make each target file truthful for the adopter repository.

## Full Copy Map

Use the full map when the repository needs feature lifecycle, decisions, task history, Guardian review, recovery validation, and checklists.

| Blueprint source | Target in adopter repository |
| --- | --- |
| `core/FEATURE_LIFECYCLE_STANDARD.md` | `FEATURE_LIFECYCLE_STANDARD.md` |
| `core/SECURITY.md` | `SECURITY.md` or a linked project security owner |
| `governance/docs/engineering-governance.md` | `docs/engineering-governance.md` |
| `governance/docs/documentation-standard.md` | `docs/documentation-standard.md` |
| `governance/docs/adr-policy.md` | `docs/adr-policy.md` |
| `templates/project-memory/*.template.md` | `project-kb/*.md` |
| `templates/feature-lifecycle/*.template.md` | `project-kb/features/<feature-name>/*.md` |
| `templates/pr-handoff/*.template.md` | `project-kb/templates/pr-handoff/*.md` or PR-local handoff docs |
| `templates/guardian/*.template.md` | `project-kb/guardian/*.md` or linked Guardian owner docs |
| `templates/recovery/*.template.md` | `project-kb/current/*.md` |
| `checklists/*.md` | `checklists/*.md` |
| `examples/ai-product/*.md` | Reference only; do not copy as project state |

Examples explain adaptation patterns. They are not canonical rule owners for the adopter repository.

## First Adoption PR

The first adoption PR should be intentionally small.

Recommended scope:

- repository identity;
- branch model;
- minimal owner documents;
- initial Project Memory;
- recovery prompt;
- installation checklist result.

Do not combine first adoption with product implementation, refactoring, dependency changes, or automation.

Suggested PR title:

```text
docs: adopt blueprint governance baseline
```

Suggested validation:

```text
git diff --check
manual recovery check from a fresh AI chat
installation checklist
forbidden private-state scan
```

## Placeholder Rules

Replace placeholders such as:

- `<PROJECT_NAME>`;
- `<OWNER>/<REPO>`;
- `<DOMAIN_A>`;
- `<DOMAIN_B>`;
- `<PROJECT_SPECIFIC_MODULE>`;
- `<PROJECT_SPECIFIC_MILESTONE>`.

Do not copy private product state, private release history, or private PR numbers into the adapted repository.

## Branch Mapping Example

Choose this map only after selecting the repository branch model.

| Project area | Example path | Branch family |
| --- | --- | --- |
| Product surface | `apps/web/**` | `feature/web-*` |
| API surface | `apps/api/**` | `feature/api-*` |
| Model assets | `models/**` | `feature/model-*` |
| Prompt assets | `prompts/**` | `feature/prompt-*` |
| Evaluation assets | `evals/**` | `feature/eval-*` |
| Documentation | `docs/**` | `docs/*` |
| Project Memory | `project-kb/**` | `docs/*` |

## Adaptation Acceptance

Adaptation is acceptable when:

- repository identity is explicit;
- branch model maps to architecture;
- Project Memory can recover current state;
- rule owners are not duplicated;
- planned work is not described as implemented;
- validation evidence is recorded;
- clean start works after merge;
- private source data is not present.
