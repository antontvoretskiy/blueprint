# Blueprint Engineering Governance

This document defines the engineering operating model for Blueprint.

It explains how work moves through branches, PRs, validation, documentation, and release preparation without depending on chat history as durable state.

## Operating Model

Blueprint uses a repository-first model:

- rules live in versioned files;
- current claims must match repository contents;
- meaningful changes use scoped PRs;
- validation evidence is reported in the PR body;
- `develop` is the integration branch;
- `main` is release-ready public state.

## Engineering Principles

| Principle | Meaning |
| --- | --- |
| Repository first | Durable rules and state live in files, not only in chat |
| One owner per rule | Each rule has one canonical owner document |
| One PR, one scope | PRs should stay reviewable and recoverable |
| Planned is not included | Documentation must not claim future work as available |
| Manual before automation | Framework rules come before optional tooling |
| Sanitized by default | Portable docs must not leak private source details |
| Validation is evidence | Claims need commands, checks, or clear manual proof |

## Branch Model

Default flow:

```text
main
  -> develop
  -> docs/<scope> or fix/<scope>
  -> PR into develop
  -> release PR into main
```

`main` should only receive release-ready changes. Normal framework work goes through `develop`.

## Work Classification

Classify work with `core/TASK_PROCESS_ROUTER.md` before implementation.

Common classes:

- bootstrap docs;
- core contract;
- governance standard;
- Project Memory;
- template bundle;
- example project;
- checklist;
- release.

If a task crosses classes, split it unless the maintainer approves a combined PR.

## Documentation Ownership

Use `governance/docs/governance-index.md` to find the owner for each rule.

When adding or changing a rule:

1. Update the owner document.
2. Update summaries only when their public claims change.
3. Keep examples and implementation details out of owner documents unless they are generic.

## Validation Ownership

Use `governance/docs/verification-standard.md` for validation language.

Every meaningful PR should include:

- commands run;
- outcome for each command;
- scans run;
- checks not run and why;
- known risks.

## Release Ownership

Release work must be explicit.

A release PR should:

- target `main`;
- name the release version;
- summarize changes from `develop`;
- verify README, manifest, and architecture status;
- report validation;
- identify any known follow-ups.

Do not treat integration work on `develop` as a public release.

## Governance Non-Goals

Engineering governance does not provide:

- CI enforcement;
- package publishing;
- install automation;
- runtime behavior;
- external service integration.

Those may become optional extensions later, but they must not redefine core governance.
