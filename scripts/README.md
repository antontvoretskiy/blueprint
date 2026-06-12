# Blueprint Validation Scripts

These scripts provide repeatable checks for the documentation-first Blueprint bundle.

They are not a CLI, installer, runtime, workflow engine, or code generator.

## Included Checks

| Script | Purpose |
| --- | --- |
| `check_quality.py` | Runs manifest, link, wording, template index, and release consistency checks |
| `check_validation_fixtures.py` | Validates system use-case, process-level, and release-readiness fixtures |
| `export_context.py` | Validates context export manifests and writes ordered context bundles |

Release consistency accepts the current `VERSION` as either the last released
version or the next release target. This keeps release-preparation branches
truthful before a GitHub Release or tag is published.

## Usage

Run all quality checks:

```bash
make quality
```

Generate context bundles:

```bash
make context-export
make context-chat
```

Or run the script directly:

```bash
python3 scripts/check_quality.py
python3 scripts/check_validation_fixtures.py
python3 scripts/export_context.py check
python3 scripts/export_context.py export
python3 scripts/export_context.py chat
```

## Boundaries

Validation scripts may check repository files, public claims, links, and template references.
They may also check versioned validation fixtures for shape, required IDs,
expected process levels, and owner-document references.
They may check context export manifests and write generated context bundles
under ignored output paths.

They must not:

- install Blueprint into another repository;
- generate product code;
- call external services;
- modify files;
- replace human review for documentation truthfulness.
