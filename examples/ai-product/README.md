# AI Product Adoption Example

Status: Example asset.
Version: v0.3.0.
Type: Sanitized adoption example.

This example shows how a hypothetical AI product repository can adopt Blueprint as its repository operating framework.

It demonstrates governance, Project Memory, recovery, Guardian checks, branch governance, Feature Lifecycle, PR Lifecycle, checklists, and clean start without adding product implementation.

## What This Example Shows

| Area | Demonstrated by |
| --- | --- |
| Repository identity | A clear project name, owner, branches, and module map |
| Governance | One owner per rule through the governance index |
| Project Memory | Compact current state, implementation status, decisions, task history, and references |
| Recovery | A new session can recover from repository files |
| Guardian checks | Work is checked for repo identity, scope, boundary, evidence, and handoff readiness |
| Branch governance | Branch names map to one project layer |
| Feature Lifecycle | Meaningful changes use specification, clarification, plan, and tasks |
| PR Lifecycle | One PR has one scope, validation evidence, and handoff notes |

## What This Example Does Not Include

This example does not include:

- application source code;
- model implementation;
- prompt content;
- evaluation data;
- deployment infrastructure;
- private project state;
- private release history;
- private PR history;
- implementation claims.

The example can govern repositories that contain those areas, but it does not contain them.

## Example Repository Shape

```text
ai-product/
  AGENTS.md
  TASK_PROCESS_ROUTER.md
  FEATURE_LIFECYCLE_STANDARD.md
  PR_HANDOFF_AND_CLEAN_START_STANDARD.md
  SECURITY.md

  docs/
    governance-index.md
    engineering-governance.md
    git-policy.md
    pr-standard.md
    verification-standard.md
    documentation-standard.md
    adr-policy.md

  project-kb/
    00_INDEX.md
    05_IMPLEMENTATION_STATUS.md
    06_WORKFLOW_AND_RULES.md
    07_DECISIONS_LOG.md
    08_CURRENT_STATE.md
    09_TASK_HISTORY.md
    10_REFERENCE.md
    current/
      CLEAN_START_BRIEF.md
    architecture-decisions/
      GUARDIAN_ARCHITECTURE.md
    GUARDIAN_VALIDATION_SCENARIOS.md

  apps/
    web/
    api/
  models/
  prompts/
  evals/
```

The `apps/`, `models/`, `prompts/`, and `evals/` directories are adopter-owned project areas. Blueprint governs their workflow, but does not provide their implementation.

## Adoption Flow

1. Copy the minimal or full Blueprint bundle into the adopter repository.
2. Define repository identity in `AGENTS.md` and `project-kb/00_INDEX.md`.
3. Register rule owners in `docs/governance-index.md`.
4. Map project modules to branch families in `docs/git-policy.md`.
5. Create initial Project Memory files from `templates/project-memory/**`.
6. Add recovery and Guardian templates if the repository needs fresh-session handoff.
7. Run a recovery check from a new session before treating the adoption as complete.

## Files In This Example

| File | Purpose |
| --- | --- |
| `ADOPTION_MAP.md` | Maps Blueprint assets to an AI product repository |
| `BRANCH_GOVERNANCE_EXAMPLE.md` | Shows branch families and module ownership |
| `RECOVERY_WALKTHROUGH.md` | Shows how a new session restores project context |

## Canonical Owners

This example is not a rule owner.

Canonical rules live in:

- `PRODUCT_MAP.md`
- `ARCHITECTURE.md`
- `BUNDLE_MANIFEST.md`
- `core/**`
- `governance/docs/**`
- `memory/project-kb/**`
- `templates/**`
- `checklists/**`
