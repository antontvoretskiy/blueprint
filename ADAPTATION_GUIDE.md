# Blueprint Adaptation Guide

This guide explains how to apply Blueprint to another repository.

Use it with `BUNDLE_MANIFEST.md`, `templates/**`, `checklists/**`, and the AI product example.

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
