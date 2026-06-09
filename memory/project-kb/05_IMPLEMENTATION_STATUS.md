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
| Recovery templates | Included | Recovery path, clean-start brief, and recovery validation templates |
| Source coverage map | Included | Coverage matrix and relationship map for transfer completeness |

## Planned

| Area | Status | Notes |
| --- | --- | --- |
| Guardian templates | Planned | To be added after recovery shape is stable |
| Feature lifecycle templates | Planned | Reusable FEATURE, CLARIFICATION, PLAN, and TASKS templates |
| PR handoff templates | Planned | Reusable PR handoff and memory update templates |
| Checklists | Planned | Installation, recovery, branch, PR readiness, clean start |
| Examples | Planned | Sanitized examples only |
| Release process | Planned | Release PR from `develop` into `main` |

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
