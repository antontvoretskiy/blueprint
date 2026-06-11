# Blueprint Git Policy

This policy defines repository identity checks, branch roles, branch naming, commit naming, merge flow, and branch cleanup for Blueprint.

## Purpose

The Git policy keeps repository history reviewable and recoverable.

It prevents:

- work in the wrong repository;
- direct changes to release-ready state;
- branch names tied to people instead of scope;
- mixed-scope PRs;
- stale branches that no longer match the target branch;
- source-reference repositories being changed by accident;
- local generated files leaking into public history.

## Ownership

This document owns:

- repository identity checks;
- branch role definitions;
- branch naming rules;
- commit naming rules;
- branch lifecycle;
- stale branch handling;
- merge and cleanup rules.

The PR body structure is owned by `governance/docs/pr-standard.md`.

Validation language is owned by `governance/docs/verification-standard.md`.

## Dependencies

This policy depends on:

- `CONTRIBUTING.md` for public contribution expectations;
- `governance/docs/pr-standard.md` for PR scope and merge requirements;
- `governance/docs/verification-standard.md` for evidence reporting;
- `governance/docs/governance-index.md` for rule ownership.

When those documents conflict, use `governance/docs/governance-index.md` to identify the canonical owner.

## Repository Identity Rule

Before creating a branch, editing files, committing, pushing, or opening a PR, confirm:

- current working directory;
- `git remote -v`;
- current branch;
- target base branch;
- worktree status;
- whether any ignored local files are expected.

Blueprint work must happen only in the Blueprint repository.

Source-reference repositories are read-only inputs. Do not create branches, commits, tags, pushes, or PRs in a source-reference repository unless maintainers explicitly approve it for that repository.

## Canonical Branch Rule

The public Blueprint repository exposes one long-lived distribution branch:

| Branch | Role |
| --- | --- |
| `main` | Release-ready public state |

Maintainers may use local or private integration branches before publication. Those branches are maintainer workflow details, not public distribution branches.

Normal public contribution work starts from current `main` and targets `main` unless maintainers explicitly request a private integration, hotfix, or release branch.

Do not use `main` as a scratch branch.

Adopting repositories may use either `main` only or `main` plus an integration branch. The chosen model must be recorded in the adopter repository Git policy and Project Memory.

## Branch Naming Standard

Branch names must describe the scope of the work, not the person doing it.

Approved branch families:

| Branch family | Purpose |
| --- | --- |
| `docs/<scope>` | Documentation, governance, framework contracts, templates, examples, and checklists |
| `fix/<scope>` | Small corrections, broken links, formatting repairs, or wording fixes |
| `chore/<scope>` | Repository maintenance with no public framework semantics |
| `release/vX.Y.Z` | Release preparation when maintainers choose a dedicated release branch |
| `hotfix/<scope>` | Urgent release-state repair with maintainer approval |

Good examples:

```text
docs/core-operating-contracts
docs/governance-standards
docs/project-memory-templates
docs/recovery-checklists
fix/manifest-links
release/v0.2.0
```

Avoid:

- branch names based on a person;
- vague labels such as `wip`, `misc`, or `updates`;
- branch names that combine unrelated scopes;
- pre-created future branches with no active work.

## Scope Mapping

Use this mapping unless maintainers approve a more specific branch name:

| Work area | Branch pattern |
| --- | --- |
| Public bootstrap docs | `docs/bootstrap-*` |
| Core contracts | `docs/core-*` |
| Governance standards | `docs/governance-*` |
| Project Memory materials | `docs/memory-*` |
| Recovery materials | `docs/recovery-*` |
| Guardian materials | `docs/guardian-*` |
| Templates | `docs/templates-*` |
| Examples | `docs/examples-*` |
| Checklists | `docs/checklists-*` |
| Release preparation | `release/vX.Y.Z` |
| Small repairs | `fix/*` |

If a PR needs more than one branch pattern, split it unless maintainers explicitly accept the combined scope.

## Branch Purpose Categories

Every branch should have one purpose:

| Category | Allowed change type |
| --- | --- |
| Bootstrap | Public presentation, root docs, local preview scaffolding |
| Core | Agent entrypoint, task routing, lifecycle, handoff, security baseline |
| Governance | Branch, PR, verification, documentation, ADR, and engineering standards |
| Memory | Project Memory structure and recovery-oriented state templates |
| Template | Reusable files intended to be copied into other repositories |
| Example | Educational sample implementation of Blueprint adoption |
| Checklist | Reviewable acceptance criteria and manual validation lists |
| Release | Version preparation, changelog, manifest, release status updates |

Do not mix release preparation with unrelated framework changes.

## Commit Naming Standard

Use:

```text
type(scope): concise outcome
```

Examples:

```text
docs: bootstrap blueprint public repository
docs(core): add portable operating contracts
docs(governance): add branch and PR standards
docs(memory): add project memory templates
fix(docs): repair manifest links
docs(release): prepare blueprint v0.1.0
```

For versioned public assets, maintainers may use:

```text
[Template] Add project memory templates v0.2.0
[Checklist] Add recovery checklist v0.2.0
[Example] Add AI product adoption example v0.3.0
[Release] Prepare Blueprint v0.1.0
```

Commit messages must not include noisy or process-only wording such as:

- vague update labels;
- work-in-progress labels;
- accidental tool provenance;
- unapproved co-author trailers;
- uncertainty phrases in the title.

## Commit Scope Rule

A commit should explain the durable outcome.

For meaningful changes, include a body with:

- Problem;
- Solution;
- Scope;
- Validation;
- Risks;
- Follow-ups.

Small typo or link fixes may use a title-only commit if the title is specific.

## Branch Lifecycle

Public main-only lifecycle:

```text
sync main
create scoped branch from main
make scoped changes
run validation
commit intentionally
open PR into main when public review is needed
review
squash merge
delete merged branch
run post-merge validation
```

Maintainer private-integration lifecycle:

```text
sync release baseline
work in local/private integration branch
validate release-ready state
publish only the validated release state to main
tag or create GitHub Release only after explicit approval
```

Release branches follow the release process and target `main`.

## Branch Reuse Rule

Do not reuse an old branch for unrelated work.

Reuse is allowed only when:

- the branch is still open for the same scope;
- the target base has not moved in a way that changes review context;
- the PR remains understandable as one review story.

When in doubt, create a fresh branch from the updated target branch.

## Branch Ownership Rule

The branch owner is responsible for:

- keeping the branch aligned with its target;
- keeping the PR scope narrow;
- removing unrelated local files before commit;
- reporting validation honestly;
- deleting the branch after merge when it is no longer needed.

Ownership does not override governance rules.

## Branch Age Guidance

A branch becomes risky when:

- the target branch has moved substantially;
- the PR has no recent validation;
- the diff has accumulated unrelated scope;
- the branch name no longer matches the content.

Refresh or split stale branches before review.

## Stale Branch Policy

For a stale branch:

1. Re-check repository identity and target base.
2. Inspect the diff against the target branch.
3. Decide whether to rebase, merge target, split scope, or close and recreate.
4. Re-run validation after the branch is refreshed.
5. Report the stale-branch handling in the PR body when it affects review.

Do not hide stale-branch repair inside an unrelated PR.

## Squash Merge Cleanup Rule

Squash merge is preferred for Blueprint PRs.

The squash title becomes the public history line and must follow the commit naming standard.

The squash body should preserve the meaningful review record:

- Problem;
- Solution;
- Scope;
- Validation;
- Risks;
- Follow-ups.

Do not add accidental tool provenance or unapproved co-author trailers.

## Stacked PR Policy

Stacked PRs are allowed only when maintainers approve the dependency chain.

Each stacked PR must state:

- base branch;
- parent PR, if any;
- paths in scope;
- paths out of scope;
- validation that belongs to this layer;
- what becomes valid only after the parent merges.

When a parent PR merges, refresh dependent branches before review.

## Dirty Worktree Policy

Before staging, inspect the worktree.

If unrelated files exist:

- do not stage them silently;
- do not delete user work;
- stage explicit paths only;
- mention ignored local files only when they affect validation or environment setup.

## Multi-Checkout Policy

When multiple local checkouts exist, repository identity checks are required before:

- branch creation;
- file edits;
- commits;
- pushes;
- PR creation.

The active checkout must match the intended repository and remote.

## Generated And Local Files Policy

Do not commit:

- local environment files;
- generated preview artifacts that are not part of the public repository;
- logs;
- cache files;
- editor metadata;
- private credentials;
- local dependency directories.

Generated public assets may be committed only when:

- they are intentionally part of the product presentation;
- their source or generation process is documented when relevant;
- validation confirms they render or link correctly.

## Branch Cleanup Safety Levels

| Action | Requirement |
| --- | --- |
| Delete merged local branch | Allowed after confirming merge |
| Delete merged remote branch | Allowed after confirming PR merge and no dependent PR needs it |
| Delete unmerged local branch | Requires maintainer approval or clear abandoned scope |
| Delete unmerged remote branch | Requires maintainer approval |
| Rewrite published history | Requires explicit maintainer approval |

## Merge Policy

Public contribution PRs:

- target `main` unless maintainers explicitly request another base;
- use squash merge by default;
- include current validation evidence;
- avoid unrelated root-doc status changes.

Release PRs:

- target `main`;
- name the release version;
- verify public status documents;
- summarize what moves into release-ready state.

## Relationship To PR Standard

This policy defines branch and commit mechanics.

`governance/docs/pr-standard.md` defines PR title, body, scope, review, and merge expectations.

## Relationship To Verification Standard

This policy requires validation before commit, PR, merge, and post-merge handoff.

`governance/docs/verification-standard.md` defines the accepted validation terms and evidence levels.

## Review Checklist

Before opening or merging a PR, confirm:

- repository identity is correct;
- branch starts from the expected base;
- branch name matches one scope;
- changed paths match the branch purpose;
- no source-reference repository was changed;
- no unrelated local files are staged;
- commit title follows the naming standard;
- PR targets the correct branch;
- validation is current;
- branch cleanup plan is clear.
