# Blueprint ADR Policy

This policy defines how Blueprint records significant architecture and governance decisions.

An ADR is an Architecture Decision Record.

## When To Use An ADR

Create an ADR when a decision:

- changes core framework boundaries;
- changes branch or release strategy;
- changes governance ownership;
- introduces optional tooling;
- changes template structure;
- affects portability;
- creates a long-term compatibility constraint.

Small wording fixes, typo fixes, and scoped documentation clarifications do not need ADRs.

## ADR Location

When ADRs are added, use:

```text
governance/docs/adr/
```

Do not create ADRs in private project memory.

Do not store product-specific decision history in Blueprint ADRs.

## ADR Filename

Use:

```text
YYYY-MM-DD-short-kebab-title.md
```

Example:

```text
2026-06-09-use-develop-as-integration-branch.md
```

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

## ADR Status

Allowed statuses:

- Proposed;
- Accepted;
- Superseded;
- Deprecated.

Only accepted ADRs define current policy.

## Portability Requirement

ADRs must be portable.

Do not include private source names, product incidents, product PR numbers, or private release history.

Use generic language and placeholders when an example is necessary.

## Relationship To Governance Index

If an ADR changes a rule owner or introduces a new owner document, update `governance/docs/governance-index.md` in the same PR.

The ADR explains why the decision happened. The owner document defines the active rule.
