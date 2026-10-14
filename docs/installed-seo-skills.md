# Installed SEO skills

All four collections listed in the guide are installed in this repository: **72 portable skill entry points**, with **309 pinned upstream source/support files**. The original link directory remains available.

## Use with your agent

| Agent | Installed project location | Example |
| --- | --- | --- |
| Codex and agents supporting the shared convention | .agents/skills/ | Ask to use `illyism-seo-title-optimization`. |
| Claude Code | .claude/skills/ | Use the skill picker or `/illyism-seo-title-optimization`. |
| Cursor | .cursor/skills/ | Select the skill, or request it by name. |
| Gemini CLI | .gemini/skills/ | Enable project skills as required by your client, then request the named skill. |
| GitHub Copilot | .github/skills/ | Request the named skill in an agent-capable client. |
| Other models/agents | AGENTS.md and .agents/skills/ | Explicitly read a named SKILL.md and its vendored workflow. |

These are model-independent Markdown workflows, not Codex-only plugins. Automatic discovery depends on the client and version, not the underlying model. If a client does not discover project skills, ask it to read the exact entry point. Reload/reopen an already-running agent after pulling the repository. A hosted chat without repository access, browsing or tools cannot execute a local workflow just by knowing its name.

Example request:

> Read AGENTS.md, then .agents/skills/illyism-seo-title-optimization/SKILL.md. Audit the titles in my website repository at [path] for [site URL]. Use real page content and return a reviewable change.

For connected research:

> Use openseo-keyword-research for [site URL]. Check whether OpenSEO MCP is connected. If it is not, tell me which data export you need; do not invent metrics.

The seo-links repo is the skill workspace and reference hub, not an application website. Specify the actual website/repo to audit or edit.

## Installed collections and dependencies

| Collection | Skills | Requirements |
| --- | ---: | --- |
| OpenSEO | 12 | Connect OpenSEO MCP in the chosen client for live data. Self-hosted external research uses DataForSEO. |
| Jev SEO | 1 | Python 3.10+, its requirements.txt, and Pango for PDF rendering. TypeSafe key for Jev judgments; optional PageSpeed/DataForSEO access. |
| NotFair | 48 | Some workflows accept URLs, repo content or exports. Live account workflows require the authorized NotFair MCP/provider connection. Local scripts may need Python/Bash, gcloud or listed dependencies. |
| Illyism | 11 | An agent able to read/edit the target repo and access actual SERPs/analytics when required. Scribiz, LinkDR and tracking services have their own access/cost requirements. |

The collections also include related content, advertising and marketing skills because the request was to install the collections in full. They are available on demand, not automatically activated for SEO tasks.

Sources are pinned in [skills-lock.json](../skills-lock.json). Entry points are namespaced by provider, so overlapping upstream names do not collide. Original workflows, scripts, references and licences live in [vendor/seo-skills](../vendor/seo-skills). Relative links are resolved from the original workflow's directory.

### Jev runtime setup

Create a dedicated environment using the Python version required by the upstream project, then install its requirements:

```sh
python -m venv .venv-jev
# Activate the environment with the command appropriate for your shell.
python -m pip install -r vendor/seo-skills/jev-seo/requirements.txt
```

On Windows, activate with `.venv-jev\\Scripts\\Activate.ps1`; on POSIX shells use `source .venv-jev/bin/activate`. Install Pango using the upstream README's OS-specific instructions if producing PDFs. Configure optional keys in your environment, never in tracked files. Set `JEVSEO_ENV_FILE` to an explicit user-controlled env file when needed.

Portable CLI invocation (works without executing the Bash launcher):

```sh
cd vendor/seo-skills/jev-seo
python -m jevseo doctor
# Return to the repository root afterwards:
cd ../../..
```

Bundled font binaries are optional; the upstream renderer falls back to system fonts. To fetch the eight original fonts and verify their pinned Git blob hashes:

```sh
python scripts/seo_skills.py fonts
```

No paid API calls or live account connections were performed as part of installation.

## Validation and adapter maintenance

```sh
python scripts/seo_skills.py check
python scripts/seo_skills.py list
python scripts/seo_skills.py sync
python -m unittest discover -s tests -v
```

Check validates every vendored source hash, every canonical skill and all five agent-layout copies. Sync regenerates existing client entry points from .agents/skills; it does not fetch new upstream versions or connect accounts. To update source versions, review the upstream diff, replace the selected source/support files and regenerate skills-lock.json with the reviewed commit and hashes. Do not silently track main.

Installation and file validation are distinct from executing all external workflows: the installed packages still need their runtimes, data and credentials. Read the selected workflow before using it. Fixed publishing quotas, automatic page merges and paid-link promotions are not adopted as repository-wide SEO rules.

## Skill catalogue

| Installed name | Source workflow |
| --- | --- |
| openseo-ai-prompt-research | [openseo/plugins/openseo/skills/ai-prompt-research/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/ai-prompt-research/SKILL.md) |
| openseo-ai-visibility-audit | [openseo/plugins/openseo/skills/ai-visibility-audit/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/ai-visibility-audit/SKILL.md) |
| openseo-competitive-landscape | [openseo/plugins/openseo/skills/competitive-landscape/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/competitive-landscape/SKILL.md) |
| openseo-competitor-analysis | [openseo/plugins/openseo/skills/competitor-analysis/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/competitor-analysis/SKILL.md) |
| openseo-keyword-clustering | [openseo/plugins/openseo/skills/keyword-clustering/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/keyword-clustering/SKILL.md) |
| openseo-keyword-research | [openseo/plugins/openseo/skills/keyword-research/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/keyword-research/SKILL.md) |
| openseo-link-prospecting | [openseo/plugins/openseo/skills/link-prospecting/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/link-prospecting/SKILL.md) |
| openseo-local-seo | [openseo/plugins/openseo/skills/local-seo/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/local-seo/SKILL.md) |
| openseo-seo-audit | [openseo/plugins/openseo/skills/seo-audit/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/seo-audit/SKILL.md) |
| openseo-seo-coach | [openseo/plugins/openseo/skills/seo-coach/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/seo-coach/SKILL.md) |
| openseo-seo-project-setup | [openseo/plugins/openseo/skills/seo-project-setup/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/seo-project-setup/SKILL.md) |
| openseo-seo-report | [openseo/plugins/openseo/skills/seo-report/SKILL.md](../vendor/seo-skills/openseo/plugins/openseo/skills/seo-report/SKILL.md) |
| jev-seo-audit | [jev-seo/SKILL.md](../vendor/seo-skills/jev-seo/SKILL.md) |
| notfair-backlink-audit | [notfair/skills/backlink-audit/SKILL.md](../vendor/seo-skills/notfair/skills/backlink-audit/SKILL.md) |
| notfair-broken-link-checker | [notfair/skills/broken-link-checker/SKILL.md](../vendor/seo-skills/notfair/skills/broken-link-checker/SKILL.md) |
| notfair-competitor-pages | [notfair/skills/competitor-pages/SKILL.md](../vendor/seo-skills/notfair/skills/competitor-pages/SKILL.md) |
| notfair-content-planner | [notfair/skills/content-planner/SKILL.md](../vendor/seo-skills/notfair/skills/content-planner/SKILL.md) |
| notfair-content-writer | [notfair/skills/content-writer/SKILL.md](../vendor/seo-skills/notfair/skills/content-writer/SKILL.md) |
| notfair-ecommerce-seo | [notfair/skills/ecommerce-seo/SKILL.md](../vendor/seo-skills/notfair/skills/ecommerce-seo/SKILL.md) |
| notfair-gemini | [notfair/skills/gemini/SKILL.md](../vendor/seo-skills/notfair/skills/gemini/SKILL.md) |
| notfair-geo-optimizer | [notfair/skills/geo-optimizer/SKILL.md](../vendor/seo-skills/notfair/skills/geo-optimizer/SKILL.md) |
| notfair-gohighlevel | [notfair/skills/gohighlevel/SKILL.md](../vendor/seo-skills/notfair/skills/gohighlevel/SKILL.md) |
| notfair-google-ads-assets | [notfair/skills/google-ads-assets/SKILL.md](../vendor/seo-skills/notfair/skills/google-ads-assets/SKILL.md) |
| notfair-google-ads-audit | [notfair/skills/google-ads-audit/SKILL.md](../vendor/seo-skills/notfair/skills/google-ads-audit/SKILL.md) |
| notfair-google-ads-copy | [notfair/skills/google-ads-copy/SKILL.md](../vendor/seo-skills/notfair/skills/google-ads-copy/SKILL.md) |
| notfair-google-ads-landing | [notfair/skills/google-ads-landing/SKILL.md](../vendor/seo-skills/notfair/skills/google-ads-landing/SKILL.md) |
| notfair-google-ads | [notfair/skills/google-ads/SKILL.md](../vendor/seo-skills/notfair/skills/google-ads/SKILL.md) |
| notfair-google-analytics | [notfair/skills/google-analytics/SKILL.md](../vendor/seo-skills/notfair/skills/google-analytics/SKILL.md) |
| notfair-hreflang-international | [notfair/skills/hreflang-international/SKILL.md](../vendor/seo-skills/notfair/skills/hreflang-international/SKILL.md) |
| notfair-image-seo | [notfair/skills/image-seo/SKILL.md](../vendor/seo-skills/notfair/skills/image-seo/SKILL.md) |
| notfair-keyword-research | [notfair/skills/keyword-research/SKILL.md](../vendor/seo-skills/notfair/skills/keyword-research/SKILL.md) |
| notfair-local-seo | [notfair/skills/local-seo/SKILL.md](../vendor/seo-skills/notfair/skills/local-seo/SKILL.md) |
| notfair-meta-ads-audit | [notfair/skills/meta-ads-audit/SKILL.md](../vendor/seo-skills/notfair/skills/meta-ads-audit/SKILL.md) |
| notfair-meta-ads-creative | [notfair/skills/meta-ads-creative/SKILL.md](../vendor/seo-skills/notfair/skills/meta-ads-creative/SKILL.md) |
| notfair-meta-ads | [notfair/skills/meta-ads/SKILL.md](../vendor/seo-skills/notfair/skills/meta-ads/SKILL.md) |
| notfair-meta-tags-optimizer | [notfair/skills/meta-tags-optimizer/SKILL.md](../vendor/seo-skills/notfair/skills/meta-tags-optimizer/SKILL.md) |
| notfair-paid-ads-amazon | [notfair/skills/paid-ads-amazon/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-amazon/SKILL.md) |
| notfair-paid-ads-chatgpt | [notfair/skills/paid-ads-chatgpt/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-chatgpt/SKILL.md) |
| notfair-paid-ads-creative | [notfair/skills/paid-ads-creative/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-creative/SKILL.md) |
| notfair-paid-ads-guide | [notfair/skills/paid-ads-guide/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-guide/SKILL.md) |
| notfair-paid-ads-integrations | [notfair/skills/paid-ads-integrations/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-integrations/SKILL.md) |
| notfair-paid-ads-launch | [notfair/skills/paid-ads-launch/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-launch/SKILL.md) |
| notfair-paid-ads-linkedin | [notfair/skills/paid-ads-linkedin/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-linkedin/SKILL.md) |
| notfair-paid-ads-optimize | [notfair/skills/paid-ads-optimize/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-optimize/SKILL.md) |
| notfair-paid-ads-reddit | [notfair/skills/paid-ads-reddit/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-reddit/SKILL.md) |
| notfair-paid-ads-review | [notfair/skills/paid-ads-review/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-review/SKILL.md) |
| notfair-paid-ads-setup | [notfair/skills/paid-ads-setup/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-setup/SKILL.md) |
| notfair-paid-ads-tiktok | [notfair/skills/paid-ads-tiktok/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-tiktok/SKILL.md) |
| notfair-paid-ads-x | [notfair/skills/paid-ads-x/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads-x/SKILL.md) |
| notfair-paid-ads | [notfair/skills/paid-ads/SKILL.md](../vendor/seo-skills/notfair/skills/paid-ads/SKILL.md) |
| notfair-programmatic-seo | [notfair/skills/programmatic-seo/SKILL.md](../vendor/seo-skills/notfair/skills/programmatic-seo/SKILL.md) |
| notfair-schema-markup-generator | [notfair/skills/schema-markup-generator/SKILL.md](../vendor/seo-skills/notfair/skills/schema-markup-generator/SKILL.md) |
| notfair-search-console | [notfair/skills/search-console/SKILL.md](../vendor/seo-skills/notfair/skills/search-console/SKILL.md) |
| notfair-seo-analysis | [notfair/skills/seo-analysis/SKILL.md](../vendor/seo-skills/notfair/skills/seo-analysis/SKILL.md) |
| notfair-seo-drift | [notfair/skills/seo-drift/SKILL.md](../vendor/seo-skills/notfair/skills/seo-drift/SKILL.md) |
| notfair-seo-page | [notfair/skills/seo-page/SKILL.md](../vendor/seo-skills/notfair/skills/seo-page/SKILL.md) |
| notfair-setup-cms | [notfair/skills/setup-cms/SKILL.md](../vendor/seo-skills/notfair/skills/setup-cms/SKILL.md) |
| notfair-sitemap-audit | [notfair/skills/sitemap-audit/SKILL.md](../vendor/seo-skills/notfair/skills/sitemap-audit/SKILL.md) |
| notfair-sxo | [notfair/skills/sxo/SKILL.md](../vendor/seo-skills/notfair/skills/sxo/SKILL.md) |
| notfair-upgrade | [notfair/skills/upgrade/SKILL.md](../vendor/seo-skills/notfair/skills/upgrade/SKILL.md) |
| notfair-wordpress | [notfair/skills/wordpress/SKILL.md](../vendor/seo-skills/notfair/skills/wordpress/SKILL.md) |
| illyism-intro | [illyism/content/intro/SKILL.md](../vendor/seo-skills/illyism/content/intro/SKILL.md) |
| illyism-scribiz | [illyism/content/scribiz/SKILL.md](../vendor/seo-skills/illyism/content/scribiz/SKILL.md) |
| illyism-blitz-copy | [illyism/copywriting/blitz-copy/SKILL.md](../vendor/seo-skills/illyism/copywriting/blitz-copy/SKILL.md) |
| illyism-understand-customers | [illyism/copywriting/understand-customers/SKILL.md](../vendor/seo-skills/illyism/copywriting/understand-customers/SKILL.md) |
| illyism-customer-journey | [illyism/marketing/customer-journey/SKILL.md](../vendor/seo-skills/illyism/marketing/customer-journey/SKILL.md) |
| illyism-diff-marketing | [illyism/marketing/diff-marketing/SKILL.md](../vendor/seo-skills/illyism/marketing/diff-marketing/SKILL.md) |
| illyism-blitz-seo | [illyism/seo/blitz-seo/SKILL.md](../vendor/seo-skills/illyism/seo/blitz-seo/SKILL.md) |
| illyism-blog-refresher | [illyism/seo/blog-refresher/SKILL.md](../vendor/seo-skills/illyism/seo/blog-refresher/SKILL.md) |
| illyism-linkdr | [illyism/seo/linkdr/SKILL.md](../vendor/seo-skills/illyism/seo/linkdr/SKILL.md) |
| illyism-seo-autopilot | [illyism/seo/seo-autopilot/SKILL.md](../vendor/seo-skills/illyism/seo/seo-autopilot/SKILL.md) |
| illyism-seo-title-optimization | [illyism/seo/seo-title-optimization/SKILL.md](../vendor/seo-skills/illyism/seo/seo-title-optimization/SKILL.md) |

## Client documentation checked

- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Cursor skills](https://cursor.com/docs/skills)
- [Gemini CLI skills](https://geminicli.com/docs/cli/skills/)
- [GitHub Copilot skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Codex skills](https://developers.openai.com/codex/skills)
