# Blueprint Documentation Standard

This standard defines how Blueprint documentation stays truthful, portable, and reviewable.

## Purpose

Documentation is part of the product surface.

This standard prevents:

- public docs claiming more than the repository contains;
- duplicate rules with conflicting owners;
- private source details leaking into portable docs;
- plans being presented as included assets;
- long documents becoming unrecoverable;
- examples being confused with core requirements.

## Ownership

This document owns:

- documentation status language;
- truthfulness rules;
- portability rules;
- documentation lifecycle;
- documentation size guidance;
- source-of-truth rules;
- documentation refactor expectations;
- forbidden documentation patterns.

PR structure is owned by `governance/docs/pr-standard.md`.

Validation evidence is owned by `governance/docs/verification-standard.md`.

Rule ownership is mapped in `governance/docs/governance-index.md`.

## Dependencies

This standard depends on:

- `README.md` for public entrypoint claims;
- `OPEN_SOURCE_SPEC.md` for product definition and scope;
- `ARCHITECTURE.md` for layer boundaries;
- `BUNDLE_MANIFEST.md` for included, planned, and excluded status;
- `CONTRIBUTING.md` for public contribution workflow;
- `governance/docs/governance-index.md` for canonical ownership.

## Documentation Philosophy

Documentation must describe the repository as it is, not as the project hopes it will be.

Future work may be documented, but it must be clearly marked as planned.

Blueprint documentation should help a new contributor recover context from the repository without needing old chat history.

## Documentation Ownership Model

Every durable rule should have one canonical owner.

Summary documents may:

- introduce a topic;
- link to the owner;
- state current status;
- explain how to navigate the repository.

Summary documents must not redefine full standards already owned elsewhere.

## One Document = One Responsibility

Each document should answer one primary question.

Examples:

| Document | Primary question |
| --- | --- |
| `README.md` | What is Blueprint and how do I start? |
| `OPEN_SOURCE_SPEC.md` | What is the product boundary? |
| `ARCHITECTURE.md` | How are layers separated? |
| `BUNDLE_MANIFEST.md` | What is included, planned, and excluded? |
| `CONTRIBUTING.md` | How do contributors work safely? |
| `governance/docs/governance-index.md` | Which document owns each rule? |

If a document starts answering several unrelated questions, split it or link to owners.

## Documentation Lifecycle

Documentation can move through these states:

```text
planned
drafted
included
validated
deprecated
removed
```

State changes should be visible in the relevant owner document or manifest.

A documentation PR should not mark a layer as included unless the files exist in the repository.

## Documentation Status Model

Use clear status terms:

| Term | Meaning |
| --- | --- |
| Included | Present in the repository now |
| Planned | Intended later, not present yet |
| Example | Educational sample, not required installation |
| Template | Reusable artifact, when the template exists |
| Excluded | Deliberately outside the scope |
| Deprecated | Still present but no longer recommended |
| Removed | No longer present or supported |

Avoid ambiguous terms when users need to know whether something exists.

## Documentation Size Standard

Documents should be long enough to be useful and short enough to be reviewed.

Use:

- tables for ownership maps;
- numbered steps for procedures;
- bullets for review rules;
- code blocks for exact commands or naming formats;
- links to owner documents for detailed standards.

When a document becomes too broad:

1. Identify the primary question.
2. Move unrelated rules to the correct owner.
3. Leave a short link from the summary.
4. Update the governance index if ownership changed.

## Source-Of-Truth Documentation Rules

For every important rule:

```text
one rule
one canonical owner
short links from summaries
no duplicated standard
```

If two documents conflict, resolve ownership through `governance/docs/governance-index.md`.

Do not solve conflicts by adding a third conflicting summary.

## Documentation Completeness Rules

A public document is complete enough when it states:

- what exists now;
- what is planned later;
- what is excluded;
- how to validate claims;
- which owner document contains deeper rules;
- what a contributor should do next.

Completeness does not mean documenting every conversation.

## Documentation Migration Rules

When adapting rules from a source reference:

- preserve portable process logic;
- remove private product names;
- remove private release history;
- remove product-specific incidents;
- replace concrete project paths with placeholders or Blueprint paths;
- convert project state into templates or examples only when that layer exists;
- re-check public status after adaptation.

Do not copy product memory directly into Blueprint.

## Documentation Refactor Rules

Refactor documentation when:

- a document owns too many rules;
- the same rule appears in multiple places;
- public claims no longer match files;
- examples are mixed with core requirements;
- future work is presented as included.

Refactor in scoped PRs. Do not hide documentation restructuring inside unrelated work.

## Documentation Inheritance Rules

A new document may inherit rules by linking to an owner.

It should not duplicate the owner text unless duplication is necessary for a reusable template.

When a template repeats a rule, keep the wording short and point back to the canonical Blueprint owner when practical.

## Root Document Responsibilities

| Document | Responsibility |
| --- | --- |
| `README.md` | Public landing page and current status |
| `OPEN_SOURCE_SPEC.md` | Product definition and scope |
| `ARCHITECTURE.md` | Core, extension, and example layer boundaries |
| `BUNDLE_MANIFEST.md` | Included, planned, and excluded content |
| `CONTRIBUTING.md` | Public contribution workflow |

Root docs may summarize governance rules, but canonical rules live in the owner documents listed in `governance/docs/governance-index.md`.

## Portability Rules

Blueprint docs must be reusable in any repository.

Do not include:

- private product names;
- private domain names;
- private repository paths;
- product PR numbers;
- product release history;
- incident details;
- private project memory;
- source-reference anchors.

Use placeholders when needed:

- `<PROJECT_NAME>`;
- `<OWNER>/<REPO>`;
- `<DOMAIN_A>`;
- `<DOMAIN_B>`;
- `<PROJECT_SPECIFIC_MODULE>`;
- `<PROJECT_SPECIFIC_MILESTONE>`.

## PR Requirements

Documentation PRs should report:

- changed documents;
- public claims changed;
- validation run;
- private-term scan result;
- planned work that remains outside the PR.

If documentation changes public status, update `BUNDLE_MANIFEST.md` and any affected README or architecture sections in the same PR.

## Future Documentation Automation

Blueprint may add optional documentation checks later.

Automation should enforce rules owned here. It must not become a second owner for documentation policy.

## Forbidden Documentation Patterns

Do not:

- describe planned work as included;
- claim automation before automation exists;
- claim templates before template files exist;
- claim examples before example files exist;
- copy private source documents without sanitization;
- store private project memory in public docs;
- duplicate full standards across multiple files;
- use vague status language when existence matters;
- bury known limitations outside the Risks or Follow-ups sections.

## Documentation Review Checklist

Before merging documentation changes, confirm:

- owner documents are updated;
- summaries link instead of redefining;
- public claims match repository contents;
- status terms are accurate;
- private source details are absent;
- manifest changes are included when status changes;
- links are valid;
- validation evidence is reported;
- future work is clearly separated from included work.
