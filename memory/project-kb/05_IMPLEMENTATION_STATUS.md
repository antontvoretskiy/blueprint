# Blueprint Implementation Status

This file records what is currently included in Blueprint and what remains planned.

## Included

| Area | Status | Notes |
| --- | --- | --- |
| Public repository presentation | Included | README, license, contribution guide, architecture, manifest |
| Local preview environment | Included | Docker Compose preview and smoke checks |
| Core contracts | Included | Agent contract, task router, lifecycle, handoff, security |
| Governance standards | Included | Governance index, engineering, git, PR, verification, documentation, ADR |
| Project Memory structure | Included | Reusable Project Memory files and recovery entrypoint |
| Recovery templates | Included | Recovery path, clean-start brief, and recovery validation templates |

## Planned

| Area | Status | Notes |
| --- | --- | --- |
| Guardian templates | Planned | To be added after recovery shape is stable |
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
