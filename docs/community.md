# Blueprint Community Guide

This guide explains how to participate without weakening Blueprint's
source-of-truth model.

## Contribution Paths

| Contribution | Start with |
| --- | --- |
| Documentation correction | [Documentation issue form](../.github/ISSUE_TEMPLATE/docs_issue.yml) |
| Framework change proposal | [Framework change issue form](../.github/ISSUE_TEMPLATE/framework_change.yml) |
| PR with repository changes | [Contributing guide](../CONTRIBUTING.md) |
| Support question | [Support policy](../SUPPORT.md) |
| Security report | [Security policy](../SECURITY.md) |

Until dedicated example, template, or extension proposal forms exist, use the
framework change issue form and state the proposed layer clearly.

## Contribution Standards

Every meaningful contribution should state:

- the problem;
- the proposed solution;
- included paths;
- explicitly excluded paths;
- validation evidence;
- risks;
- follow-ups.

Public-facing changes must avoid private project names, private release
history, private PR timelines, and noisy generated-change wording.

## Example And Template Proposals

Example and template proposals should include:

- target audience;
- repository type;
- files to add or change;
- source of truth owner;
- validation plan;
- explicit exclusions.

Do not add product implementation, runtime code, private memory, or private
source-reference anchors to Blueprint core.

## Extension Proposals

Extensions are planned, not currently included as an implementation layer.

An extension proposal should explain:

- what repeated manual work it removes;
- why the behavior belongs outside Blueprint core;
- how adopters opt in;
- how the extension will be validated;
- why documentation and templates are not enough.

Do not create an `extensions/` implementation layer until a real extension
scope is approved.

## Review Expectations

Maintainers review for:

- one PR, one scope;
- truthful included, planned, and excluded status;
- canonical owner consistency;
- validation freshness;
- branch and release hygiene;
- public wording quality.
