# Blueprint Documentation Standard

This standard defines how Blueprint documentation stays truthful, portable, and reviewable.

## Documentation Principle

Documentation must describe the repository as it is, not as the project hopes it will be.

Future work may be documented, but it must be clearly marked as planned.

## Status Language

Use clear status terms:

| Term | Meaning |
| --- | --- |
| Included | Present in the repository now |
| Planned | Intended later, not present yet |
| Example | Educational sample, not required installation |
| Template | Reusable artifact, when the template exists |
| Excluded | Deliberately outside the scope |
| Deprecated | Still present but no longer recommended |

Avoid ambiguous terms when users need to know whether something exists.

## Truthfulness Rules

- Do not claim automation unless the repository contains working automation.
- Do not claim templates unless template files exist.
- Do not claim examples unless example files exist.
- Do not claim enforcement unless a validator or process exists.
- Do not claim release readiness unless release validation is complete.

Root docs should be updated when a public status changes.

## Portability Rules

Blueprint docs must be reusable in any repository.

Do not include:

- private product names;
- private domain names;
- private repository paths;
- product PR numbers;
- product release history;
- incident details;
- source-reference anchors;
- private project memory.

Use placeholders when needed:

- `<PROJECT_NAME>`;
- `<OWNER>/<REPO>`;
- `<DOMAIN_A>`;
- `<DOMAIN_B>`;
- `<PROJECT_SPECIFIC_MODULE>`;
- `<PROJECT_SPECIFIC_MILESTONE>`.

## Structure Rules

Use headings that match the reader's task.

Prefer:

- short sections;
- tables for ownership maps;
- numbered steps for procedures;
- explicit included and excluded lists;
- links to canonical owner documents.

Avoid duplicating full standards across multiple files.

## Root Document Responsibilities

| Document | Responsibility |
| --- | --- |
| `README.md` | Public landing page and current status |
| `OPEN_SOURCE_SPEC.md` | Product definition and scope |
| `ARCHITECTURE.md` | Layer boundaries |
| `BUNDLE_MANIFEST.md` | Included, planned, and excluded content |
| `CONTRIBUTING.md` | Public contribution workflow |

Root docs may summarize governance rules, but canonical rules live in the owner documents listed in `governance/docs/governance-index.md`.

## PR Requirements

Documentation PRs should report:

- changed documents;
- public claims changed;
- validation run;
- private-term scan result;
- planned work that remains outside the PR.

If documentation changes public status, update `BUNDLE_MANIFEST.md` and any affected README or architecture sections in the same PR.
