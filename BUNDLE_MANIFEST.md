# Blueprint Bundle Manifest

This manifest defines what belongs in the current Blueprint bundle, what is planned later, and what is explicitly excluded from core.

## Included Now

| Path | Status | Purpose |
| --- | --- | --- |
| `README.md` | Included | Public product landing page |
| `LICENSE` | Included | MIT license |
| `CONTRIBUTING.md` | Included | Contribution rules and validation expectations |
| `OPEN_SOURCE_SPEC.md` | Included | Product definition and scope |
| `ARCHITECTURE.md` | Included | Core, extension, and example layer boundaries |
| `BUNDLE_MANIFEST.md` | Included | Bundle composition and boundaries |
| `docs/benchmarks/spec-kit-open-source-marketing-benchmark.md` | Included | Public presentation benchmark |
| `media/blueprint-logo.png` | Included | Public brand asset |
| `Makefile` | Included | Local validation commands |
| `compose.yaml` | Included | Isolated local preview environment |
| `.env.example` | Included | Non-secret local environment defaults |
| `public/` | Included | Static preview surface |
| `public/api/` | Included | Static API preview endpoint for local smoke checks |
| `core/AGENTS.md` | Included | Agent operating contract |
| `core/TASK_PROCESS_ROUTER.md` | Included | Task routing by operating layer |
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
| `memory/project-kb/current/CLEAN_START_BRIEF.md` | Included | Current clean-start brief |
| `memory/project-kb/architecture-decisions/GUARDIAN_ARCHITECTURE.md` | Included | Guardian process architecture |
| `memory/project-kb/GUARDIAN_VALIDATION_SCENARIOS.md` | Included | Generic Guardian validation scenarios |

## Planned Later

| Area | Planned paths |
| --- | --- |
| Templates | `templates/project-memory/`, `templates/feature-lifecycle/`, `templates/pr-handoff/`, `templates/guardian/`, `templates/recovery/` |
| Examples | `examples/ai-product/` first, then SaaS, marketplace, CRM, regulated platform |
| Checklists | installation, recovery, branch governance, PR readiness, clean start |
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
