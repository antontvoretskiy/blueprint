# Blueprint Core Security Baseline

This document defines the portable security baseline for Blueprint-governed work.

It is a framework rule document, not a substitute for a repository-specific vulnerability disclosure policy. A public project may add a root `SECURITY.md` later for maintainer contact and private reporting details.

## Security Principles

Blueprint security starts with repository boundaries:

- know which repository is being changed;
- know which branch is being changed;
- know which paths are allowed;
- treat source references as read-only unless explicitly approved;
- do not copy private project data into portable framework files;
- report validation honestly.

## Secret Handling

Do not commit:

- API keys;
- tokens;
- passwords;
- session strings;
- private certificates;
- local environment files;
- private URLs;
- sensitive logs;
- private customer or user data.

Use `.env.example` for non-secret defaults. Keep real local values in ignored files such as `.env.local`.

## Source Reference Handling

When adapting content from a private or product-specific source:

1. Read only what is needed.
2. Do not modify the source repository.
3. Remove private names, domains, paths, incidents, owners, release history, and PR numbers.
4. Replace product-specific details with placeholders.
5. Run a product-term scan before opening a public PR.

## Dependency And Tooling Changes

Do not add dependencies, package managers, installers, GitHub Actions, MCP integration, automation, runtime support, or code generation without explicit approval.

When tooling is approved later, document:

- why the dependency is needed;
- what it can access;
- how it is pinned or versioned;
- how it is validated;
- how it can be removed.

## Validation Expectations

For public documentation changes:

```bash
make doctor
make smoke
git diff --check
```

Also run scans for:

- forbidden public wording;
- private product terms;
- noisy AI phrases;
- bad commit wording.

For future executable tooling, add tests that verify failure behavior, not only success behavior.

## Sensitive Reports

Do not publish sensitive vulnerabilities or leaked private data in a public issue.

Use the repository's configured private security reporting channel when one exists. If no private channel exists, contact the maintainers through the channel listed by that repository before publishing details.

## Security Non-Goals

Blueprint core does not provide:

- runtime sandboxing;
- agent execution isolation;
- secret management service;
- dependency scanner;
- CI enforcement;
- access control system;
- incident response process.

Blueprint can define expectations for those controls, but the adopting repository must implement them.
