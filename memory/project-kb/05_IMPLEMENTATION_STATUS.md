# Blueprint Implementation Status

This file records what is currently included in Blueprint and what remains planned.

## Included

| Area | Status | Notes |
| --- | --- | --- |
| Public repository presentation | Included | README, license, contribution guide, architecture, manifest |
| Local preview environment | Included | Docker Compose preview and smoke checks |
| Complete product map | Included | Product shape, subsystem links, process levels, project management, and feature management |
| Core contracts | Included | Agent contract, task router, lifecycle, handoff, security |
| Governance standards | Included | Governance index, engineering, git, PR, verification, documentation, ADR |
| Project Memory structure | Included | Reusable Project Memory files and recovery entrypoint |
| Project Memory templates | Included | Reusable templates for project context, map, architecture, domain model, status, workflow, decisions, current state, history, and references |
| Feature lifecycle templates | Included | Reusable FEATURE, CLARIFICATION, PLAN, and TASKS templates |
| PR handoff templates | Included | Reusable PR body, handoff, memory update decision, and clean-start transition templates |
| Guardian templates | Included | Reusable repository, change, architecture, memory, PR, and release guard templates |
| Checklists | Included | Installation, recovery, branch governance, PR readiness, and clean-start acceptance checklists |
| Recovery templates | Included | Recovery path, clean-start brief, and recovery validation templates |
| Source coverage map | Included | Coverage matrix and relationship map for transfer completeness |
| System use-case validation suite | Included | Manual validation suite and checklist for recovery, routing, memory, Guardian, release, and public-quality use cases |
| System use-case validation result | Included | First full manual validation run passed on `develop` |
| AI product example | Included | Sanitized adoption example for applying Blueprint to an AI product repository |
| Public release packaging | Included | Version, changelog, release process, validation checklist, support, conduct, security, and GitHub contribution templates |

## Planned

| Area | Status | Notes |
| --- | --- | --- |
| Additional examples | Planned | SaaS, marketplace, CRM, and regulated platform examples |
| Branch cleanup | Planned | Merged docs branches can be cleaned after maintainer approval |
| v0.4.0 scope selection | Planned | Must happen after branch cleanup or explicit maintainer decision to defer cleanup |

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
make smoke
git diff --check
```

Public PRs also run wording, link, path-scope, title, and PR-body checks.
