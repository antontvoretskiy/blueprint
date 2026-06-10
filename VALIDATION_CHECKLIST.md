# Blueprint Validation Checklist

Use this checklist for public-facing PRs and release preparation.

## Repository Identity

- [ ] Working repository is `antontvoretskiy/blueprint`.
- [ ] Work is on a scoped Blueprint branch.
- [ ] Source-reference repositories are not modified.
- [ ] `main` is not changed except through an explicit release PR.
- [ ] Unrelated untracked files are not staged.

## Scope

- [ ] PR has one clear scope.
- [ ] Changed files match the PR scope.
- [ ] No product implementation is added.
- [ ] No CLI, installer, automation, or integration is added unless explicitly in scope.
- [ ] README, manifest, and current state agree.

## Public Wording

- [ ] Forbidden public wording scan passes.
- [ ] Product-term scan passes.
- [ ] No private project names appear.
- [ ] No private release history appears.
- [ ] No private PR timeline appears.
- [ ] Planned work is not described as included.

## Links And Formatting

- [ ] Markdown link check passes.
- [ ] `git diff --check` passes.
- [ ] Tables render as valid Markdown.
- [ ] New files are referenced by owner or navigation docs.
- [ ] Versioned public assets include version metadata.

## Local Validation

- [ ] `make doctor` passes.
- [ ] `make config` passes.
- [ ] `make smoke` passes.
- [ ] System use-case validation suite is run when preparing public packaging, release, or branch cleanup.
- [ ] Additional checks are listed in the PR body.
- [ ] Not-run checks are reported honestly.

## Contribution Hygiene

- [ ] Commit title follows the public title standard.
- [ ] PR title follows the public title standard.
- [ ] PR body includes Problem, Solution, Scope, Validation, Risks, and Follow-ups.
- [ ] Versioned public assets include the metadata block.
- [ ] No noisy generated-change wording appears.
- [ ] No unapproved co-author trailers appear.

## Release Readiness

- [ ] `VERSION` matches release intent.
- [ ] `CHANGELOG.md` has the release entry.
- [ ] `RELEASE.md` gates are satisfied.
- [ ] `SUPPORT.md` exists and is useful.
- [ ] `SECURITY.md` exists and is useful.
- [ ] `CODE_OF_CONDUCT.md` exists.
- [ ] GitHub contribution templates exist.
- [ ] Release PR target is `main`.
- [ ] Branch cleanup is approval-gated.
