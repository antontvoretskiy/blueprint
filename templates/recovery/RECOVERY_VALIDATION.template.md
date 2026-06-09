# <PROJECT_NAME> Recovery Validation

Status: Manual validation template.
Repository: `<OWNER>/<REPO>`
Branch: `<CURRENT_BRANCH>`
Validator: `<NAME_OR_ROLE>`
Date: `<YYYY-MM-DD>`

This template checks whether a fresh session can recover project state from repository files.

## Inputs

Read:

1. `AGENTS.md`
2. `project-kb/00_INDEX.md`
3. `project-kb/08_CURRENT_STATE.md`
4. `project-kb/05_IMPLEMENTATION_STATUS.md`
5. `project-kb/10_REFERENCE.md`
6. `TASK_PROCESS_ROUTER.md`

Add owner documents when the task touches governance, architecture, feature lifecycle, release, or validation.

## Validation Matrix

| Check | Expected evidence | Result |
| --- | --- | --- |
| Repository identity is clear | Remote and repository name match the task | `<PASS_FAIL_OR_NOT_RUN>` |
| Branch role is clear | Current branch and target branch are known | `<PASS_FAIL_OR_NOT_RUN>` |
| Current state is recoverable | `08_CURRENT_STATE.md` explains the recovery point | `<PASS_FAIL_OR_NOT_RUN>` |
| Included state is accurate | `05_IMPLEMENTATION_STATUS.md` matches repository contents | `<PASS_FAIL_OR_NOT_RUN>` |
| Reference map is usable | `10_REFERENCE.md` points to owner documents | `<PASS_FAIL_OR_NOT_RUN>` |
| Next work is routable | `TASK_PROCESS_ROUTER.md` identifies the workflow | `<PASS_FAIL_OR_NOT_RUN>` |
| Planned work is separated | Planned items are not described as included | `<PASS_FAIL_OR_NOT_RUN>` |
| Clean-start brief is temporary | Brief links back to canonical memory and owner docs | `<PASS_FAIL_OR_NOT_RUN>` |
| Old chat is not required | Recovery can complete from repository files | `<PASS_FAIL_OR_NOT_RUN>` |

Use `PASS`, `FAIL`, or `NOT RUN: <reason>`.

## Recovery Summary

```text
Repository:
Branch:
Current recovery point:
Included state:
Not included:
Next recommended work:
Applicable owner documents:
```

## Failure Handling

If any required check fails:

1. Stop implementation.
2. Identify the missing or conflicting owner document.
3. Update Project Memory or the owner document in a scoped PR.
4. Re-run recovery validation.

Do not compensate for broken recovery by relying on old chat history.
