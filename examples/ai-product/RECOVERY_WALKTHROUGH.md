# AI Product Recovery Walkthrough

Status: Example asset.
Version: v0.3.0.
Type: Sanitized adoption example.

This walkthrough shows how a fresh session can recover an AI product repository that adopted Blueprint.

Canonical recovery rules live in `core/AGENTS.md`, `memory/project-kb/00_INDEX.md`, and `templates/recovery/**`.

## Recovery Goal

A new session should understand:

- which repository it is in;
- which branch and scope are active;
- what is included, planned, and excluded;
- which task level applies;
- which owner documents control the work;
- what validation is required;
- whether Project Memory needs an update.

If the session needs old chat history to answer these questions, recovery has failed.

## Standard Recovery Path

```text
AGENTS.md
-> project-kb/00_INDEX.md
-> project-kb/08_CURRENT_STATE.md
-> project-kb/05_IMPLEMENTATION_STATUS.md
-> project-kb/10_REFERENCE.md
-> TASK_PROCESS_ROUTER.md
```

For governance changes, also read:

```text
docs/governance-index.md
-> relevant governance owner document
```

For meaningful feature work, also read:

```text
FEATURE_LIFECYCLE_STANDARD.md
-> project-kb/features/<feature-name>/
```

## Example Recovery Run

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Confirm repository identity | Current path, remote URL, branch, and status are recorded |
| 2 | Read the agent entrypoint | `AGENTS.md` defines the recovery path |
| 3 | Load Project Memory | `project-kb/00_INDEX.md` points to status, current state, and references |
| 4 | Classify the task | `TASK_PROCESS_ROUTER.md` selects L0-L4 procedure |
| 5 | Find the owner document | `docs/governance-index.md` identifies the canonical rule owner |
| 6 | Check branch scope | `docs/git-policy.md` maps branch family to paths |
| 7 | Apply Guardian checks | Repository, change, architecture, memory, and PR checks are completed as needed |
| 8 | Validate evidence | Commands, link checks, review notes, or manual evidence are recorded |
| 9 | Decide memory update | Durable state changes update Project Memory; chat-only notes do not |
| 10 | Prepare PR handoff | PR body, validation, risks, and follow-ups are clear |

## Recovery Evidence Table

| Question | Expected source |
| --- | --- |
| What project is this? | `project-kb/00_INDEX.md` |
| What is current? | `project-kb/08_CURRENT_STATE.md` |
| What is included? | `project-kb/05_IMPLEMENTATION_STATUS.md` |
| What documents matter? | `project-kb/10_REFERENCE.md` |
| What process level applies? | `TASK_PROCESS_ROUTER.md` |
| What branch is allowed? | `docs/git-policy.md` |
| What validation wording is allowed? | `docs/verification-standard.md` |
| What PR format is required? | `docs/pr-standard.md` |
| What clean-start work is required? | `PR_HANDOFF_AND_CLEAN_START_STANDARD.md` |

## Failure Signals

Recovery is not acceptable when:

- repository identity is guessed instead of checked;
- a task starts before the recovery path is read;
- branch scope is unclear;
- planned work is described as implemented;
- validation evidence is missing;
- Project Memory is stale after durable state changes;
- old chat history is required to continue.

## Clean Start

After merge:

1. PR handoff records what changed.
2. Validation evidence is preserved.
3. Project Memory is updated only if durable state changed.
4. The current recovery point is updated when needed.
5. The next session can start from the repository without old chat context.
