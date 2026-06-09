# Blueprint Open Source Specification

## Product Definition

Blueprint is an open-source operating framework for AI-native software development.

It defines how a repository manages:

- governance;
- project memory;
- task routing;
- process levels;
- feature lifecycle;
- PR lifecycle;
- branch governance;
- recovery between AI chats;
- Guardian checks;
- clean starts after merge.

Blueprint is not a product runtime, not a code generator, and not a feature framework.

## Problem Statement

AI-native software teams increasingly depend on human and agent collaboration across many disconnected sessions. Without a repository-level operating framework, work becomes fragile:

- AI chat context gets lost.
- Project rules live in chat instead of the repository.
- Agents start work without recovery.
- PRs mix unrelated layers.
- Branches do not mirror architecture.
- Documentation claims more than implementation proves.
- New chats cannot continue without old conversation history.

Blueprint makes those operating rules explicit, versioned, reviewable, and portable.

## Target Users

Blueprint is for:

- AI-native product teams;
- solo builders using AI coding agents;
- engineering teams using Codex, Claude, Cursor, or similar tools;
- startups with fast-moving repositories;
- multi-module SaaS and product repositories;
- teams that need repository-first governance.

## Core Outcome

A repository using Blueprint should be able to answer:

1. What rules govern this project?
2. Where is durable project memory stored?
3. How does a new AI chat recover current state?
4. Which operating layer owns this task?
5. Which branch should this work happen on?
6. What makes a PR ready for review?
7. What must be checked before a clean start after merge?
8. What claims are proven, planned, or out of scope?
9. How much process is required for this task?
10. Which project or feature artifacts must exist before implementation?

## Operating Layers

Blueprint is organized around connected operating layers:

| Layer | Responsibility |
| --- | --- |
| Governance | Repository rules, ownership, source of truth, standards |
| Project Memory | Project knowledge, current state, decision history, recovery input |
| Process Levels | L0-L4 task-size model that prevents unnecessary procedure |
| Recovery | New-chat recovery, handoff, clean-start briefs |
| Guardian | Pre-work, pre-merge, and scope-drift checks |
| Branch Governance | Branch roles, architecture boundaries, merge sequencing |
| Feature Lifecycle | Feature intake, planning, implementation, validation |
| PR Lifecycle | PR scope, review readiness, handoff, post-merge reset |

The complete product shape is owned by `PRODUCT_MAP.md`.

## Non-Goals

Blueprint does not provide:

- product runtime implementation;
- domain algorithms;
- generated application code;
- UI framework components;
- feature scaffolding;
- model orchestration runtime;
- private product memory;
- source-project PR history;
- source-project migration timeline.

## Difference From Spec Kit

[GitHub Spec Kit](https://github.com/github/spec-kit) is focused on Spec-Driven Development: specs, plans, tasks, and implementation flow.

Blueprint is broader and more operational:

| Area | Spec Kit | Blueprint |
| --- | --- | --- |
| Main focus | Spec-driven development | Repository operating framework |
| Primary artifact | Specs, plans, tasks | Governance, memory, recovery, lifecycle |
| AI chat recovery | Not the main layer | Core feature |
| Project memory | Constitution-style project guidance | Explicit memory system |
| Branch governance | Not primary | Core layer |
| PR handoff and clean start | Not primary | Core layer |
| Guardian process | Not primary | Core layer |
| Scope | Feature delivery workflow | Full project operation framework |

## Open Source Requirements

Blueprint must remain:

- generic enough to install into any repository;
- explicit about what is implemented versus planned;
- free of private product history;
- free of product-specific runtime assumptions;
- structured for human and AI agent contributors;
- readable without access to the original source project.

## v0.1.0 Scope

v0.1.0 includes:

- README;
- license;
- contributing guide;
- open-source specification;
- architecture document;
- bundle manifest;
- local preview environment;
- open-source presentation benchmark.

v0.1.0 does not include:

- automation or CLI;
- runtime integrations;
- GitHub Actions enforcement;
- package manager setup;
- generated archive tooling;
- reusable templates;
- example project bundles.

## Release Readiness Criteria

Before the first public release:

- license is present;
- README explains the product and its limits;
- architecture and manifest agree on current scope;
- contribution rules prevent product-specific leakage;
- product-term scan is clean or justified;
- quickstart does not require private context;
- planned work is clearly marked as planned.
