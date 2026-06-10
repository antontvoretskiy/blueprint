# Blueprint Bundle Manifest

This manifest defines what belongs in the current Blueprint bundle, what is planned later, and what is explicitly excluded from core.

## Included Now

| Path | Status | Purpose |
| --- | --- | --- |
| `README.md` | Included | Public product landing page |
| `VERSION` | Included | Current version marker |
| `CHANGELOG.md` | Included | Versioned public change history |
| `RELEASE.md` | Included | Manual release process |
| `LICENSE` | Included | MIT license |
| `CODE_OF_CONDUCT.md` | Included | Public participation rules |
| `SUPPORT.md` | Included | Public support boundaries |
| `SECURITY.md` | Included | Public security reporting policy |
| `CONTRIBUTING.md` | Included | Contribution rules and validation expectations |
| `OPEN_SOURCE_SPEC.md` | Included | Product definition and scope |
| `OPEN_SOURCE_GUIDE.md` | Included | Public entry points and quality rules |
| `ADAPTATION_GUIDE.md` | Included | Adoption and installation guide |
| `MIGRATION_GUIDE.md` | Included | Migration and sanitization guide |
| `VALIDATION_CHECKLIST.md` | Included | Public release and adoption validation checklist |
| `docs/validation/system-use-case-suite.md` | Included | Manual system use-case validation suite, v0.4.1 |
| `docs/validation/process-efficiency-dogfood-v0.4.1.md` | Included | Manual process-efficiency dogfood audit, v0.4.1 |
| `PRODUCT_MAP.md` | Included | Complete product shape, process levels, and project/feature management model |
| `ARCHITECTURE.md` | Included | Core, extension, and example layer boundaries |
| `BUNDLE_MANIFEST.md` | Included | Bundle composition and boundaries |
| `.github/CODEOWNERS` | Included | Repository ownership hint |
| `.github/PULL_REQUEST_TEMPLATE.md` | Included | Public PR structure template |
| `.github/ISSUE_TEMPLATE/config.yml` | Included | Public issue template configuration |
| `.github/ISSUE_TEMPLATE/framework_change.yml` | Included | Framework change request template |
| `.github/ISSUE_TEMPLATE/docs_issue.yml` | Included | Documentation issue template |
| `docs/benchmarks/spec-kit-open-source-marketing-benchmark.md` | Included | Public presentation benchmark |
| `media/blueprint-logo.png` | Included | Public brand asset |
| `Makefile` | Included | Local validation commands |
| `compose.yaml` | Included | Isolated local preview environment |
| `.env.example` | Included | Non-secret local environment defaults |
| `public/` | Included | Static preview surface |
| `public/api/` | Included | Static API preview endpoint for local smoke checks |
| `core/AGENTS.md` | Included | Agent operating contract |
| `core/TASK_PROCESS_ROUTER.md` | Included | Task routing, process levels, context budgets, and recovery budgets |
| `core/FEATURE_LIFECYCLE_STANDARD.md` | Included | Feature lifecycle standard |
| `core/PR_HANDOFF_AND_CLEAN_START_STANDARD.md` | Included | PR handoff and clean-start standard |
| `core/SECURITY.md` | Included | Portable security baseline |
| `governance/docs/governance-index.md` | Included | Governance authority map |
| `governance/docs/engineering-governance.md` | Included | Engineering operating model |
| `governance/docs/git-policy.md` | Included | Branch and merge policy |
| `governance/docs/pr-standard.md` | Included | Pull request standard |
| `governance/docs/verification-standard.md` | Included | Validation evidence standard |
| `governance/docs/documentation-standard.md` | Included | Documentation truthfulness standard |
| `governance/docs/adr-policy.md` | Included | Architecture decision record policy |
| `memory/project-kb/00_INDEX.md` | Included | Project Memory entrypoint |
| `memory/project-kb/05_IMPLEMENTATION_STATUS.md` | Included | Implementation status memory |
| `memory/project-kb/06_WORKFLOW_AND_RULES.md` | Included | Workflow memory |
| `memory/project-kb/07_DECISIONS_LOG.md` | Included | Decisions memory |
| `memory/project-kb/08_CURRENT_STATE.md` | Included | Current-state memory |
| `memory/project-kb/09_TASK_HISTORY.md` | Included | Task-history memory |
| `memory/project-kb/10_REFERENCE.md` | Included | Reference map |
| `memory/project-kb/11_SOURCE_COVERAGE_MATRIX.md` | Included | Source-reference coverage matrix |
| `memory/project-kb/12_SYSTEM_RELATIONSHIP_MAP.md` | Included | Owner and dependency relationship map |
| `memory/project-kb/current/CLEAN_START_BRIEF.md` | Included | Current clean-start brief |
| `memory/project-kb/current/RECOVERY_VALIDATION.md` | Included | Current recovery validation result |
| `memory/project-kb/current/SYSTEM_USE_CASE_VALIDATION.md` | Included | Current system use-case validation result |
| `memory/project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md` | Included | Guardian process architecture |
| `memory/project-kb/GUARDIAN_VALIDATION_SCENARIOS.md` | Included | Generic Guardian validation scenarios |
| `templates/project-memory/README.md` | Included | Project Memory template bundle guide, v0.2.0 |
| `templates/project-memory/00_INDEX.template.md` | Included | Project Memory index template |
| `templates/project-memory/01_PROJECT_CONTEXT.template.md` | Included | Project context template |
| `templates/project-memory/02_PROJECT_MAP.template.md` | Included | Project map template |
| `templates/project-memory/03_SYSTEM_ARCHITECTURE.template.md` | Included | System architecture memory template |
| `templates/project-memory/04_DOMAIN_MODEL.template.md` | Included | Domain model template |
| `templates/project-memory/05_IMPLEMENTATION_STATUS.template.md` | Included | Implementation status template |
| `templates/project-memory/06_WORKFLOW_AND_RULES.template.md` | Included | Workflow and rules template |
| `templates/project-memory/07_DECISIONS_LOG.template.md` | Included | Decisions log template |
| `templates/project-memory/08_CURRENT_STATE.template.md` | Included | Current state template |
| `templates/project-memory/09_TASK_HISTORY.template.md` | Included | Task history template |
| `templates/project-memory/10_REFERENCE.template.md` | Included | Reference map template |
| `templates/feature-lifecycle/README.md` | Included | Feature Lifecycle template bundle guide, v0.2.0 |
| `templates/feature-lifecycle/FEATURE.template.md` | Included | Feature specification template |
| `templates/feature-lifecycle/CLARIFICATION.template.md` | Included | Feature clarification template |
| `templates/feature-lifecycle/PLAN.template.md` | Included | Feature implementation plan template |
| `templates/feature-lifecycle/TASKS.template.md` | Included | Feature task breakdown template |
| `templates/pr-handoff/README.md` | Included | PR handoff template bundle guide, v0.2.0 |
| `templates/pr-handoff/PR_BODY.template.md` | Included | Structured PR body template |
| `templates/pr-handoff/PR_HANDOFF.template.md` | Included | PR handoff summary template |
| `templates/pr-handoff/MEMORY_UPDATE_DECISION.template.md` | Included | Memory update decision template |
| `templates/pr-handoff/CLEAN_START_TRANSITION.template.md` | Included | Clean-start transition template |
| `templates/guardian/README.md` | Included | Guardian template bundle guide, v0.3.0 |
| `templates/guardian/REPOSITORY_GUARDIAN.template.md` | Included | Repository identity and branch guard template |
| `templates/guardian/CHANGE_GUARDIAN.template.md` | Included | Scope and public-claim guard template |
| `templates/guardian/ARCHITECTURE_GUARDIAN.template.md` | Included | Architecture boundary guard template |
| `templates/guardian/MEMORY_GUARDIAN.template.md` | Included | Project Memory update guard template |
| `templates/guardian/PR_GUARDIAN.template.md` | Included | PR readiness guard template |
| `templates/guardian/RELEASE_GUARDIAN.template.md` | Included | Release readiness guard template |
| `templates/recovery/README.md` | Included | Recovery template bundle guide, v0.3.0 |
| `templates/recovery/RECOVERY_PATH.template.md` | Included | Fresh-session recovery path template |
| `templates/recovery/CLEAN_START_BRIEF.template.md` | Included | Clean-start brief template |
| `templates/recovery/RECOVERY_VALIDATION.template.md` | Included | Recovery validation template |
| `checklists/README.md` | Included | Checklist bundle guide, v0.3.0 |
| `checklists/installation-checklist.md` | Included | Installation acceptance checklist |
| `checklists/recovery-checklist.md` | Included | Recovery acceptance checklist |
| `checklists/branch-governance-checklist.md` | Included | Branch governance acceptance checklist |
| `checklists/pr-readiness-checklist.md` | Included | PR readiness acceptance checklist |
| `checklists/clean-start-checklist.md` | Included | Clean-start acceptance checklist |
| `checklists/system-use-case-validation-checklist.md` | Included | System use-case validation checklist, v0.4.1 |
| `examples/ai-product/README.md` | Included | AI product adoption example guide, v0.3.0 |
| `examples/ai-product/ADOPTION_MAP.md` | Included | AI product adoption mapping example |
| `examples/ai-product/BRANCH_GOVERNANCE_EXAMPLE.md` | Included | AI product branch governance example |
| `examples/ai-product/RECOVERY_WALKTHROUGH.md` | Included | AI product recovery walkthrough |

## Planned Later

| Area | Planned paths |
| --- | --- |
| Additional examples | SaaS, marketplace, CRM, regulated platform |
| Extensions | CLI, installer, GitHub Actions, MCP integration, validation scripts |

Planned content must stay marked as planned until it exists in the repository.

## Explicitly Excluded From Core

Blueprint core must not include:

- runtime framework;
- agent runtime;
- workflow engine;
- code generator;
- MCP server;
- SaaS starter kit;
- product framework;
- UI framework;
- product runtime;
- product algorithms;
- admin UI;
- product memory;
- product history;
- product PR timeline;
- product-specific decisions;
- private source-reference anchors.

## Bundle Acceptance Criteria

A Blueprint bundle is acceptable when:

- every included file has a clear operating purpose;
- every planned file is marked as planned, not implemented;
- no private product memory is copied as-is;
- no product runtime assumptions are required;
- validation claims match actual repository contents;
- installation can be performed without access to a private source project;
- README links resolve;
- forbidden public wording scan passes;
- commit and PR titles follow the public contribution standard;
- versioned public assets declare their SemVer version;
- local preview validation passes.
