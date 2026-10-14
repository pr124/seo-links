# Portable SEO Skills Implementation Plan

> For agentic workers: implement inline with superpowers:executing-plans.

**Goal:** Install all four listed skill collections with portable discovery, supporting files and verified provenance.
**Architecture:** Preserve pinned upstream files in vendor/seo-skills. Namespaced SKILL.md entry points route five agent layouts to those sources.
**Tech Stack:** Markdown, JSON and Python standard library.
**Spec:** User request of 14 October 2026: install all listed skills in seo-links and support agents beyond Codex.

## Constraints and review focus

- Preserve the link catalogue and all original source records.
- Do not connect accounts, purchase services or run live campaigns.
- Namespace overlapping skills; retain relative dependency layout and licences.
- Pin file hashes; reject altered sources, missing adapters and paths outside the workspace.
- Distinguish installed source from runtime/API readiness. Optional Jev fonts use a checksum-verified download and system-font fallback.

## Tasks

- [x] Read and pin four upstream revisions; enumerate 72 entry points and dependent files.
- [x] Vendor portable runtime sources, licences, scripts and references, excluding development CI, screenshots and sample output.
- [x] Add shared/Claude/Cursor/Gemini/Copilot entry points plus repository guidance.
- [x] Add validation, adapter synchronization and optional font download commands.
- [x] Test missing adapters, source tampering, adapter repair and path traversal using temporary workspace fixtures.
- [x] Validate all installed source hashes and adapters; compile Python source and review relative dependencies.
- [x] Validate installation and prepare the reviewed GitHub tree; verify all resulting tree paths/blob hashes before updating main.

## Implementation rulings

- Existing session authorization covers direct repository updates; continue without another approval question.
- Portable entry points preserve upstream workflows in vendor paths instead of rewriting model-specific tools into invented equivalents.
- Jev font binaries cannot be transferred by the text-only GitHub reader. They are optional in upstream code; provide pinned downloads and preserve font licences.
- No actual client login or API work is implied by installation; external runtimes/providers remain explicit dependencies.

## Final review

An independent reviewer confirmed source-integrity validation and active workflow links. Found one important portability issue: the Jev Bash launcher was incorrectly shown as a Python command. Corrected the guide and all Jev adapters to run python -m jevseo from the vendored runtime directory. Live account workflows, runtime dependency installation and actual client discovery remain untested.
