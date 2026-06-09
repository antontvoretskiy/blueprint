# Blueprint Decisions Log

This file records accepted decisions that affect recovery and future work.

Detailed architecture decisions may later move into ADR files when the decision needs more context.

## Accepted Decisions

| Date | Decision | Consequence |
| --- | --- | --- |
| 2026-06-09 | Use `develop` as the integration branch and `main` as release-ready public state | Feature PRs target `develop`; release PRs target `main` |
| 2026-06-09 | Keep source references read-only | Blueprint work must not modify reference repositories |
| 2026-06-09 | Keep public content free of reserved positioning and source-specific terms | Public scans are required before PRs |
| 2026-06-09 | Build layers manually before automation | CLI, installer, CI, and integrations stay planned until the manual framework is stable |
| 2026-06-09 | Keep one PR to one operating scope | Core, governance, memory, templates, examples, and checklists land separately |
| 2026-06-09 | Develop Blueprint by using Blueprint | New rules should be exercised on `develop` before release-ready state |

## Decision Rules

- Record decisions that affect future recovery.
- Keep entries short.
- Use ADRs for decisions that need context, alternatives, and consequences.
- Do not store private product decision history in Blueprint memory.
