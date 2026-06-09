# Blueprint Security Policy

This document defines the public security reporting policy for Blueprint.

For framework security expectations inside Blueprint-governed work, see `core/SECURITY.md`.

## Supported Versions

| Version | Supported |
| --- | --- |
| Current release candidate | Yes |
| Older unreleased snapshots | No |

Until a release PR lands on `main`, the supported public target is the current release candidate on `develop`.

## Reporting A Vulnerability

Do not publish sensitive vulnerability details in a public issue.

Use GitHub private vulnerability reporting for this repository when available.

If private reporting is not available, contact the maintainers through the repository owner profile before publishing details.

## What To Include

Include:

- affected file or workflow;
- impact;
- reproduction steps;
- expected behavior;
- actual behavior;
- affected version;
- whether private data is involved.

Do not include secrets, tokens, private keys, private URLs, customer data, or private project memory.

## Security Scope

In scope:

- documentation that could cause unsafe handling of private data;
- template instructions that could leak secrets;
- contribution flow that could expose sensitive reports;
- local environment defaults that could conflict with safe development.

Out of scope:

- product implementation in adopter repositories;
- application vulnerabilities outside Blueprint assets;
- third-party services not included in this repository;
- runtime isolation that Blueprint does not provide.
