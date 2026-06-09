# <PROJECT_NAME> Workflow And Rules

Status: <STATUS>.

This file summarizes active workflow rules for recovery.

Canonical rules live in owner documents. This file should link to them instead of redefining them in full.

## Branch Flow

Current project flow:

```text
<RELEASE_BRANCH>
  -> <INTEGRATION_BRANCH>
  -> <WORK_BRANCH_PATTERN>
  -> PR into <INTEGRATION_BRANCH>
  -> release PR into <RELEASE_BRANCH>
```

| Branch | Role |
| --- | --- |
| `<RELEASE_BRANCH>` | `<ROLE>` |
| `<INTEGRATION_BRANCH>` | `<ROLE>` |
| `<WORK_BRANCH_PATTERN>` | `<ROLE>` |

## Task Routing

Task routing owner: `<TASK_ROUTER_PATH>`.

Process levels:

| Level | Use for | Notes |
| --- | --- | --- |
| L0 | Trivial task | Keep procedure minimal |
| L1 | Documentation or small scoped change | Use owner and source-of-truth checks |
| L2 | Scoped layer change | Use layer boundaries and relevant validation |
| L3 | Meaningful feature implementation | Use Feature Lifecycle |
| L4 | Architecture, migration, release, or merge | Use full review gates |

## PR Rules

Meaningful PRs use:

- Problem;
- Solution;
- Scope;
- Validation;
- Risks;
- Follow-ups.

One PR should have one scope.

## Current Build Or Work Order

1. `<STEP_1>`
2. `<STEP_2>`
3. `<STEP_3>`

## Canonical References

- Agent contract: `<AGENT_ENTRYPOINT_PATH>`
- Task routing: `<TASK_ROUTER_PATH>`
- Feature lifecycle: `<FEATURE_LIFECYCLE_PATH>`
- PR handoff: `<PR_HANDOFF_PATH>`
- Security: `<SECURITY_PATH>`
- Governance index: `<GOVERNANCE_INDEX_PATH>`
- Git policy: `<GIT_POLICY_PATH>`
- PR standard: `<PR_STANDARD_PATH>`
- Verification: `<VERIFICATION_STANDARD_PATH>`
- Documentation: `<DOCUMENTATION_STANDARD_PATH>`
- ADR policy: `<ADR_POLICY_PATH>`
