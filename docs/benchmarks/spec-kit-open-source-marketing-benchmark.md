# Spec Kit Open Source Repository Benchmark

Status: canonical presentation and marketing-structure reference for Blueprint.

Scope: use this as a benchmark for repository packaging, README narrative, docs navigation, community entry points, and open-source value communication. Do not treat it as a product architecture or implementation reference.

Source snapshot:

- Repository: https://github.com/github/spec-kit
- Public README: https://github.com/github/spec-kit?tab=readme-ov-file
- Documentation site: https://github.github.io/spec-kit/
- Local inspection commit: `90832d19bf7dcdaacc86301ea1e3cf85a9377b7d`
- Snapshot date: 2026-06-09

## Why This Is The Benchmark

Spec Kit presents itself as a complete open-source product, not just a code dump. The repository answers the visitor's first questions in a deliberate order:

1. What is this?
2. Why should I care?
3. Can I try it immediately?
4. Does it work with my tools?
5. Can I customize it for my workflow or organization?
6. Is there a community and contribution path?
7. Where do I go for deeper reference?

The repo combines marketing, onboarding, reference, governance, and community growth in one coherent surface.

## README Pattern

Spec Kit's README structure is a strong default for Blueprint:

1. Brand signal: logo, project name, compact tagline.
2. Value proposition: one concise sentence focused on user outcome.
3. Trust badges: release, stars, license, documentation.
4. Table of contents: product narrative, not a random file index.
5. Concept explanation: a short framing section that names the category.
6. Fast path: copy-paste install/init commands before deep theory.
7. Workflow walkthrough: numbered steps from first command to useful result.
8. Media proof: video/GIF/demo after the initial quickstart.
9. Community surface: extensions, presets, walkthroughs, related projects.
10. Integration proof: supported tools and commands.
11. Customization story: how users adapt the product to their own context.
12. Philosophy: principles after utility has already been established.
13. Detailed process: expandable/deeper guide for committed users.
14. Support, acknowledgements, license.

Blueprint should mirror this ordering: value first, runnable path second, ecosystem/community third, deep design later.

## Table Of Contents Pattern

The README table of contents works because it maps to the visitor journey:

- Category definition: "What is ...?"
- Activation: "Get Started"
- Proof: video overview, community, integrations
- Product surface: commands/reference/customization
- Belief system: philosophy, phases, goals
- Requirements: prerequisites
- Depth: learn more, detailed process
- Trust and maintenance: support, acknowledgements, license

For Blueprint, the table of contents should avoid generic labels like "Overview" unless paired with a concrete user question. Prefer section names that sell clarity:

- What Is Blueprint?
- Quick Start
- Core Workflow
- Why Blueprint Exists
- Use Cases
- Integrations
- Architecture Overview
- Extending Blueprint
- Community And Contributing
- Roadmap
- Support
- License

## Value Proposition Pattern

Spec Kit's value narrative has four layers:

1. Pain: ad-hoc AI coding and "vibe coding" are unpredictable.
2. New category: Spec-Driven Development names the method.
3. Mechanism: specs, plans, tasks, and implementation artifacts feed each other.
4. Outcome: faster high-quality software with predictable outcomes.

Blueprint should use the same shape:

1. Name the painful current workflow.
2. Give the category or method a crisp name.
3. Explain the mechanism in one sentence.
4. Tie it to a measurable developer/product outcome.

Avoid vague claims like "better developer experience" unless followed by the concrete workflow that creates the benefit.

## Repository Structure Pattern

Spec Kit's top-level structure separates audience-facing surfaces from implementation:

- `README.md`: main product pitch and activation path.
- `docs/`: documentation site with landing page, quickstart, install, reference, concepts, development, and community sections.
- `src/`: implementation.
- `templates/`: reusable product artifacts.
- `extensions/`, `presets/`, `integrations/`, `workflows/`: ecosystem and customization model.
- `tests/`: validation surface.
- `.github/`: issue templates, PR template, workflows, dependabot, CODEOWNERS.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `LICENSE`, `CHANGELOG.md`, `CITATION.cff`: open-source trust and governance.
- `media/`: visual proof for README/docs.

Blueprint should treat these as presentation categories, not necessarily exact folder names. If Blueprint does not yet have extensions or presets, do not create fake folders; instead reserve the narrative slot for real extension points.

## Docs Site Pattern

The Spec Kit docs landing page repeats the README promise but adds a stronger product-site structure:

- Hero: name, promise, concise explanation, primary and secondary CTA.
- Pillars: default workflow, agent compatibility, customization, organization adoption.
- Community proof: contributors, stars, integrations, extensions, presets.
- Navigation cards: getting started, reference, community, development, concepts.
- Footer CTA: one final command block.

Blueprint should use this when it grows beyond a README. The docs homepage should not be a manual index; it should be a second landing page for committed users.

## Open Source Trust Pattern

Spec Kit makes contribution and maintenance visible:

- Structured issue templates for bugs, feature requests, agent requests, extension submissions, and preset submissions.
- Contact links route general discussion, docs, contribution, and security reports to the right places.
- PR template and contribution guide define expected validation.
- Security and support files clarify what maintainers will and will not handle.
- Community contribution types are productized as catalog submissions, not treated as loose suggestions.

Blueprint should add trust files before asking for meaningful outside contributions:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `SUPPORT.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/PULL_REQUEST_TEMPLATE.md`

## Marketing Principles To Reuse

- Put the transformation above the mechanics.
- Make the first command visible within the first screenful of serious reading.
- Show breadth through integrations and community proof, not long prose.
- Teach the mental model before exposing exhaustive reference.
- Use tables for command/reference comparison.
- Use media only when it proves a workflow, not as decoration.
- Give advanced users a path to customize, extend, or self-host.
- Treat contributors as a user segment with their own onboarding path.

## Blueprint Acceptance Checklist

Use this checklist before publishing Blueprint broadly:

- The README opens with a clear brand, tagline, and one-sentence outcome.
- The first install/run command appears before philosophy or architecture.
- The table of contents follows a visitor journey, not the repo tree.
- Every major section answers a user decision question.
- The quickstart can be executed by a new visitor without private context.
- The repo shows trust basics: license, contributing, security, support.
- There is at least one visual proof asset if the product has a UI or visible workflow.
- Docs are split into getting started, reference, concepts, development, and community once README becomes too large.
- Extension/customization points are described only when they really exist.
- Community contribution routes are structured with templates and labels.

## Anti-Patterns To Avoid

- A README that starts with implementation details before value.
- A table of contents that mirrors file names instead of user intent.
- Claims of extensibility without a concrete extension mechanism.
- Screenshots or badges that do not support a decision.
- Deep architecture explanations before the quickstart.
- Community links without contribution rules or issue templates.

## References

- Spec Kit repository: https://github.com/github/spec-kit
- Spec Kit README: https://github.com/github/spec-kit?tab=readme-ov-file
- Spec Kit docs site: https://github.github.io/spec-kit/
- Spec Kit docs navigation: https://github.com/github/spec-kit/blob/main/docs/toc.yml
- Spec Kit contribution guide: https://github.com/github/spec-kit/blob/main/CONTRIBUTING.md
- Spec Kit issue templates: https://github.com/github/spec-kit/tree/main/.github/ISSUE_TEMPLATE
