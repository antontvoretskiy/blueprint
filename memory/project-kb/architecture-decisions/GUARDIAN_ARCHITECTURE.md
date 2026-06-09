# Blueprint Guardian Architecture

Guardian is the process-control layer for Blueprint-governed work.

Guardian is not a runtime service, not CI, and not a separate agent. It is a set of checks that protect repository boundaries, scope, and truthfulness.

## Guardian Layers

| Layer | Purpose |
| --- | --- |
| Repository Guardian | Confirms repository identity, branch, base branch, and working tree state |
| Scope Guardian | Checks allowed and forbidden paths |
| Architecture Guardian | Checks layer boundaries and non-goals |
| Memory Guardian | Checks whether durable state needs a memory update |
| PR Guardian | Checks PR title, body, validation, risks, and follow-ups |
| Release Guardian | Checks readiness before moving integration state to release-ready state |

## Guardian Inputs

Guardian checks use:

- `core/AGENTS.md`;
- `core/TASK_PROCESS_ROUTER.md`;
- `ARCHITECTURE.md`;
- `BUNDLE_MANIFEST.md`;
- `CONTRIBUTING.md`;
- `governance/docs/governance-index.md`;
- `governance/docs/verification-standard.md`;
- `memory/project-kb/08_CURRENT_STATE.md`.

## Guardian Checks

Guardian should check:

- repository identity;
- branch and base branch;
- dirty worktree;
- allowed paths;
- forbidden paths;
- planned versus included claims;
- private source-term leakage;
- validation evidence;
- PR body structure;
- clean-start readiness.

## Guardian Non-Goals

Guardian does not replace:

- tests;
- CI;
- security review;
- human review;
- release approval;
- runtime validation.

Guardian protects process boundaries. It does not prove product behavior.
