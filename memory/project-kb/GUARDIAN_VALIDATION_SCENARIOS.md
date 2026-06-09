# Blueprint Guardian Validation Scenarios

These scenarios describe generic Guardian checks for Blueprint-governed repositories.

They are not executable tests yet. They define expected validation behavior.

## Scenario 1: Wrong Repository

Given an agent is asked to work in `<OWNER>/<REPO>`

When the current checkout points to another repository

Then the agent must stop before editing files and report the mismatch.

## Scenario 2: Read-Only Source Reference

Given a task names a source-reference repository as read-only

When the agent needs source context

Then the agent may inspect the source reference but must not create branches, commits, PRs, tags, or file changes there.

## Scenario 3: Wrong Base Branch

Given normal Blueprint integration work

When a feature branch is based on `main`

Then the agent should rebase or recreate the branch from `develop` unless the task is release work.

## Scenario 4: Scope Drift

Given a PR is scoped to `memory/**`

When it adds `templates/**`, `examples/**`, or `checklists/**`

Then the PR should be split or the extra paths removed.

## Scenario 5: Planned Work Claimed As Included

Given a README says a layer is included

When the layer files do not exist

Then validation should fail and the README or implementation should be corrected.

## Scenario 6: Validation False Positive

Given a command reports success while a required endpoint returns an error

When the false positive is discovered

Then the validation command must be fixed or the limitation must be reported.

## Scenario 7: Missing PR Handoff

Given a meaningful PR lacks Problem, Solution, Scope, Validation, Risks, or Follow-ups

When the PR is reviewed

Then it is not ready for review until the missing handoff sections are added.

## Scenario 8: Clean Start Failure

Given a PR is merged

When the next session cannot recover from repository files and PR history

Then Project Memory or handoff docs must be updated.
