# Blueprint Checklists

Asset: operational-checklists
Version: v0.3.0
Type: Checklist Bundle
Author: Blueprint Maintainers
Status: Included

These checklists provide manual acceptance criteria for repositories adopting Blueprint.

They do not replace owner documents, Project Memory, Guardian templates, PR handoff templates, or validation evidence. They help reviewers confirm that adoption and review steps are complete enough to proceed.

## Checklist Files

| Checklist | Purpose |
| --- | --- |
| `installation-checklist.md` | Confirms the required Blueprint files and owner links are installed |
| `recovery-checklist.md` | Confirms a new session can recover from repository files |
| `branch-governance-checklist.md` | Confirms branch, base, naming, and scope rules |
| `pr-readiness-checklist.md` | Confirms a PR is ready for review |
| `clean-start-checklist.md` | Confirms merged work can be continued from repository state |
| `system-use-case-validation-checklist.md` | Confirms Blueprint use cases and dependencies before packaging or release preparation |

## Result Terms

Use these result terms:

| Result | Meaning |
| --- | --- |
| `PASS` | The check was performed and met expectations |
| `FAIL` | The check was performed and found a blocker |
| `N/A` | The check does not apply to this scope |

Do not mark a checklist complete if a required owner document is missing, a public claim lacks evidence, or the next session would need old chat history to continue.

## Owner Documents

Checklist rules come from:

- `core/AGENTS.md`
- `core/TASK_PROCESS_ROUTER.md`
- `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md`
- `governance/docs/git-policy.md`
- `governance/docs/pr-standard.md`
- `governance/docs/verification-standard.md`
- `BUNDLE_MANIFEST.md`
- `memory/project-kb/00_INDEX.md`
- `memory/project-kb/08_CURRENT_STATE.md`
- `memory/project-kb/10_REFERENCE.md`
