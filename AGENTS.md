# SEO Links agent instructions

This repository is a curated resource hub and a portable SEO skill workspace. It is not the website a user wants audited unless they explicitly say so. Ask for the target website/repository when it is missing; never publish generated SEO pages into this link catalogue by default.

## Installed skills

See [installed skill catalogue](docs/installed-seo-skills.md) and [pinned manifest](skills-lock.json). Canonical entry points live in .agents/skills; matching entry points are committed for Claude Code, Cursor, Gemini CLI and GitHub Copilot. Read the chosen SKILL.md and its vendored upstream workflow on demand. Do not load or execute all 72 workflows at startup.

- OpenSEO: connected keyword research, clustering, local SEO, competitor analysis and audits; requires OpenSEO MCP for live data.
- Jev SEO: local crawl/audit/report workflow; Python dependencies and optional APIs; see its vendored README.
- NotFair: SEO, analytics and related marketing workflows; live account work needs the appropriate authorized connector.
- Illyism: title optimization, content refreshes, comparison pages and SEO planning; connected data is needed where the workflow requests it.

Prefer repository-prefixed skill names to avoid collisions. Resolve references from the vendored workflow directory. Translate tools to the host agent's equivalents; a Markdown workflow does not grant unavailable tools or make a model capable of browsing by itself.

## Work rules

Use verified input data and preserve provenance. Do not invent keyword volumes, rankings, citations, customer claims or business facts. Distinguish source claims, heuristics and documented requirements. Do not adopt fixed page/link quotas, automatic page merging, paid ranking links or fake identities as default SEO requirements.

Existing user authorization governs actions. Installing these workflows alone does not authorize external posts/messages, purchases, credentials or account connections, deployments or destructive changes. Draft proposed changes and verify them before publishing within the task's authorized scope. Never store credentials in tracked files. Use supplied exports if a live connector is unavailable and report gaps honestly.

For this hub, deduplicate across README.md, data/resources.json and data/destinations.json. Keep existing collapsible Markdown groups, their counts and navigation intact. Preserve upstream vendor files and licences; keep local adjustments in adapters and documentation. Do not run installed third-party skills automatically.
