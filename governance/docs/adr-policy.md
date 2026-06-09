# Blueprint ADR Policy

This policy defines how Blueprint records significant architecture and governance decisions.

An ADR is an Architecture Decision Record.

## Purpose

ADRs preserve durable decisions that affect Blueprint's structure, compatibility, governance, or public adoption path.

They prevent:

- important decisions being trapped in chat;
- repeated debate over accepted tradeoffs;
- hidden changes to layer boundaries;
- governance changes without rationale;
- versioned public assets changing without decision history.

## Ownership

This document owns:

- when ADRs are required;
- ADR location and naming;
- ADR lifecycle;
- ADR status terms;
- ADR review rules;
- deprecation and supersession rules;
- forbidden ADR patterns.

The governance index owns the rule authority map.

The documentation standard owns status language for ordinary docs.

## Dependencies

This policy depends on:

- `ARCHITECTURE.md` for layer boundaries;
- `BUNDLE_MANIFEST.md` for included, planned, and excluded assets;
- `governance/docs/governance-index.md` for rule ownership;
- `governance/docs/documentation-standard.md` for truthfulness and portability rules;
- `governance/docs/pr-standard.md` for PR reporting.

## ADR Philosophy

An ADR should explain why a durable decision exists.

The active rule still lives in its owner document.

Use ADRs for decisions that future maintainers will need to understand, not for every small edit.

## ADR Ownership Model

ADRs are historical decision records.

Owner documents define the current rule.

When an ADR changes active policy:

1. Add or update the ADR.
2. Update the owner document.
3. Update `governance/docs/governance-index.md` if ownership changes.
4. Report the relationship in the PR body.

## When To Use An ADR

Create an ADR when a decision:

- changes core framework boundaries;
- changes branch or release strategy;
- changes governance ownership;
- introduces optional tooling;
- changes template structure;
- affects portability;
- creates a long-term compatibility constraint;
- changes versioning rules;
- changes the public adoption model.

## Decisions That Do Not Require ADR

Small changes do not need ADRs:

- typo fixes;
- broken link repairs;
- scoped wording clarifications;
- formatting cleanup;
- manifest status corrections that do not change policy;
- examples that follow existing rules.

## ADR Location

When ADRs are added, use:

```text
governance/docs/adr/
```

Do not create ADRs in private project memory.

Do not store product-specific decision history in Blueprint ADRs.

## ADR Numbering Standard

Use date-first filenames:

```text
YYYY-MM-DD-short-kebab-title.md
```

Example:

```text
2026-06-09-use-develop-as-integration-branch.md
```

Date-first names keep ADRs sortable without requiring a central counter.

## ADR Template

Use this structure:

```text
# ADR: <Decision Title>

Date:
Status:
Scope:

## Context

## Decision

## Consequences

## Alternatives Considered

## Validation

## Follow-ups
```

## ADR Lifecycle

Standard lifecycle:

```text
Proposed
Accepted
Superseded
Deprecated
```

An ADR may be proposed in the same PR that introduces the decision.

Only accepted ADRs define current decision history.

## ADR Status Model

| Status | Meaning |
| --- | --- |
| Proposed | Under review, not yet accepted |
| Accepted | Current accepted decision |
| Superseded | Replaced by a newer ADR |
| Deprecated | No longer recommended, but kept for history |

Do not delete accepted ADRs only because the decision changed. Supersede them.

## ADR Review Rules

An ADR PR should explain:

- the decision scope;
- the owner documents affected;
- alternatives considered;
- compatibility impact;
- validation used;
- follow-up work.

Reviewers should check that the ADR does not redefine active rules without updating owner documents.

## ADR Deprecation And Supersession Rules

When replacing a decision:

1. Create or update the newer ADR.
2. Mark the older ADR as `Superseded`.
3. Link the older ADR to the newer ADR.
4. Update owner documents to reflect the current rule.
5. Update the governance index when ownership changes.

When a decision is no longer recommended but not replaced, mark it `Deprecated`.

## ADR Relationship To Other Governance Docs

| Area | Relationship |
| --- | --- |
| `ARCHITECTURE.md` | ADRs explain durable layer decisions; architecture states current boundaries |
| `BUNDLE_MANIFEST.md` | ADRs explain bundle changes; manifest states current included/planned/excluded status |
| `governance/docs/governance-index.md` | ADRs explain ownership changes; index states active owners |
| `governance/docs/pr-standard.md` | ADR PRs use the same PR body and validation rules |
| `governance/docs/documentation-standard.md` | ADRs follow the same portability and truthfulness rules |

## Portability Requirement

ADRs must be portable.

Do not include private source names, product incidents, product PR numbers, or private release history.

Use generic language and placeholders when an example is necessary.

## Future ADR Automation

Blueprint may add optional ADR linting later.

Automation should check this policy. It must not replace maintainer review of architecture and governance decisions.

## Forbidden ADR Patterns

Do not:

- use ADRs as task notes;
- store private source history in ADRs;
- change active policy only in an ADR;
- create ADRs for trivial wording fixes;
- delete accepted ADRs instead of superseding them;
- include private product names or private PR numbers;
- claim a decision is accepted before review.

## Review Checklist

Before merging an ADR change, confirm:

- ADR is required for the decision;
- filename follows the standard;
- status is valid;
- context and decision are clear;
- owner documents are updated when active rules change;
- governance index is updated when ownership changes;
- portability requirements are met;
- validation and follow-ups are explicit.
