# Blueprint PR Handoff And Clean Start Standard

This standard defines how a Blueprint PR stays reviewable and how work becomes recoverable after merge.

## PR Principle

One PR should have one scope, one branch family, and one review story.

If a PR mixes unrelated layers, reviewers cannot validate boundaries or recover context reliably.

## Required PR Body

Meaningful PRs must use:

```text
## Problem

## Solution

## Scope

## Validation

## Risks

## Follow-ups
```

The PR body is a handoff artifact. It must explain what changed, what did not change, and how the change was validated.

## Scope Section

The Scope section should list:

- included paths;
- explicitly excluded paths;
- branch base;
- whether the PR targets `develop` or `main`;
- whether the change affects public release state.

For Blueprint itself, default development PRs target `develop`. Release PRs target `main`.

## Validation Section

Validation must include commands and outcomes.

Use `PASS`, `FAIL`, or `NOT RUN` with a reason.

Do not report a validation command as passing if it masked an error. If a command gives a false positive, fix the command or report the limitation.

Minimum validation for documentation PRs:

```bash
make doctor
make smoke
git diff --check
```

Public-facing documentation should also include:

- forbidden public wording scan;
- product-term scan;
- README local links check;
- commit and PR title quality check;
- noisy AI phrase scan;
- bad commit wording scan.

## Commit And PR Titles

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

Do not use placeholder or low-signal titles.

## Handoff Checklist

Before requesting review:

- repository identity is confirmed;
- base branch is correct;
- changed files match scope;
- root docs and manifest remain truthful;
- private source terms are absent;
- validation results are current;
- risks and follow-ups are listed;
- commit title and PR title are clean.

## Merge Rules

For Blueprint itself:

```text
feature branch
  -> PR into develop
  -> reviewed integration
  -> release PR from develop into main
```

`main` represents release-ready public state. `develop` is the integration branch for unreleased work.

## Clean Start Rule

After merge, the next session should recover from:

- repository files;
- merged PR body;
- commit history;
- release or integration branch state.

Old chat history must not be required.

## Clean Start Output

After merging a meaningful PR, report:

- merged PR link;
- merge commit or squash commit;
- target branch;
- deleted branches, if any;
- validation repeated after merge;
- next recommended branch;
- remaining risks.

When Project Memory exists, update the appropriate current-state or task-history files as part of the clean-start process.
