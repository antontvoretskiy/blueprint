# Blueprint Pull Request Standard

This standard defines how Blueprint PRs are titled, scoped, reviewed, validated, and merged.

## PR Principle

One PR should have one review story.

A reviewer should be able to answer:

- what changed;
- why it changed;
- which paths are in scope;
- which paths are excluded;
- how it was validated;
- what remains later.

## Title Standard

Use the public title standard from `CONTRIBUTING.md`.

Default format:

```text
type(scope): concise outcome
```

Examples:

```text
docs(core): add portable operating contracts
docs(governance): add branch and PR standards
docs(memory): add project memory templates
fix(docs): repair manifest links
```

For versioned public assets, use the title-style formats defined in `CONTRIBUTING.md`.

## Body Standard

Meaningful PRs must include:

```text
## Problem

## Solution

## Scope

## Validation

## Risks

## Follow-ups
```

## Scope Requirements

The Scope section must list:

- included paths;
- explicitly excluded paths;
- base branch;
- whether `main` changes;
- whether release state changes.

For Blueprint integration work, base should be `develop`.

For release work, base should be `main`.

## Validation Requirements

The Validation section must report commands and outcomes.

Use:

- `PASS`;
- `FAIL`;
- `NOT RUN`, with a reason.

Minimum documentation validation:

```bash
make doctor
make smoke
git diff --check
```

Public-facing PRs should also include:

- forbidden public wording scan;
- product-term scan;
- markdown links check;
- commit title quality check;
- PR title quality check;
- noisy AI phrase scan;
- bad commit wording scan.

## Review Checklist

Before requesting review, confirm:

- branch base is correct;
- one PR maps to one scope;
- owner documents are updated;
- root docs remain truthful;
- planned work is not described as included;
- private source details are absent;
- validation evidence is current;
- risks and follow-ups are explicit.

## Merge Standard

Use squash merge unless the maintainer requests otherwise.

The squash title should be the final public history line and must follow the title standard.

The squash body should preserve:

- Problem;
- Solution;
- Scope summary;
- Validation summary.

Do not add accidental co-author trailers.

## After Merge

After merge:

1. Sync the target branch.
2. Delete the merged feature branch if appropriate.
3. Run relevant validation on the target branch.
4. Report the clean-start state.
5. Start the next branch from the updated target branch.
