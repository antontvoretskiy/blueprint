# Blueprint Quickstart

Use this quickstart to apply Blueprint to another repository without relying
on old chat history.

Blueprint currently has no installer. Adoption is a deliberate copy-and-adapt
process using repository files.

## Before You Start

Confirm:

- the target repository identity;
- whether source-reference repositories are read-only;
- whether the target repository uses `main` only or `main` plus an integration branch;
- whether you need minimal or full Blueprint adoption.

## Ten-Minute Adoption Path

1. Read the public overview in [README](../README.md).
2. Read the product boundary in [Product map](../PRODUCT_MAP.md).
3. Choose an adoption shape in [Adaptation guide](../ADAPTATION_GUIDE.md).
4. Copy the minimal owner set or full owner set from the adaptation copy map.
5. Replace placeholders with target-repository names and paths.
6. Create or update Project Memory from [Project Memory templates](../templates/project-memory/README.md).
7. Document the branch model in the target Git policy and Project Memory.
8. Run a fresh-session recovery check.
9. Validate the adaptation with the target repository checklist.
10. Open one scoped PR for the adoption baseline.

## Minimal Adoption

Use minimal adoption when the repository needs recovery, task routing, branch
policy, PR handoff, and validation before adding the full template set.

Start from:

- [Agent operating contract](../core/AGENTS.md);
- [Task process router](../core/TASK_PROCESS_ROUTER.md);
- [PR handoff and clean start standard](../core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md);
- [Governance index](../governance/docs/governance-index.md);
- [Git policy](../governance/docs/git-policy.md);
- [PR standard](../governance/docs/pr-standard.md);
- [Verification standard](../governance/docs/verification-standard.md);
- selected [Project Memory templates](../templates/project-memory/README.md).

## Full Adoption

Use full adoption when the repository needs feature lifecycle, Guardian review,
decisions, task history, clean-start templates, and checklists.

Add:

- [Feature lifecycle standard](../core/FEATURE_LIFECYCLE_STANDARD.md);
- complete [governance docs](../governance/docs/governance-index.md);
- complete [Project Memory templates](../templates/project-memory/README.md);
- [Guardian templates](../templates/guardian/README.md);
- [Recovery templates](../templates/recovery/README.md);
- [Checklists](../checklists/README.md).

## Recovery Test

After copying files, start a new AI session and ask:

```text
Read this repository's recovery path and tell me:
1. current project state;
2. current branch and release status;
3. latest validated work;
4. next recommended task;
5. files I should read before making changes.

Use repository files as the source of truth.
```

If the answer requires old chat history, the adoption is not complete.

## Validation

For a first adoption PR, report:

```text
- git diff --check: PASS or FAIL
- manual recovery check: PASS or FAIL
- installation checklist: PASS or FAIL
- private-state scan: PASS or FAIL
```

Use `NOT RUN` or `N/A` when a check does not run or does not apply.
