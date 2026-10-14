---
name: jev-seo-audit
description: "jev-seo workflow: Jev SEO audit. Use when this specific workflow is requested."
---

# jev seo audit

This is an installed entry point, not a web bookmark.

1. Locate this repository root and read `AGENTS.md` and `docs/installed-seo-skills.md` for scope and dependencies.
2. Read `vendor/seo-skills/jev-seo/SKILL.md` completely. Resolve its relative references against that file's own directory, not this entry point. Supporting source files are vendored alongside it.
3. Follow the workflow using the current agent's equivalent tools. Claude/Codex-specific wording does not require a particular model. When a required connector, API, runtime or permission is missing, report that limitation rather than inventing results.
4. For Jev CLI commands on Windows or other non-Bash hosts, use `python -m jevseo` from `vendor/seo-skills/jev-seo`; the upstream `bin/jevseo` file is a Bash launcher and must not be passed to Python.
5. Treat third-party publishing quotas, SEO scores and ranking promises as heuristics. Review changes before publishing. Installation does not authorize purchases, account connections, outbound messages or destructive changes.

Upstream: https://github.com/AgriciDaniel/jev-seo/blob/55a184a3b0d09565a4c84268f725a47784e62528/SKILL.md
