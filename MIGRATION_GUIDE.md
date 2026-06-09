# Blueprint Migration Guide

This guide explains how to migrate an existing repository governance system into Blueprint.

Migration is an adaptation process, not a direct copy.

## Migration Principle

Preserve portable operating logic.

Remove private product state.

## Migration Inputs

Collect only the documents needed to understand:

- governance rules;
- task routing;
- branch policy;
- PR lifecycle;
- verification language;
- documentation policy;
- ADR policy;
- Project Memory shape;
- recovery flow;
- Guardian checks;
- clean-start rules.

Do not import product implementation, private memory, private incidents, private release history, or private PR timelines.

## Migration Steps

1. Inventory source documents.
2. Classify each source document as portable, template-only, example-only, or excluded.
3. Map each portable rule to one Blueprint owner document.
4. Convert stateful memory into templates.
5. Replace private names and paths with placeholders.
6. Remove product implementation references from core.
7. Update the coverage matrix.
8. Update the relationship map.
9. Run link, wording, and validation checks.
10. Open a scoped PR with migration evidence.

## Classification Table

| Source content | Blueprint action |
| --- | --- |
| Governance rule | Adapt into `governance/docs/**` or `core/**` |
| Task routing rule | Adapt into `core/TASK_PROCESS_ROUTER.md` |
| Feature lifecycle rule | Adapt into `core/FEATURE_LIFECYCLE_STANDARD.md` or templates |
| PR handoff rule | Adapt into `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` or templates |
| Project Memory state | Convert to template or current Blueprint memory when generic |
| Product release history | Exclude |
| Product implementation path | Replace with placeholder or exclude |
| Private incident or blocker | Exclude |

## Sanitization Checklist

Before migration PR review, confirm:

- private project names are removed;
- private domains are removed;
- private PR numbers are removed;
- private owners are removed;
- private incidents are removed;
- product-specific milestones are removed;
- product implementation paths are removed or replaced;
- status language distinguishes included, planned, example, template, and excluded.

## Migration Acceptance

Migration is acceptable when:

- every portable source rule has one Blueprint owner;
- every excluded area is documented as excluded;
- relationship maps explain how owners connect;
- recovery can proceed without old chat history;
- validation evidence is present;
- no private product state remains.
