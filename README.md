<p align="center">
  <img src="media/blueprint-logo.png" alt="Blueprint logo" width="440">
</p>

<h1 align="center">📐 Blueprint</h1>

<p align="center">
  <strong>Operating framework for AI-native software development.</strong>
</p>

<p align="center">
  Keep governance, project memory, recovery, branch rules, and PR handoff inside the repository.
</p>

<p align="center">
  <a href="https://github.com/antontvoretskiy/blueprint/releases/tag/v0.4.2"><img alt="Release: v0.4.2" src="https://img.shields.io/badge/release-v0.4.2-blue"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green"></a>
  <a href="docs/validation/process-efficiency-dogfood-v0.4.1.md"><img alt="Validation: dogfooded" src="https://img.shields.io/badge/validation-dogfooded-0f766e"></a>
  <a href="BUNDLE_MANIFEST.md"><img alt="Status: released" src="https://img.shields.io/badge/status-released-0f766e"></a>
  <a href="https://github.com/antontvoretskiy/blueprint/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/antontvoretskiy/blueprint?style=social"></a>
</p>

Blueprint helps software teams and AI agents operate from the repository instead of from fragile chat memory.

Chat helps execution. The repository owns durable rules, current state, recovery points, validation evidence, and handoff.

Blueprint is not a runtime, code generator, agent runtime, workflow engine, SaaS starter kit, product framework, or UI framework.

<a id="table-of-contents"></a>

## 🧭 Table of Contents

- [🤔 What Is Blueprint?](#what-is-blueprint)
- [⚡ Get Started](#get-started)
- [🧠 Practical AI-Agent Use Cases](#practical-ai-agent-use-cases)
- [🧩 What Blueprint Manages](#what-blueprint-manages)
- [🔁 Repository Recovery Loop](#repository-recovery-loop)
- [🛡️ Guardian Checks](#guardian-checks)
- [🌱 Blueprint vs GitHub Spec Kit](#blueprint-vs-github-spec-kit)
- [📁 Repository Structure](#repository-structure)
- [✅ Current Status](#current-status)
- [🧪 Validation](#validation)
- [🛠️ Repository Development](#repository-development)
- [🗺️ Roadmap](#roadmap)
- [🤝 Contributing](#contributing)
- [📄 License](#license)

<a id="what-is-blueprint"></a>

## 🤔 What Is Blueprint?

Blueprint is a repository-first operating framework for AI-native software development.

It defines how a repository manages:

- governance and source-of-truth ownership;
- project memory and current-state recovery;
- task routing and process levels;
- feature lifecycle and planning boundaries;
- PR lifecycle, handoff, and clean start;
- branch governance and release flow;
- Guardian checks for scope, truthfulness, and validation.

The shift is simple:

```text
old way: project context lives in chat
new way: project context lives in the repository
```

That matters because AI-native projects fail when a new chat cannot recover state, a PR mixes unrelated scopes, or documentation claims more than the repository proves.

<a id="get-started"></a>

## ⚡ Get Started

Blueprint is documentation-first. There is no installer yet.

Start with this 10-minute path:

1. Read the product shape in [PRODUCT_MAP.md](PRODUCT_MAP.md).
2. Pick an adoption path in [ADAPTATION_GUIDE.md](ADAPTATION_GUIDE.md).
3. Copy either the minimal or full template set from [templates/](templates).
4. Create your Project Memory from [templates/project-memory/README.md](templates/project-memory/README.md).
5. Run a recovery test from a new AI chat using the prompt below.

Fresh-chat recovery prompt:

```text
Read the repository recovery path and tell me:
1. current project state;
2. current branch and release status;
3. latest validated work;
4. next recommended task;
5. files I should read before making changes.

Use repository files as the source of truth.
```

If the new chat needs old conversation history to continue, recovery failed.

<a id="practical-ai-agent-use-cases"></a>

## 🧠 Practical AI-Agent Use Cases

Blueprint is designed to be used directly inside Codex, Claude, Cursor, ChatGPT, and other AI-assisted development workflows.

### 🧭 Recover A New Codex Chat

Use this when you open a new chat and need the agent to continue from the repository, not from memory.

```text
Recover this repository from its Blueprint files.

Start from:
- memory/project-kb/00_INDEX.md
- memory/project-kb/08_CURRENT_STATE.md
- memory/project-kb/05_IMPLEMENTATION_STATUS.md
- memory/project-kb/10_REFERENCE.md
- core/TASK_PROCESS_ROUTER.md

Return:
1. current state;
2. active branch model;
3. latest release;
4. next safe task;
5. required validation before edits.
```

### 🔄 Sync Project Context Into Another AI Chat

Use this when you want to update ChatGPT, Claude, or another assistant with the repository source of truth.

```text
Send me the markdown files that represent the current project source of truth
so I can update another AI chat.

Include:
- memory/project-kb/00_INDEX.md
- memory/project-kb/08_CURRENT_STATE.md
- memory/project-kb/05_IMPLEMENTATION_STATUS.md
- memory/project-kb/09_TASK_HISTORY.md
- memory/project-kb/10_REFERENCE.md
- memory/project-kb/current/CLEAN_START_BRIEF.md
- core/TASK_PROCESS_ROUTER.md

Do not summarize them unless I ask.
Do not include private source-reference files.
```

### ⚖️ Classify A Task Before Spending Context

Use this when the task might be small and you do not want the agent to run a heavy process for a docs-only or status-only request.

```text
Classify this task through Blueprint process levels before doing any work.

Return:
- selected level: L0, L1, L2, L3, or L4;
- why this level is enough;
- recovery budget;
- context budget;
- files you need to read;
- validation required.

If the task is L0 or L1, keep the answer compact.
```

### 🧾 Prepare A PR Handoff

Use this before opening or handing off a PR.

```text
Prepare a Blueprint PR handoff for this branch.

Include:
- problem;
- solution;
- scope;
- changed files;
- validation;
- risks;
- follow-ups;
- memory update decision;
- clean-start decision.

Use repository files as the source of truth.
```

### 🧼 Clean Start After Merge

Use this after a PR merges so the next chat does not depend on the old conversation.

```text
Update the repository recovery state after this merge.

Check:
- current state;
- task history;
- clean-start brief;
- reference map;
- whether new validation evidence should be linked.

Do not create a second memory system.
Keep only durable state that helps the next chat recover.
```

<a id="what-blueprint-manages"></a>

## 🧩 What Blueprint Manages

| Layer | Purpose | Canonical starting point |
| --- | --- | --- |
| Governance | Rule ownership, policy, validation language | [governance/docs/governance-index.md](governance/docs/governance-index.md) |
| Project Memory | Durable current state and recovery knowledge | [memory/project-kb/00_INDEX.md](memory/project-kb/00_INDEX.md) |
| Process Levels | How much procedure a task requires | [core/TASK_PROCESS_ROUTER.md](core/TASK_PROCESS_ROUTER.md) |
| Recovery | Fresh-chat continuation from repository files | [templates/recovery/README.md](templates/recovery/README.md) |
| Guardian | Scope, truthfulness, and boundary checks | [templates/guardian/README.md](templates/guardian/README.md) |
| Branch Governance | Branch naming, layering, and release flow | [governance/docs/git-policy.md](governance/docs/git-policy.md) |
| Feature Lifecycle | From idea to clarification, plan, tasks, implementation | [core/FEATURE_LIFECYCLE_STANDARD.md](core/FEATURE_LIFECYCLE_STANDARD.md) |
| PR Lifecycle | PR scope, validation, handoff, and clean start | [core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md](core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md) |

Blueprint governs project work. It does not implement product work.

<a id="repository-recovery-loop"></a>

## 🔁 Repository Recovery Loop

Blueprint work follows a loop that scales from tiny status checks to release work:

```text
request
-> repository identity check
-> recovery budget
-> task routing
-> process level
-> owner document
-> scoped work
-> validation evidence
-> PR handoff when needed
-> Project Memory update when durable state changed
-> clean start
-> next chat recovers from repository
```

Small tasks stay small. Risky tasks get the full process.

| Level | Use for | Default recovery |
| --- | --- | --- |
| L0 | status checks, clean checks, answer-only repo checks | 0 recovery docs |
| L1 | docs-only commits, handoff reports, small memory updates | max 2 recovery docs |
| L2 | scoped layer changes | max 3 recovery docs |
| L3 | meaningful feature implementation | feature lifecycle required |
| L4 | architecture, migration, release, merge, cross-domain work | full recovery allowed |

<a id="guardian-checks"></a>

## 🛡️ Guardian Checks

Guardian is Blueprint's process-control layer.

It checks whether work is compatible with repository rules before work starts, during review, and before merge.

Guardian helps catch:

- wrong-repository edits;
- dirty checkout contamination;
- docs claims without implementation evidence;
- mixed-scope PRs;
- branch names that do not match architecture;
- stale Project Memory;
- missing PR handoff;
- chat context that never made it back into the repository.

Guardian is not CI, not an agent runtime, and not a service.

<a id="blueprint-vs-github-spec-kit"></a>

## 🌱 Blueprint vs GitHub Spec Kit

[GitHub Spec Kit](https://github.com/github/spec-kit) is focused on Spec-Driven Development: specifications, plans, tasks, and implementation flow.

Blueprint is broader and more operational:

| Area | GitHub Spec Kit | Blueprint |
| --- | --- | --- |
| Main focus | Spec-driven development | Repository operating framework |
| Primary artifact | Specs, plans, tasks | Governance, memory, recovery, lifecycle |
| AI chat recovery | Not the main layer | Core feature |
| Project memory | Constitution-style project guidance | Explicit memory system |
| Branch governance | Not primary | Core layer |
| PR handoff and clean start | Not primary | Core layer |
| Guardian process | Not primary | Core layer |
| Scope | Feature delivery workflow | Full project operation framework |

Use Spec Kit when you need a spec-centered delivery workflow.

Use Blueprint when you need the repository itself to operate predictably across humans, AI agents, branches, PRs, and chats.

<a id="repository-structure"></a>

## 📁 Repository Structure

| Path | Purpose |
| --- | --- |
| [core/](core) | Agent entrypoint, router, lifecycle, handoff, security |
| [governance/](governance) | Branch, PR, verification, documentation, and ADR standards |
| [memory/project-kb/](memory/project-kb) | Project Memory and recovery state |
| [templates/](templates) | Reusable adoption templates |
| [checklists/](checklists) | Manual validation and readiness checklists |
| [examples/](examples) | Sanitized adoption examples |
| [docs/validation/](docs/validation) | Manual validation suites and dogfood evidence |
| [media/](media) | Public brand and README assets |

The full bundle is listed in [BUNDLE_MANIFEST.md](BUNDLE_MANIFEST.md).

<a id="current-status"></a>

## ✅ Current Status

Blueprint v0.4.2 is released on `main`.

Included now:

| Area | Status |
| --- | --- |
| Product definition and architecture | Included |
| Core operating contracts | Included |
| Governance standards | Included |
| Project Memory structure | Included |
| Project Memory templates | Included |
| Feature Lifecycle templates | Included |
| PR handoff templates | Included |
| Guardian templates | Included |
| Recovery templates | Included |
| Checklists | Included |
| AI product example | Included |
| System use-case validation suite | Included |
| Process-efficiency dogfood audit | Included |
| Local preview environment | Included |

Not included yet:

- additional example projects;
- validation automation;
- CLI;
- installer;
- runtime integrations.

<a id="validation"></a>

## 🧪 Validation

Blueprint tracks validation as repository-owned evidence.

| Validation artifact | Purpose |
| --- | --- |
| [System use-case validation suite](docs/validation/system-use-case-suite.md) | Manual end-to-end use-case coverage |
| [Process-efficiency dogfood audit](docs/validation/process-efficiency-dogfood-v0.4.1.md) | Evidence that L0/L1/L2 budgets work in this repository |
| [Validation checklist](VALIDATION_CHECKLIST.md) | Public release and adoption validation gates |
| [Bundle manifest](BUNDLE_MANIFEST.md) | Included, planned, and excluded assets |

The current release also passed local repository checks:

```bash
make doctor
make config
make smoke
git diff --check
```

<a id="repository-development"></a>

## 🛠️ Repository Development

This repository includes an isolated local Docker preview environment.

Requirements:

- Docker Desktop with Docker Compose
- `make`

Start the environment:

```bash
make doctor
make up
make smoke
```

Default local endpoints:

| Service | URL |
| --- | --- |
| App preview | <http://127.0.0.1:3231> |
| API placeholder | <http://127.0.0.1:8231> |
| Mailpit | <http://127.0.0.1:8046> |
| Postgres | `127.0.0.1:55461` |
| Redis | `127.0.0.1:6406` |
| SMTP | `127.0.0.1:1046` |

Useful commands:

```bash
make doctor  # check local port and Docker namespace conflicts
make config  # validate compose config
make up      # start the local stack
make ps      # show containers
make logs    # stream logs
make smoke   # verify app and api placeholders respond
make down    # stop containers
make clean   # stop containers and remove local volumes
```

<a id="roadmap"></a>

## 🗺️ Roadmap

| Version | Scope |
| --- | --- |
| v0.1.0 | Public repository bootstrap, architecture, manifest, contribution policy, preview environment |
| v0.2.0 | Core operating contracts, governance standards, and Project Memory structure |
| v0.3.0 | Recovery, Guardian, PR handoff, validation templates, checklists, first AI product example, and public release packaging |
| v0.4.0 | System use-case validation, dependency verification, branch cleanup completion, and packaging readiness |
| v0.4.1 | Process-level regression hardening, context budgets, and recovery budgets |
| v0.4.2 | Process-efficiency dogfood audit and post-audit recovery state |
| Next | README funnel, practical use-case media, adoption readiness |

<a id="contributing"></a>

## 🤝 Contributing

Blueprint uses professional commit, PR, validation, and versioning standards.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.

Release-facing PRs use:

```text
Problem
Solution
Scope
Validation
Risks
Follow-ups
```

<a id="license"></a>

## 📄 License

Blueprint is released under the [MIT License](LICENSE).
