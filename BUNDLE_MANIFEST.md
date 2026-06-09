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

## Planned Later

| Area | Planned paths |
| --- | --- |
| Governance standards | `governance/docs/governance-index.md`, `engineering-governance.md`, `git-policy.md`, `pr-standard.md`, `verification-standard.md`, `documentation-standard.md`, `adr-policy.md` |
| Project Memory | `memory/project-kb/00_INDEX.md`, `05_IMPLEMENTATION_STATUS.md`, `06_WORKFLOW_AND_RULES.md`, `07_DECISIONS_LOG.md`, `08_CURRENT_STATE.md`, `09_TASK_HISTORY.md`, `10_REFERENCE.md` |
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
