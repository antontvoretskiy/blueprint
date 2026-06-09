# Blueprint System Relationship Map

This document explains how Blueprint system documents work together.

It is the operating map for owners, dependencies, and recovery flow.

## System Principle

Blueprint is repository-first.

The repository owns durable state, rules, decisions, templates, and validation evidence.

Chat, handoffs, and clean-start briefs can help execution, but they do not replace owner documents.

## Layer Model

| Layer | Owner pattern | Responsibility |
| --- | --- | --- |
| Public entrypoint | `README.md`, `OPEN_SOURCE_SPEC.md` | Explain what Blueprint is and current public status |
| Architecture boundary | `ARCHITECTURE.md` | Define layer boundaries and non-goals |
| Bundle manifest | `BUNDLE_MANIFEST.md` | Declare included, planned, and excluded files |
| Core contracts | `core/**` | Define required process contracts |
| Governance | `governance/docs/**` | Define rule ownership and standards |
| Project Memory | `memory/project-kb/**` | Record current state, decisions, references, and recovery points |
| Templates | `templates/**` | Provide reusable artifacts for other repositories |
| Checklists | `checklists/**` | Provide acceptance criteria when added |
| Examples | `examples/**` | Show sanitized adoption examples when added |

## Owner Map

| System concern | Canonical owner | Supporting documents |
| --- | --- | --- |
| Public positioning | `README.md` | `OPEN_SOURCE_SPEC.md`, `BUNDLE_MANIFEST.md` |
| Product boundary | `OPEN_SOURCE_SPEC.md` | `ARCHITECTURE.md`, `BUNDLE_MANIFEST.md` |
| Layer boundary | `ARCHITECTURE.md` | `governance/docs/engineering-governance.md` |
| Included/planned/excluded status | `BUNDLE_MANIFEST.md` | `memory/project-kb/05_IMPLEMENTATION_STATUS.md` |
| Agent recovery entrypoint | `core/AGENTS.md` | `memory/project-kb/00_INDEX.md`, `memory/project-kb/08_CURRENT_STATE.md` |
| Task routing | `core/TASK_PROCESS_ROUTER.md` | `governance/docs/engineering-governance.md` |
| Feature lifecycle | `core/FEATURE_LIFECYCLE_STANDARD.md` | future `templates/feature-lifecycle/**` |
| PR handoff and clean start | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | `templates/recovery/CLEAN_START_BRIEF.template.md` |
| Branch governance | `governance/docs/git-policy.md` | `governance/docs/pr-standard.md` |
| PR lifecycle | `governance/docs/pr-standard.md` | `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` |
| Verification language | `governance/docs/verification-standard.md` | `Makefile`, PR body |
| Documentation truthfulness | `governance/docs/documentation-standard.md` | `BUNDLE_MANIFEST.md` |
| ADR process | `governance/docs/adr-policy.md` | future `governance/docs/adr/**` |
| Security baseline | `core/SECURITY.md` | `CONTRIBUTING.md` |
| Self-hosting | `governance/docs/engineering-governance.md` | `memory/project-kb/08_CURRENT_STATE.md` |
| Source coverage | `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` | this document |
| System relationships | `memory/project-kb/12_SYSTEM_RELATIONSHIP_MAP.md` | `governance/docs/governance-index.md` |
| Current recovery point | `memory/project-kb/08_CURRENT_STATE.md` | `memory/project-kb/current/CLEAN_START_BRIEF.md` |
| Implementation status | `memory/project-kb/05_IMPLEMENTATION_STATUS.md` | `BUNDLE_MANIFEST.md` |
| Reference map | `memory/project-kb/10_REFERENCE.md` | all owner documents |

## Dependency Flow

```text
README.md
  -> OPEN_SOURCE_SPEC.md
  -> ARCHITECTURE.md
  -> BUNDLE_MANIFEST.md
  -> CONTRIBUTING.md

core/AGENTS.md
  -> memory/project-kb/00_INDEX.md
  -> memory/project-kb/08_CURRENT_STATE.md
  -> memory/project-kb/05_IMPLEMENTATION_STATUS.md
  -> memory/project-kb/10_REFERENCE.md
  -> core/TASK_PROCESS_ROUTER.md

core/TASK_PROCESS_ROUTER.md
  -> core/FEATURE_LIFECYCLE_STANDARD.md
  -> core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md
  -> governance/docs/git-policy.md
  -> governance/docs/pr-standard.md
  -> governance/docs/verification-standard.md

governance/docs/governance-index.md
  -> governance/docs/engineering-governance.md
  -> governance/docs/git-policy.md
  -> governance/docs/pr-standard.md
  -> governance/docs/verification-standard.md
  -> governance/docs/documentation-standard.md
  -> governance/docs/adr-policy.md

memory/project-kb/10_REFERENCE.md
  -> all current owner documents
```

Dependency means the document relies on the owner for active rules.

Dependency does not allow a supporting document to redefine the owner.

## Standard Work Flow

```text
request
-> repository identity check
-> recovery path
-> task routing
-> owner document lookup
-> scoped branch from develop
-> implementation or documentation work
-> validation evidence
-> PR handoff
-> memory update check
-> PR into develop
-> merge
-> clean start
-> next branch from updated develop
```

## Recovery Flow

Fresh sessions recover from:

```text
core/AGENTS.md
-> memory/project-kb/00_INDEX.md
-> memory/project-kb/08_CURRENT_STATE.md
-> memory/project-kb/05_IMPLEMENTATION_STATUS.md
-> memory/project-kb/10_REFERENCE.md
-> core/TASK_PROCESS_ROUTER.md
```

If the task changes governance, also load:

```text
governance/docs/governance-index.md
-> relevant governance owner document
```

If the task changes templates, also load:

```text
BUNDLE_MANIFEST.md
-> ARCHITECTURE.md
-> relevant templates/** README
-> memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md
```

## Self-Hosting Flow

Blueprint validates its own rules by using them on `develop` before release.

```text
new rule or template
-> scoped PR into develop
-> validation using current Blueprint standards
-> Project Memory update if durable state changes
-> clean start can recover the new state
-> only then eligible for release PR into main
```

If a rule cannot guide Blueprint itself, it is not ready to be presented as release-ready.

## Status Truth Flow

When a file or layer becomes included:

1. Add the file.
2. Update `BUNDLE_MANIFEST.md`.
3. Update `memory/project-kb/05_IMPLEMENTATION_STATUS.md`.
4. Update `memory/project-kb/08_CURRENT_STATE.md` if recovery state changes.
5. Update `memory/project-kb/10_REFERENCE.md` if navigation changes.
6. Update `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` if source coverage changes.
7. Update `README.md` or `ARCHITECTURE.md` only when public status or layer architecture changes.

Do not claim included status before files exist.

## Conflict Resolution

When two documents conflict:

1. Use `governance/docs/governance-index.md` to identify the rule owner.
2. Use this relationship map to identify affected supporting documents.
3. Update the owner first.
4. Update summaries and memory second.
5. Report the conflict and resolution in the PR body.

## Current Missing Relationship Owners

The following relationships are not complete yet:

| Missing item | Required owner |
| --- | --- |
| Project context template | `templates/project-memory/01_PROJECT_CONTEXT.template.md` |
| Project map template | `templates/project-memory/02_PROJECT_MAP.template.md` |
| Project architecture memory template | `templates/project-memory/03_SYSTEM_ARCHITECTURE.template.md` |
| Domain model template | `templates/project-memory/04_DOMAIN_MODEL.template.md` |
| Feature artifact templates | `templates/feature-lifecycle/**` |
| Guardian templates | `templates/guardian/**` |
| PR handoff templates | `templates/pr-handoff/**` |
| Checklists | `checklists/**` |

Do not treat the system transfer as complete until these relationships are resolved or explicitly excluded.
