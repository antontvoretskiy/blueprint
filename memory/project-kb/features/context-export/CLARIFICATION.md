# Context Export Clarification

Feature: context-export
Version: v0.9.0
Status: Release target

| Question | Decision | Reason |
| --- | --- | --- |
| Should this be a packaged CLI? | No | The current scope is a repository-local command, not a distributed CLI or installer |
| Should the command open Codex or Cursor automatically? | No | Opening or controlling editor chat sessions is tool-specific and not portable |
| Should generated bundles be committed? | No | Bundles are generated artifacts; repository files remain canonical |
| Should the export include file contents or only paths? | Include file contents | External LLMs and databases need a self-contained context payload |
| Should there be more than one profile? | Yes | External LLM export and chat bootstrap have different context sizes |
| Should quality checks validate this feature? | Yes | The command depends on an ordered manifest and must fail when paths drift |

## Open Questions

No critical open questions block implementation.

Future optional questions:

- Whether adopters need JSONL or ZIP output.
- Whether a future packaged CLI should wrap the same manifest.
- Whether editor-specific launchers should live outside Blueprint core.
