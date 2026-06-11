# Blueprint Validation Fixtures

Asset: validation-fixtures
Version: v0.8.0
Type: Validation Fixture Bundle
Author: Blueprint Maintainers
Status: Release target

These fixtures make Blueprint validation expectations inspectable from
repository files.

They do not run Blueprint in another repository, install dependencies, call
external services, or replace manual review. They define stable expected inputs
and outcomes that local validation scripts can check before a release.

## Fixture Files

| Fixture | Purpose |
| --- | --- |
| `system-use-cases.json` | Defines the UC-01 through UC-15 validation matrix |
| `process-level-regression.json` | Defines RT-01 through RT-18 router expectations |
| `release-readiness.json` | Defines main-only release readiness evidence |

## Checker

Run the fixture checker through the repository quality target:

```bash
make quality
```

Or run it directly:

```bash
python3 scripts/check_validation_fixtures.py
```

The checker validates fixture shape, required IDs, expected process levels,
result terms, referenced owner documents, and main-only release readiness
settings.

## Boundaries

Validation fixtures may define expected repository validation behavior.

They must not:

- create branches, commits, tags, releases, or pull requests;
- install Blueprint into another repository;
- generate product code;
- execute a product runtime;
- call GitHub or other external services;
- hide manual validation gaps.
