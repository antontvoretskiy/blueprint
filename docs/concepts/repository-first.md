# Repository-First Development

Blueprint is built around one rule:

```text
The repository is the source of truth.
```

Chat can help execution, but durable rules, current state, decisions,
validation evidence, and recovery paths must live in versioned files.

## Why This Matters

AI-assisted projects lose continuity when:

- current state exists only in a chat;
- a new session cannot tell which branch or release is current;
- rules are repeated with small differences across files;
- planned work is described as implemented;
- PR handoff depends on the memory of one person or agent.

Blueprint moves that continuity into the repository.

## Durable State

Durable state belongs in:

- [Project Memory](../../memory/project-kb/00_INDEX.md);
- [Current state](../../memory/project-kb/08_CURRENT_STATE.md);
- [Implementation status](../../memory/project-kb/05_IMPLEMENTATION_STATUS.md);
- [Reference map](../../memory/project-kb/10_REFERENCE.md);
- [Task history](../../memory/project-kb/09_TASK_HISTORY.md).

These files are compact recovery owners. They should link to canonical
documents instead of copying every rule.

## Canonical Owners

Every rule should have one owner.

Examples:

| Rule area | Owner |
| --- | --- |
| Task routing | [Task process router](../../core/TASK_PROCESS_ROUTER.md) |
| Agent start gate | [Agent operating contract](../../core/AGENTS.md) |
| Branch policy | [Git policy](../../governance/docs/git-policy.md) |
| PR structure | [PR standard](../../governance/docs/pr-standard.md) |
| Validation language | [Verification standard](../../governance/docs/verification-standard.md) |
| Documentation status | [Documentation standard](../../governance/docs/documentation-standard.md) |

Summaries can route to owners. They must not redefine owners.

## Recovery Loop

Blueprint recovery follows this shape:

```text
request
-> repository identity
-> current state
-> task routing
-> owner document
-> scoped work
-> validation evidence
-> PR handoff
-> Project Memory update
-> clean start
```

Small tasks should not pay the cost of full recovery. The task router defines
the process level and recovery budget.

## Truthfulness Rule

A public claim is valid only when:

- an owner document supports it;
- repository contents support it;
- validation evidence supports it;
- the PR reports the evidence clearly.

If a capability is planned, label it as planned. If it belongs outside
Blueprint core, label it as excluded.
