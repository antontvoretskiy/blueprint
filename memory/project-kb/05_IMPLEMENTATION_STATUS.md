# Blueprint Implementation Status

This file records what is currently included in Blueprint and what remains planned.

## Included

| Area | Status | Notes |
| --- | --- | --- |
| Public repository presentation | Included | README, license, contribution guide, architecture, manifest; v0.9.0 public README is released |
| Local preview environment | Included | Docker Compose preview and smoke checks |
| Complete product map | Included | Product shape, subsystem links, process levels, project management, and feature management |
| Core contracts | Included | Agent contract, task router, compact process levels, context budgets, recovery budgets, lifecycle, handoff, security |
| Governance standards | Included | Governance index, engineering, git, PR, verification, documentation, ADR |
| Project Memory structure | Included | Reusable Project Memory files and recovery entrypoint |
| Project Memory templates | Included | Reusable templates for project context, map, architecture, domain model, status, workflow, decisions, current state, history, and references |
| Feature lifecycle templates | Included | Reusable FEATURE, CLARIFICATION, PLAN, and TASKS templates |
| PR handoff templates | Included | Reusable PR body, handoff, memory update decision, and clean-start transition templates |
| Guardian templates | Included | Reusable repository, change, architecture, memory, PR, and release guard templates |
| Checklists | Included | Installation, recovery, branch governance, PR readiness, and clean-start acceptance checklists |
| Recovery templates | Included | Recovery path, clean-start brief, and recovery validation templates |
| Source coverage map | Included | Coverage matrix and relationship map for transfer completeness |
| System use-case validation suite | Included | Manual validation suite, checklist, and v0.8.0 fixtures for recovery, routing, memory, Guardian, release, public-quality use cases, and process-level regression scenarios |
| System use-case validation result | Included | Historical v0.4.0 manual validation is retained; current validation now requires v0.8.0 fixture checks and main-only release evidence |
| Post-validation branch cleanup | Included | Merged docs branches after PRs #20 through #25 were removed locally and remotely after maintainer approval |
| AI product example | Included | Sanitized adoption example for applying Blueprint to an AI product repository |
| Public release packaging | Included | Version, changelog, release process, validation checklist, support, conduct, security, and GitHub contribution templates |
| Public use-case media | Included | Blueprint logo and practical AI-agent use-case screenshots for the public README |
| Public main-only branch model | Included | Public GitHub exposes `main` as the release-ready distribution branch; maintainer integration branches may be local or private |
| Documentation quality gates | Included | Local `make quality` checks, validation fixture checks, and docs-quality GitHub Actions workflow validate repository documentation claims |
| Documentation navigation | Included | Docs landing page, navigation map, quickstart, repository-first concept, template reference, governance reference, and community guide |
| Validation fixtures | Included | Versioned UC, RT, and release-readiness fixture data plus `scripts/check_validation_fixtures.py` |
| Context export | Included | Ordered context export manifest, local bundle generation commands, and ignored generated output path |

## Planned

| Area | Status | Notes |
| --- | --- | --- |
| Additional examples | Planned | SaaS, marketplace, CRM, and regulated platform examples |
| CLI and installer | Planned | Remain outside the current bundle until manual adoption becomes too repetitive |
| Release automation | Planned | Release publication remains manual until the release process repeats enough to automate safely |

## Excluded From Core

Blueprint core excludes:

- runtime framework;
- agent runtime;
- workflow engine;
- code generator;
- product implementation;
- product UI;
- product API;
- product algorithms;
- private product memory;
- product release history.

Blueprint may govern repositories that contain those areas, but it must not include their implementation.

## Validation Baseline

Current local validation commands:

```bash
make doctor
make config
make quality
make smoke
git diff --check
python3 -m py_compile scripts/check_quality.py
python3 -m py_compile scripts/check_validation_fixtures.py
python3 -m py_compile scripts/export_context.py
make context-export
make context-chat
```

Public PRs also run wording, link, path-scope, title, and PR-body checks.

System use-case validation must also run the process-level regression matrix
before UC-03 can be reported as passed for future packaging. In v0.8.0 and
later, the fixture checker verifies the required UC and RT fixture coverage.
