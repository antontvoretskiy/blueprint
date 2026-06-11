# Blueprint Validation Scripts

These scripts provide repeatable checks for the documentation-first Blueprint bundle.

They are not a CLI, installer, runtime, workflow engine, or code generator.

## Included Checks

| Script | Purpose |
| --- | --- |
| `check_quality.py` | Runs manifest, link, wording, template index, and release consistency checks |

## Usage

Run all quality checks:

```bash
make quality
```

Or run the script directly:

```bash
python3 scripts/check_quality.py
```

## Boundaries

Validation scripts may check repository files, public claims, links, and template references.

They must not:

- install Blueprint into another repository;
- generate product code;
- call external services;
- modify files;
- replace human review for documentation truthfulness.
