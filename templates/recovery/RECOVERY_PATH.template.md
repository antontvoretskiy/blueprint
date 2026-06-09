# <PROJECT_NAME> Recovery Path

Status: Active recovery contract.
Owner: <OWNER_OR_TEAM>
Repository: `<OWNER>/<REPO>`

This document defines how a new contributor or agent recovers project state from repository files.

It is not a chat transcript and not a substitute for Project Memory.

## Repository Identity

| Field | Value |
| --- | --- |
| Repository | `<OWNER>/<REPO>` |
| Integration branch | `<INTEGRATION_BRANCH>` |
| Release branch | `<RELEASE_BRANCH>` |
| Current recovery owner | `<RECOVERY_OWNER>` |

Before doing work, verify:

- current working directory;
- `git remote -v`;
- current branch;
- target base branch;
- worktree status;
- ignored local files that may affect validation.

## Standard Recovery Order

Read these files in order:

```text
AGENTS.md
-> project-kb/00_INDEX.md
-> project-kb/08_CURRENT_STATE.md
-> project-kb/05_IMPLEMENTATION_STATUS.md
-> project-kb/10_REFERENCE.md
-> TASK_PROCESS_ROUTER.md
```

If the repository uses different paths, update this list and keep it linked from `project-kb/00_INDEX.md`.

## Optional Recovery Inputs

For governance work, also read:

```text
docs/governance-index.md
docs/git-policy.md
docs/pr-standard.md
docs/verification-standard.md
docs/documentation-standard.md
docs/adr-policy.md
```

For architecture work, also read:

```text
project-kb/07_DECISIONS_LOG.md
<ARCHITECTURE_OWNER_DOC>
<DOMAIN_OWNER_DOC>
```

For feature work, also read:

```text
<FEATURE_FOLDER>/FEATURE.md
<FEATURE_FOLDER>/PLAN.md
<FEATURE_FOLDER>/TASKS.md
```

## Recovery Decision

After reading the recovery inputs, decide:

| Question | Expected result |
| --- | --- |
| What repository is this? | `<OWNER>/<REPO>` |
| What branch should work target? | `<INTEGRATION_BRANCH>` unless release work is approved |
| What is included now? | Read from `project-kb/05_IMPLEMENTATION_STATUS.md` |
| What is the current recovery point? | Read from `project-kb/08_CURRENT_STATE.md` |
| What task router applies? | Read from `TASK_PROCESS_ROUTER.md` |
| What is explicitly excluded? | Read from current state, manifest, or owner docs |

If any answer is missing, stop and update Project Memory before implementation.

## Recovery Output

At the end of recovery, report:

```text
Repository:
Branch:
Base branch:
Current recovery point:
Included state:
Not included:
Next recommended work:
Applicable owner documents:
Validation needed before work:
```

## Failure Handling

Recovery fails when:

- old chat history is required to understand the current state;
- repository identity is unclear;
- current state and implementation status conflict;
- planned work is presented as included;
- no owner document exists for the next task;
- the next task cannot be routed.

When recovery fails, do not start implementation. Fix the recovery source first.
