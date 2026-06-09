# Blueprint Engineering Governance

This document defines the engineering operating model for Blueprint.

It explains how work moves through branches, PRs, validation, documentation, and release preparation without depending on chat history as durable state.

## Purpose

Engineering governance keeps Blueprint work scoped, traceable, and truthful.

It prevents:

- starting implementation before task classification;
- changing multiple layers in one PR;
- presenting planned work as included;
- separating code changes from their documentation impact;
- losing handoff state after merge;
- adding process without an owner document.

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

## One Responsibility Rule

Each task, branch, commit, and PR should have one primary responsibility.

One responsibility means:

- one layer;
- one review story;
- one validation story;
- one owner document when possible;
- explicit follow-ups for adjacent work.

When a task crosses responsibilities, split it before implementation unless maintainers approve a combined PR.

## Task Lifecycle

Standard lifecycle:

```text
request
identity check
task classification
scope decision
branch from develop
implementation
validation
PR
review
merge
post-merge recovery update
next branch from updated target
```

The lifecycle can be shorter for trivial fixes, but repository identity and scope must still be clear.

## Task Size And Decomposition

Decompose work when:

- it touches multiple layers;
- it creates both rules and examples;
- it changes public status and adds new assets;
- it requires different validation methods;
- it mixes release preparation with integration work;
- it would make review depend on old chat context.

Prefer a sequence of small PRs over one broad PR.

## Scope Boundaries

Blueprint has three product layers:

| Layer | Responsibility |
| --- | --- |
| Core Layer | Required portable contracts and governance primitives |
| Extension Layer | Optional tools or integrations that support adoption |
| Example Layer | Educational examples that demonstrate adoption patterns |

Core changes must not absorb optional tools, project-specific implementation, or examples.

Extension and example work must not redefine core rules.

## Branch Model

Default flow:

```text
main
  -> develop
  -> docs/<scope> or fix/<scope>
  -> PR into develop
  -> release PR into main
```

`main` should only receive release-ready changes.

Normal framework work goes through `develop`.

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

## Traceability Expectations

Meaningful changes should be traceable from:

```text
task request
  -> branch
  -> commit
  -> PR body
  -> validation evidence
  -> affected owner documents
  -> follow-ups
```

Traceability does not require heavy process for trivial fixes.

It does require that durable context ends up in the repository instead of only in chat.

## Validation Ownership

Use `governance/docs/verification-standard.md` for validation language.

Every meaningful PR should include:

- commands run;
- outcome for each command;
- scans run;
- checks not run and why;
- known risks.

## Governance Change Rule

When changing governance:

- identify the canonical owner;
- update the owner document;
- update the governance index if ownership changes;
- update public root docs only if public claims changed;
- validate for duplicate or conflicting rules;
- list excluded layers in the PR body.

Governance changes should not be bundled with unrelated templates, examples, or release preparation.

## Release Ownership

Release work must be explicit.

A release PR should:

- target `main`;
- name the release version;
- summarize changes from `develop`;
- verify README, manifest, and architecture status;
- report validation;
- identify known follow-ups.

Do not treat integration work on `develop` as a public release.

## Relationship To Project Implementation

Blueprint may govern projects that contain applications, services, infrastructure, models, templates, or domain-specific code.

Blueprint core does not contain those implementation layers.

If future examples show implementation paths, they must remain examples and must not redefine core governance.

## Relationship To Detailed Standards

| Topic | Detailed owner |
| --- | --- |
| Rule authority | `governance/docs/governance-index.md` |
| Branch and commit mechanics | `governance/docs/git-policy.md` |
| PR body, scope, review, merge | `governance/docs/pr-standard.md` |
| Validation evidence | `governance/docs/verification-standard.md` |
| Documentation truthfulness | `governance/docs/documentation-standard.md` |
| Architecture decisions | `governance/docs/adr-policy.md` |

This document summarizes the engineering operating model. The detailed owners define the active rules.

## Open Governance Enforcement Gaps

Current gaps:

- no CI enforcement is included;
- no installer is included;
- no template linting is included;
- no release automation is included;
- no external integration is included.

These gaps are acceptable while Blueprint is establishing portable rules first.

Do not claim automation before it exists.

## Engineering Non-Goals

Engineering governance does not provide:

- CI enforcement;
- package publishing;
- install automation;
- product implementation behavior;
- external service integration.

Those may become optional extensions later, but they must not redefine core governance.

## Review Checklist

Before merging engineering-governance changes, confirm:

- task scope is clear;
- branch base is correct;
- one PR maps to one responsibility;
- owner documents are updated;
- root docs remain truthful;
- validation evidence is current;
- planned layers are not claimed as included;
- follow-ups are explicit.
