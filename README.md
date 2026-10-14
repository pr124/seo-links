# SEO Links

A curated SEO toolkit for indie founders: research demand, fix technical issues, publish useful pages, build authority and measure visibility across search and AI answers.

> Browse by the job you need to do. Expand a group for its tools, articles or submission destinations.

The export contains **48 SEO source posts**, grouped into **46 source records**. After relevance review, **27 selected resources from the export**, plus **1 supplemental article**, appear below. Directory posts are merged into one destination index; incomplete articles, repeated advice and unsupported promotions remain in the [source register](docs/source-review.md).

Relevant articles use a link and a short takeaway. Partial supplied text stays labelled partial; the full article is not copied into the guide.

## Contents

- [SEO Websites, Tools, Skills and GitHub Repos](#seo-websites-tools-skills-and-github-repos)
- [Keyword Research](#keyword-research)
- [Technical SEO](#technical-seo)
- [Content and On-Page SEO](#content-and-on-page-seo)
- [Backlinks and Authority](#backlinks-and-authority)
- [Backlink Opportunities and DR](#backlink-opportunities-and-dr)
- [AI Search and GEO](#ai-search-and-geo)
- [SaaS and App SEO](#saas-and-app-seo)
- [Automation and Skills](#automation-and-skills)
- [Review Coverage](#review-coverage)

---

## SEO Websites, Tools, Skills and GitHub Repos

A single index of the reviewed SEO websites, tools, MCP integrations, reusable skills and source repositories. Expand the groups below; each project is listed once by its main purpose. Submission directories remain in [Backlink Opportunities and DR](#backlink-opportunities-and-dr).

<details>
<summary><strong>Measurement and Local Search</strong> - 5 tools</summary>

- [Google Search Console](https://search.google.com/search-console/about) - Query, click, impression and indexing reports.
- [Google Analytics](https://marketingplatform.google.com/about/analytics/) - Measure visitors and conversions after the click.
- [Google Business Profile](https://www.google.com/business/) - Manage local business information on Google.
- [Bing Webmaster Tools](https://www.bing.com/webmasters/about) - Review search performance, crawl and indexing information for your registered sites.
- [Google Merchant Center](https://business.google.com/us/merchant-center/) - Manage product data and eligible product listings across Google surfaces.

</details>

<details>
<summary><strong>Keyword Research and Competitors</strong> - 10 resources</summary>

- [Google Trends](https://trends.google.com/trends/) - Explore interest by topic, location and time.
- [Ahrefs](https://ahrefs.com/) - Keyword, competitor and backlink research.
- [Semrush](https://www.semrush.com/) - SEO research, audits and visibility tracking.
- [Ubersuggest](https://neilpatel.com/ubersuggest/) - Keyword and competitor research; [apps and integrations](https://app.neilpatel.com/en/apps-integrations) is the current destination of the supplied aitools.neilpatel.com link.
- [Mangools](https://mangools.com/) - Keyword, SERP, backlink and rank-tracking tools.
- [SE Ranking](https://seranking.com/) - Keyword research, rank tracking and site audits.

- [Keyword Tool](https://keywordtool.io/) - Find autocomplete-based keyword ideas across search platforms; advanced metrics depend on the plan.
- [SpyFu](https://www.spyfu.com/) - Research competitor organic keywords, ranking history and backlink opportunities; vendor estimates are not first-party analytics.
- [Majestic](https://majestic.com/) - Inspect backlinks, referring domains and link context; its proprietary scores are not Google ranking scores.
- [Similarweb](https://www.similarweb.com/) - Explore competitor traffic and channel research; use external measurements for context alongside your own analytics.
</details>

<details>
<summary><strong>Technical Audits and Automation</strong> - 6 resources</summary>

- [Screaming Frog SEO Spider](https://www.screamingfrog.co.uk/seo-spider/) - Crawl pages to inspect technical SEO issues.
- [DataForSEO](https://dataforseo.com/) - SEO data APIs for repeatable research workflows.
- [Index My Site](https://indexmysite.app/) - Bulk URL submissions and indexing-job tracking. Indexing is Google's decision.

- [Seobility](https://www.seobility.net/en/) - Website audits, rank monitoring and backlink analysis; review current plan limits.
- [Screpy](https://screpy.com/) - Website audits, rank tracking, performance monitoring and SEO reporting.
- [Raven Tools](https://raventools.com/) - Site auditing, rank tracking, backlink research and reporting.
</details>

<details>
<summary><strong>Choosing a Toolkit</strong> - 1 resource</summary>

- [Build an SEO toolkit around the work you need to do](https://x.com/seo_bint_ejamil/status/2108267666855416056) - Start with Search Console, Analytics, a crawler and Business Profile; add paid research tools when the strategy needs them.

</details>

<details>
<summary><strong>GitHub Repositories and Self-Hosted SEO</strong> - 6 resources</summary>

- [OpenSEO](https://github.com/every-app/open-seo) - Self-hosted keyword research, rank tracking, competitor insights, backlinks, site audits and AI visibility; includes an MCP server and agent skills. Requires a DataForSEO API key and paid usage; [MCP setup](https://openseo.so/docs/mcp).
- [Jev SEO](https://github.com/AgriciDaniel/jev-seo) - Local SEO crawler and audit-report generator, usable as a CLI or Claude Code skill. Produces PDF, spreadsheet and Markdown reports. Jev judgments require TypeSafe API access; optional extended research uses paid DataForSEO. Audit scores are heuristics, not ranking predictions. Documentation reviewed; not installed or runtime-tested.

- [advertools](https://github.com/eliasdabbas/advertools) - Python library for crawling, sitemap and robots.txt analysis, URL processing and server-log analysis. Some integrations require separate provider access.
- [GEO/AEO Tracker](https://github.com/danishashko/geo-aeo-tracker) - Self-hosted dashboard for prompts, brand mentions and citations. Live tracking uses Bright Data; analysis may use OpenRouter and other paid APIs. Demo mode uses sample data, and its heuristic scores are not ranking factors.
- [mesure-citations](https://github.com/thomasmerlaud/mesure-citations) - French-language Node CLI to maintain a fixed prompt corpus, record manual observations and compare mentions with linked citations. Does not query AI services automatically; no API key required.
- [ai-crawler-bots](https://github.com/TryGeoSuite/ai-crawler-bots) - Node CLI and GitHub Action for robots.txt checks, live reachability and log analysis. Treat its visibility score as a heuristic; check current operator documentation rather than adopting its default bot policies blindly.
</details>

<details>
<summary><strong>Reusable SEO Skills</strong> - 4 collections</summary>

- [OpenSEO Agent Skills](https://openseo.so/docs/skills/setup) - Workflows for keyword research and clustering, competitor analysis, local SEO, link prospecting and audits. Requires a working OpenSEO MCP connection; [skill source files](https://github.com/every-app/open-seo/tree/main/plugins/openseo/skills). The keyword-research skill was inspected directly.
- [Jev SEO skill workflow](https://github.com/AgriciDaniel/jev-seo/blob/main/SKILL.md) - Workflow for running the audit, checking surprising findings and producing reports. Uses the Jev SEO repo above and its API/dependency setup. Review model-generated judgments before acting on them.

- [NotFair Plugin](https://github.com/nowork-studio/notfair-plugin) - SEO and analytics workflows for audits, keyword research, sitemaps, local SEO and content. Former NotFair and toprank links resolve to this one repo. Live account workflows need its OAuth-connected MCP and authorized provider access; documentation reviewed, not installed.
- [Illyism SEO Skills](https://github.com/Illyism/seo-skills) - SEO skills for technical audits, SERP research, title improvements, content refreshes, comparison pages and AI-answer tracking. Requires an agent that reads SKILL.md plus connected research/analytics data where needed. Review before use: includes paid-backlink promotion and opinionated publishing, linking and page-merging rules; these are not universal SEO requirements. Documentation inspected; not installed or runtime-tested.

**Installed in this repo:** [72 portable skills and setup guide](docs/installed-seo-skills.md). Entry points are committed for Codex/shared agents, Claude Code, Cursor, Gemini CLI and GitHub Copilot; pinned sources and dependencies are included under `vendor/seo-skills`.

</details>

<details>
<summary><strong>SEO Reference Websites and Validators</strong> - 5 resources</summary>

- [Google Search Central](https://developers.google.com/search/docs) - Official documentation for crawl access, indexing, content, structured data and search appearance. See the [selected official references](#official-references).
- [Schema Markup Validator](https://validator.schema.org/) - Check Schema.org markup syntax and vocabulary; validation does not establish rich-result eligibility or ranking benefits.
- [Bing Webmaster API documentation](https://learn.microsoft.com/en-us/bingwebmaster/) - Documentation for registered-site search and indexing data.

- [Schema.org vocabulary](https://schema.org/docs/schemas.html) - Look up structured-data types and properties; Schema.org vocabulary is broader than Google's supported rich-result types.
- [Open Graph protocol](https://ogp.me/) - Reference for social-preview metadata; distinct from Google structured-data eligibility.
</details>

<details>
<summary><strong>Performance and Accessibility</strong> - 3 resources</summary>

- [PageSpeed Insights](https://pagespeed.web.dev/) - Inspect page performance and available real-user data; a test score is not a ranking guarantee.
- [GTmetrix](https://gtmetrix.com/) - Analyze page loads, request waterfalls and performance changes; account and plan limits apply.
- [WAVE](https://wave.webaim.org/) - Find accessibility issues and support manual evaluation; automated checks cannot establish complete compliance.

</details>

<details>
<summary><strong>Browser Extensions</strong> - 2 resources</summary>

- [Keyword Surfer](https://surferseo.com/keyword-surfer-extension/) - View keyword ideas and volume estimates in search results, with keyword collections and CSV export.
- [META SEO inspector](https://www.omiod.com/meta-seo-inspector/) - Inspect page metadata and identify missing or inconsistent on-page information.

</details>

<details>
<summary><strong>Structured Data and Metadata</strong> - 1 resources</summary>

- [Google Rich Results Test](https://search.google.com/test/rich-results) - Test URLs or code for supported Google rich-result markup; a valid test does not guarantee display.

</details>

<details>
<summary><strong>SEO Learning and Updates</strong> - 2 resources</summary>

- [Google Search Central Blog](https://developers.google.com/search/blog) - Official search announcements and documentation updates.
- [Ahrefs Blog](https://ahrefs.com/blog/) - Research and practical SEO tutorials from the tool provider; distinguish studies, opinions and current search-engine requirements.

</details>

<details>
<summary><strong>More SEO Resource Collections</strong> - 2 resources</summary>

- [teles/awesome-seo](https://github.com/teles/awesome-seo) - Broad discovery list of SEO tools and references; individual listings and claims need their own checks.
- [bmpi-dev/awesome-seo](https://github.com/bmpi-dev/awesome-seo) - SEO learning and tool collection with English and Chinese resources; includes older material and non-SEO monetization topics.

</details>

### SEO MCP Servers

MCP lets an assistant use connected tools and data. These **six integrations** cover search performance, analytics, SEO data and page research. Provider documentation was reviewed on 11 October 2026; the servers have not been installed or tested here. Official and community projects are labelled separately.

<details>
<summary><strong>Search Performance and Measurement</strong> — 2 resources</summary>

- [Google Search Console MCP](https://github.com/AminForou/mcp-gsc) - **Community.** Analyze queries, clicks, impressions and URL indexing; the server also includes property and sitemap management tools. Google credentials and access to the relevant Search Console property.
- [Google Analytics MCP](https://github.com/googleanalytics/google-analytics-mcp) - **Official / experimental.** Read Analytics account and property information and run reports to investigate traffic and outcomes. Google credentials and access to the relevant Analytics property.

</details>

<details>
<summary><strong>Keyword, Competitor and Backlink Research</strong> — 2 resources</summary>

- [Ahrefs MCP](https://docs.ahrefs.com/en/mcp/docs/introduction) - **Official.** Connect Ahrefs research data to an MCP-compatible assistant. An eligible Ahrefs plan (Lite or higher) and available API units.
- [DataForSEO MCP](https://github.com/dataforseo/mcp-server-typescript) - **Official.** Use DataForSEO APIs for SERP, keyword, backlink and on-page research. The current v3 server exposes API discovery and request tools. DataForSEO API access; usage is billed through the provider.

</details>

<details>
<summary><strong>Page Research and Content Extraction</strong> — 1 resource</summary>

- [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) - **Official.** Search, fetch and crawl web pages; useful for collecting competitor-page content for analysis. Firecrawl cloud authentication or a configured self-hosted service.

</details>

Start with Search Console to investigate your own pages, add Analytics for traffic and outcomes, and use a research provider when you need external search or backlink data. Review the permissions exposed by each server before connecting an account.

<details>
<summary><strong>Indexing Job Automation</strong> — 1 resource</summary>

- [Index My Site MCP](https://indexmysite.app/docs/mcp) - **Official.** Submit URLs, list jobs and check indexing results and credit balances. Requires an account and credits for submissions; indexing remains Google's decision.

</details>

If you publish your own MCP server, use the [MCP directories](#mcp-directories) and [GitHub lists](#mcp-and-plugin-github-lists) and the [official registry publishing guide](https://modelcontextprotocol.io/registry/quickstart).

---


## Keyword Research

Understand demand, customer language and missing answers before choosing what to publish.

<details>
<summary><strong>Search Intent and Content Gaps</strong> - 2 resources</summary>

- [AI prompt for finding gaps in the top 10 search results](https://x.com/2whazzuup/status/2108987931893645344) - Analyze intent, competitor weaknesses, original evidence, differentiated angles and the article brief before deciding whether to pursue a keyword.
- [Use Google and Reddit results to find unanswered questions](https://x.com/2whazzuup/status/2107882301669396684) - Review the leading discussions, build a more useful resource and repurpose the article for a relevant community.

</details>

<details>
<summary><strong>Trends and Long-Tail Demand</strong> - 1 resource</summary>

- [Google Trends workflow for niche and location keywords](https://x.com/borjafat/status/2098755362513953188) - Filter by category and location, narrow to long-tail topics, export the data and use it to plan content. The claimed feature novelty and faster-ranking outcome were not independently verified.

</details>

<details>
<summary><strong>Customer Reviews and Question Research</strong> - 5 destinations</summary>

- [G2](https://www.g2.com/) - Research competitor complaints and buying criteria; eligible vendors can also investigate product-profile options.
- [Capterra](https://www.capterra.com/) - Research software reviews and categories. Primary identity checked; reader access was limited.
- [Trustpilot](https://www.trustpilot.com/) - Inspect customer expectations, complaints and objections.
- [Apple App Store](https://www.apple.com/app-store/) - Research competing apps and recurring review themes.
- [Google Play](https://play.google.com/store/apps) - Review competing app listings and user problems.

</details>

---

## Technical SEO

Make important pages discoverable, crawlable and understandable, then inspect the indexing evidence.

<details>
<summary><strong>Crawling, Rendering and Canonicals</strong> - 2 resources</summary>

- [Check rendering and canonicals before migrating an AI-built site](https://x.com/AllGasSeo/status/2108631484051656772) - A reminder to review search accessibility and canonical configuration before replacing an existing website. React alone does not establish an indexing problem; evaluate what crawlers actually receive.
- [Technical SEO checklist for an AI-built website](https://x.com/suraj_sharma14/status/2106240327569035424) - Covers crawl access, noindex, redirects, 404s, canonicals, sitemaps, internal links, images and layout stability. Use as an audit checklist; the post's ranking deadline and blanket schema recommendations are not verified requirements.

</details>

<details>
<summary><strong>Sitemaps and Indexing Reports</strong> - 1 resource</summary>

- [Submit child sitemaps for section-level diagnostics](https://x.com/brodieseo/status/2107457558248358111) - Group sitemaps by products, categories, articles or help content to isolate indexing issues in Search Console. Submitting child sitemaps is useful for reporting; Google also accepts a sitemap index on its own.

</details>

---

<details>
<summary><strong>Local Listings and Review Replies</strong> - 2 practical tips</summary>

1. **Audit business citations.** Keep a reference record of the business name, address, phone and website. Compare public directory and review listings with it, flag outdated or incorrect facts, and prioritize prominent relevant listings. Equivalent phone/address formatting alone is not necessarily an error.
2. **Review public replies before publishing.** AI can draft concise responses, but a person should check tone and facts. Avoid disclosing or confirming private customer or case details, and route sensitive complaints to the responsible person.

</details>

---

## Content and On-Page SEO

Improve original value, accurate search titles, useful answers and genuinely outdated information.

<details>
<summary><strong>Improve Existing Pages</strong> - 1 resource</summary>

- [Turn Search Console impressions into content improvements](https://x.com/asaio87/status/2107817393342779773) - Find questions a page already appears for, answer missing intent explicitly, and create a separate linked page when the topic deserves one.

</details>

<details>
<summary><strong>Publishing and Maintenance</strong> - 1 resource</summary>

- [A consistent content and quality-link routine](https://x.com/asaio87/status/2106102846957486356) - Keep publishing in your niche, improve existing pages and favor relevant links over large volumes of spam.

</details>

<details>
<summary><strong>Content Refreshes and Search Intent</strong> - 1 resource</summary>

- [Real content updates, satisfying answers and brand visibility](https://x.com/mehrab_build/status/2108572075485200422) - Refresh information substantively, keep dates honest, deliver the title’s promise early and track relevant branded searches in Search Console. **Partial thread text.** [Evidence and qualifications](docs/content-quality.md).

</details>

<details>
<summary><strong>Original Value and Search Titles</strong> - 1 resource</summary>

- [Original value and accurate search titles](https://x.com/mehrab_build/status/2106409427628867584) - Add evidence, examples or answers the leading results lack, and write titles that accurately describe the page and match the search intent. **Partial thread text.** [Evidence and qualifications](docs/content-quality.md).

</details>

<details>
<summary><strong>Video Research and Product Demonstrations</strong> - 1 destination</summary>

- [YouTube](https://www.youtube.com/) - Research tutorial questions and publish useful original product demonstrations.

</details>

[Checked guidance and ranking-claim qualifications](docs/content-quality.md) - Original value, titles, real updates, click evidence and brand measurement.

---

## Backlinks and Authority

Find relevant mentions and placements that serve an actual audience.

<details>
<summary><strong>Outreach and Existing Mentions</strong> - 1 resource</summary>

- [Find and reclaim unlinked brand mentions](https://x.com/seo_wins/status/2106648293715607936) - Search for existing mentions of your brand, identify missing links and ask the publisher to add the relevant URL. [Companion post](https://x.com/hridoyreh/status/2106647803799945615). Two near-identical bookmarks are grouped here; both original sources are preserved.

**Find resource pages for outreach:** Search Google with `"your topic" intitle:resources inurl:resources` (for example, `"seo" intitle:resources inurl:resources`). Review each result for topical fit and whether your resource adds something useful before contacting the publisher. These are prospects, not guaranteed backlink placements.

</details>

<details>
<summary><strong>Directories and Launch Listings</strong> - 2 resources</summary>

- [MCP and SaaS directory submission list](https://x.com/attenisalluneed/status/2106029974105043227) - The full list has 38 names across MCP directories, GitHub lists, SaaS launch sites, and agent/AI-search destinations. Full source names and positions are retained in the source catalogue and prospect archive. Relevant destinations appear once in the curated directory index; ambiguous names and poor-fit platforms are withheld from the main guide. DR and followed-backlink claims remain unverified.
- [Startup backlink prospect list](https://x.com/hridoyreh/status/2079831605863178416) - The full exported list contains 127 positions and 122 unique names across product directories, software reviews, communities, publishers and other platforms. Full source names and positions are retained in the source catalogue and prospect archive. Relevant destinations appear once in the curated directory index; ambiguous names and poor-fit platforms are withheld from the main guide. DR and followed-backlink claims remain unverified.

</details>

The directory bookmarks contribute destinations to the next section. [Source lists and original positions](docs/backlink-prospects.md) remain available for reconciliation.

---

## Backlink Opportunities and DR

**160 unique relevant destinations**, grouped by purpose. Each publisher or product appears once; its submission, homepage and related routes belong to that entry.

Use directories that fit the product, communities where you can contribute and publications where you have a credible story. DR, “free dofollow” and ranking gains are unverified source claims. Current listing terms and link attributes need checking before submission.

[Full source-list archive](docs/backlink-prospects.md) · [Unique destination index and evidence](data/destinations.json)

### MCP Directories

<details>
<summary><strong>10 destinations</strong></summary>

For compatible MCP servers. Directory discovery does not establish a followed backlink.

- [Official MCP Registry](https://registry.modelcontextprotocol.io/) - Official catalog for discovering Model Context Protocol servers.
- [AI Indigo](https://aiindigo.com/mcp-servers) - MCP server section of AI Indigo's broader AI tools directory.
- [AllMCPs](https://allmcps.com/) - Directory for discovering MCP servers and inspecting their connection metadata.
- [Glama](https://glama.ai/mcp/servers) - Searchable MCP server registry with server metadata and categories.
- [MCP Directory](https://mcp.directory/) - MCP server and skill directory.
- [MCP Market](https://mcpmarket.com/) - Catalog of MCP servers and agent skills.
- [MCP Repository](https://mcprepository.com/) - Searchable repository and category directory for MCP servers.
- [MCP Servers](https://mcpservers.org/) - Curated collection of Model Context Protocol servers.
- [MCP So](https://mcp.so/) - MCP server, client and AI tool directory.
- [TensorBlock MCP](https://www.tensorblock.co/mcp) - TensorBlock's community MCP index, backed by its awesome-mcp-servers repository.

</details>

### MCP and Plugin GitHub Lists

<details>
<summary><strong>4 destinations</strong></summary>

Contribute an eligible server or plugin using each repository’s contribution requirements. Independent repositories remain separate destinations.

- [awesome mcp lists](https://github.com/collabnix/awesome-mcp-lists) - Curated MCP server, client and toolkit list.
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - Propose a useful MCP server through the list's contribution process.
- [toolsdk mcp registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry) - ToolSDK's structured MCP server registry and gateway project.
- [xAI plugin marketplace](https://github.com/xai-org/plugin-marketplace) - Official xAI plugin catalog for Grok Build.

</details>

### Agent, API and llms.txt Discovery

<details>
<summary><strong>6 destinations</strong></summary>

Match the actual API, plugin, agent skill or documentation to the destination. llms.txt directories do not establish a Google AI eligibility requirement.

- [Claude Code plugin directory](https://claude.com/marketplace/plugins) - Anthropic's plugin marketplace with a Claude Code compatibility filter.
- [ClawHub](https://clawhub.ai/) - OpenClaw skill and plugin registry.
- [llms txt Hub](https://llmstxthub.com/) - Directory of AI-ready documentation and websites implementing llms.txt.
- [llms txt Site](https://llmstxt.site/) - Directory of llms.txt file locations and related file statistics.
- [Public APIs](https://github.com/public-apis/public-apis) - Community list of public APIs and a separate MCP server section.

- [Vercel Connect](https://vercel.com/connect/browse) - Directory for services agents can connect to. Use the dashboard's Submit a Service flow, describe the service, add OAuth or API-key connection methods, test OAuth methods where applicable, and submit for Vercel review. [Submit a service](https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fconnect%2Fsubmit-service).

</details>

### SaaS and Startup Launches

<details>
<summary><strong>43 destinations</strong></summary>

- [Acid Tools](https://acidtools.com/) - AI tools directory focused on automation, writing, design and productivity.
- [AI Directories](https://www.aidirectori.es/) - AI tool catalog and service for submissions to other directories.
- [AlternativeTo](https://alternativeto.net/) - Crowdsourced software recommendations and alternatives directory.
- [Aura Plus Plus](https://auraplusplus.com/) - Aura++ is a startup and product launch platform with project pages, community votes and scheduled launches.
- [BetaList](https://betalist.com/) - Early-stage startup discovery platform with a Submit startup route.
- [Better Launch](https://www.betterlaunch.co/) - Product discovery and launch platform for founders.
- [ConfettiSaaS](https://confettisaas.com/) - Directory for SaaS startups and founders.
- [DanielLaunches](https://daniellaunches.com/) - Platform for discovering and launching useful products.
- [EarlyHunt](https://earlyhunt.com/) - Weekly project-launch platform for new AI products and startups.
- [Fazier](https://fazier.com/) - Product discovery and launch platform with a dedicated submission page.
- [FeedMyStartup](https://feedmystartup.com/) - Startup and app discovery directory with submission links.
- [Findly](https://findly.tools/) - Curated SaaS and tools directory for makers.
- [Firsto](https://firsto.co/) - Product-launch platform for makers, indie hackers and startup founders.
- [FoundrList](https://www.foundrlist.com/) - Founder network combining product launches, maker discovery and community features.
- [IndieHunt](https://indiehunt.io/) - Weekly launch platform for AI products and indie makers.
- [IndieTool](https://www.indietool.io/) - Directory and launchpad for products built by indie founders.
- [Launch Llama](https://tools.launchllama.co/) - Curated startup and tool launch directory.
- [Launch Streak](https://launchstreak.dev/) - Maker product launches and recurring builder activity.
- [LaunchIgniter](https://launchigniter.com/) - Product launch platform for creators to showcase products and gather early-adopter feedback.
- [LaunchPanda](https://www.launchpanda.dev/) - Product launch community and directory submission workflow.
- [Microlaunch](https://microlaunch.net/) - Startup launch and discovery platform with monthly product launches.
- [Noonlaunch](https://noonlaunch.com/) - Product launch boards and startup directory.
- [PeerPush](https://peerpush.com/) - Product discovery platform for indie makers, startups, and technology products.
- [PitchWall](https://pitchwall.co/) - Discovery platform for AI tools, SaaS products, and technology startups.
- [Product Hunt](https://www.producthunt.com/) - Technology product discovery and launch community.
- [RankCert](https://rankcert.com/) - Product launch board with public product listings and domain verification. Basic listing is advertised as free; optional upgrades are paid. Check current badge and link terms.
- [ScrollLaunch](https://www.scrolllaunch.com/) - Weekly product launches and startup directory.
- [SideProjectors](https://www.sideprojectors.com/) - Marketplace for showcasing, buying and selling side projects and finding co-founders.
- [Startup Buffer](https://startupbuffer.com/) - Public startup directory organized by market, location, tags and related products.
- [Startup Fame](https://startupfa.me/) - Startup discovery directory with reviewed startup profiles.
- [StartupBase](https://startupbase.io/) - Product launch and discovery platform with product pages and launch rankings.
- [Startups FYI](https://www.startups.fyi/) - Curated startup and side-project discovery site paired with a founder newsletter.
- [Stork](https://www.stork.ai/browse) - Stork's directory of AI tools, agents and MCP-related products.
- [Tiny Startup](https://www.tinystartups.com/) - Curated startup launch and discovery directory for small products and side projects.
- [TinyLaunch](https://www.tinylaunch.com/) - Product launch platform with launch rankings, winner badges and product discovery.
- [Tinyshelf](https://www.tinyshelf.co/) - Curated software directory with categories and tags.
- [ToolFame](https://toolfame.com/) - Broad AI, SaaS and online tools directory with a submission link.
- [Toolfolio](https://toolfolio.com/) - Tool discovery directory spanning AI, design, coding and business resources.
- [TrustMRR](https://trustmrr.com/) - Verified startup revenue database and marketplace for SaaS and digital business acquisitions.
- [Turbo0](https://turbo0.com/) - Directory of tools and products, with an emphasis on content creation.
- [Twelve Tools](https://twelve.tools/) - Daily curated directory of tools and startups.
- [Uneed](https://www.uneed.best/) - Product launch and discovery platform with launch scheduling and product pages.
- [WhatLaunched](https://whatlaunched.today/) - Startup launch and discovery directory. **Limited access:** current submission terms are unconfirmed.

</details>

### AI Product Directories

<details>
<summary><strong>20 destinations</strong></summary>

- [AI Agent Store](https://aiagentstore.ai/) - AI-agent marketplace and discovery directory for agents, tools, frameworks and related products.
- [AI Parabellum](https://aiparabellum.com/) - Curated AI-tool directory with a product submission and dedicated tool-review page model.
- [AI Tool Trek](https://aitooltrek.com/) - AI-tool discovery directory with a dedicated tool-submission workflow.
- [AIxploria](https://www.aixploria.com/en/) - AI-tool directory with categorized discovery, rankings and related editorial resources.
- [Altern](https://altern.ai/) - Discovery platform for AI tools, models, agents and other AI ecosystem products.
- [Appscribed](https://appscribed.com/) - AI-tool directory combining product listings with hand-written editorial reviews.
- [BotsFloor](https://botsfloor.com/) - The botsfloor.com destination currently presents BotStash, an AI-tool discovery directory.
- [Dang](https://dang.ai/) - AI tools discovery directory with tool-submission navigation.
- [Futurepedia](https://www.futurepedia.io/) - AI-tool and software discovery platform with categorized product information.
- [MagicBox.tools](https://magicbox.tools/) - AI tools directory with search, categories and Submit navigation.
- [Open Tools](https://opentools.ai/) - AI tool directory with product discovery, comparisons, and tool or MCP launch options.
- [Powerusers](https://powerusers.ai/) - AI tool directory and resource site with a Submit AI Tool route.
- [RankYourAI](https://rankyourai.com/) - AI tool directory with a product submission page.
- [SEOFAI](https://seofai.com/) - AI tools directory organized by use cases and job roles.
- [ShowMeBestAI](https://showmebest.ai/) - AI tools discovery directory with an explicit AI tool submission link.
- [That AI Collection](https://thataicollection.com/) - AI applications directory with categorized listings, comparisons and a listing route.
- [There's an AI for That](https://theresanaiforthat.com/) - AI application discovery platform organized around finding tools for tasks. **Limited access:** current submission terms are unconfirmed.
- [Toolify AI](https://www.toolify.ai/) - AI tools discovery directory with tool submission and promotional options.
- [ToolPilot](https://www.toolpilot.ai/) - AI tools catalogue with Submit Your AI Tool navigation.
- [Wavel](https://www.wavel.io/) - AI tools and agents discovery marketplace with an AI tool submission route.

</details>

### Software Reviews and Deals

<details>
<summary><strong>24 destinations</strong></summary>

- [Affiliate Watch](https://affiliate.watch/) - Affiliate-program discovery directory with program reviews and comparison information. **Limited access:** current submission terms are unconfirmed.
- [Alternative Me](https://alternative.me/) - Software and product alternative-comparison platform with reviews and recommendations.
- [AppSumo](https://appsumo.com/) - Software-deal marketplace with partner requirements; its blog is a related editorial route, not a second independent listing site.
- [CompareCamp](https://comparecamp.com/) - Software review and comparison publication.
- [Dan Recommends](https://www.danrecommends.com/) - Human-written SaaS product-review service with published review pages.
- [Dealify](https://dealify.com/) - Software lifetime-deal marketplace with a Sell on Dealify route.
- [DealMirror](https://dealmirror.com/) - Marketplace for discounted software and lifetime product deals.
- [FounderPass](https://www.founderpass.com/) - Startup-perks and discount platform offering negotiated product deals to founders.
- [GoodFirms](https://www.goodfirms.co/) - B2B software and service-provider profiles, reviews, and category discovery.
- [KEN Moo](https://kenmoo.me/) - SaaS lifetime-deal discovery, discussion, and software coverage.
- [Product Canyon](https://productcanyon.com/) - Software marketplace featuring lifetime and subscription deals.
- [Ramen.tools](https://ramen.tools/) - Maker tool-stack sharing and discovery community.
- [RocketHub](https://www.rockethub.com/) - Curated lifetime software deals and startup-perk marketplace.
- [SaaS Genius](https://www.saasgenius.com/get-listed/) - Business software discovery and review catalogue with a vendor listing route.
- [SaaS Pirate](https://saaspirate.com/submit-a-deal/) - Curated SaaS and software discounts and lifetime deals.
- [SaaSHub](https://www.saashub.com/services/submit) - Software alternatives and reviews directory with a product submission form.
- [SaaSZilla](https://saaszilla.co/) - Curated software deal platform that selects products and teams for listings.
- [Serchen](https://www.serchen.com/get-listed) - Business software marketplace with company profiles and a listing route.
- [Software Suggest](https://www.softwaresuggest.com/vendors) - Business software and service recommendations platform with a vendor listing route. Provider advertises a free basic listing and requires a business email; paid promotion is separate.
- [Software World](https://www.softwareworld.co/register/) - Business software and services review directory with a vendor-account listing route. Provider currently lists a $99 one-time approval fee for new listings; claiming an existing profile is free.
- [StackSocial](https://www.stacksocial.com/) - Commerce platform for software subscriptions, tech products and promotional deals. **Limited access:** current submission terms are unconfirmed.
- [Startup Stash](https://startupstash.com/) - Curated directory of tools and resources for startups.
- [Tekpon](https://tekpon.com/software/) - Software discovery, reviews, pricing and comparison catalogue.
- [TrustRadius](https://www.trustradius.com/) - B2B software review and comparison platform offering claimed vendor product profiles.

</details>

### Developer and Open-Source Products

<details>
<summary><strong>12 destinations</strong></summary>

- [API List](https://apilist.fun/) - Categorized API directory for developers, with an Add API route.
- [Chrome Web Store](https://chromewebstore.google.com/) - Distribution store for actual Chrome extensions, with developer publishing and review workflows.
- [code.market](https://code.market/) - Curated digital-product catalogue covering software, templates and developer resources.
- [DevHunt](https://devhunt.org/) - Launch and discovery platform focused on developer tools.
- [Gumroad](https://gumroad.com/) - Creator storefront and marketplace for selling products and sharing a creator business.
- [LibHunt](https://www.libhunt.com/) - Discovery of open-source projects, software libraries, and alternatives using developer-community mentions. **Limited access:** current submission terms are unconfirmed.
- [OpenAlternative](https://openalternative.co/) - Directory of open-source alternatives to proprietary software.
- [OSS Gallery](https://oss.gallery/) - Crowdsourced gallery of open-source projects.
- [Peerlist](https://peerlist.io/) - Professional builder network with portfolios and a Launchpad for projects.
- [Privacy Tools](https://privacytools.io/) - Privacy-focused software and service recommendations, alternatives, and app discovery.
- [SourceForge](https://sourceforge.net/) - Open-source project hosting and distribution platform with a separate B2B software catalogue.
- [StackShare](https://stackshare.io/) - Developer tool discovery and technology-stack sharing platform. **Limited access:** current submission terms are unconfirmed.

</details>

### Editorial, Podcasts and Founder Stories

<details>
<summary><strong>17 destinations</strong></summary>

Pitch a relevant story or interview. Editorial coverage is different from a self-serve listing.

- [Bootstrappers](https://bootstrappers.com/) - Publication featuring bootstrapped-founder interviews and practical startup stories.
- [Boring Cash Cow](https://boringcashcow.com/) - Curated profiles, showcases and interviews about simple profitable online businesses.
- [Failory](https://www.failory.com/) - Founder-focused publication and newsletter covering startup failures, successes and lessons.
- [First Round Review](https://review.firstround.com/) - In-depth startup publication featuring founder and operator expertise, company stories and practical advice.
- [Forbes](https://www.forbes.com/) - Business media publication; potential fit is a newsworthy story or relevant expert contribution.
- [Founder Reports](https://founderreports.com/) - Business publication with in-depth founder and CEO interviews, original research and editorial content.
- [Latka](https://getlatka.com/add) - SaaS company database and founder interviews, with reviewed company-profile submissions.
- [Micro Founder](https://microfounder.com/) - Curated solo-founder startup examples, revenue profiles, and founder Q&A.
- [Mixergy](https://mixergy.com/) - Entrepreneur interviews, business podcast episodes, and startup courses.
- [My First Million](https://www.mfmpod.com/) - Business-ideas podcast hosted by Shaan Puri and Sam Parr.
- [Niche Pursuits](https://www.nichepursuits.com/) - Online-business publication with SEO articles, founder success stories, and podcast interviews.
- [SaaS Club / The SaaS Podcast](https://saasclub.io/) - Founder interview publisher, newsletter and SaaS community.
- [Sidebar](https://sidebar.io/) - Curated design-link publication and newsletter.
- [Starter Story](https://www.starterstory.com/share) - Entrepreneur interview and business case-study publisher.
- [TechCrunch](https://techcrunch.com/contact-us/) - Technology news outlet for newsworthy startup and product story pitches.
- [VentureBeat](https://venturebeat.com/contact-2) - Enterprise AI news publisher for relevant editorial pitches.
- [YourStory](https://yourstory.com/companies) - List an eligible company in YourStory’s company directory; editorial startup coverage is a separate route with the same publisher. Company listing and editorial coverage have separate requirements.

</details>

### Communities and Publishing

<details>
<summary><strong>14 destinations</strong></summary>

Publish original useful material or participate meaningfully; follow each community’s rules.

- [Beehiiv](https://www.beehiiv.com/) - Newsletter and website publishing platform for a brand's own content and audience.
- [DevTo](https://dev.to/) - DEV Community is a publishing and discussion community for software developers.
- [Hacker News / Show HN](https://news.ycombinator.com/showhn.html) - Share a working project through Show HN or contribute relevant technical discussions; follow community rules.
- [HackerNoon](https://hackernoon.com/) - Technology publication and contributor platform for useful articles and project stories.
- [Hashnode](https://hashnode.com/) - Blogging platform for developers and engineers to publish technical work.
- [Indie Hackers](https://www.indiehackers.com/) - Founder community with product discovery, startup discussions, and business case studies.
- [Medium](https://medium.com/) - General publishing platform for author profiles, articles, and ideas.
- [PromptZone](https://www.promptzone.com/) - AI community for prompts, guides, discussion, and builder projects.
- [Quora](https://www.quora.com/) - Question-and-answer platform for sharing useful knowledge and expertise.
- [Reddit](https://www.reddit.com/) - Topic-based discussion communities where relevant projects and knowledge can be shared.
- [Stacker News](https://stacker.news/) - Community discussion and link-posting platform with Bitcoin-oriented participation economics.
- [Substack](https://substack.com/) - Publishing platform for newsletters, articles, podcasts, video and creator communities.
- [Vocal Media](https://vocal.media/) - Creator publishing platform and communities for original articles and stories.
- [WIP](https://wip.co/join) - Maker accountability community for building in public and sharing project progress.

</details>

### Business and Web Directories

<details>
<summary><strong>3 destinations</strong></summary>

- [Brownbook](https://www.brownbook.net/) - Business directory offering company profiles, listing and claiming.
- [LinkCentre](https://www.linkcentre.com/) - Web directory with website submission and country/category browsing.
- [Viesearch](https://viesearch.com/) - Categorized web directory and human-curated discovery index.

</details>

### Publishing, Media and Brand Profiles

<details>
<summary><strong>6 destinations</strong></summary>

Use original tutorials, visual assets or public documentation. Hosting and profile pages are different from independent editorial backlinks.

- [Flickr](https://www.flickr.com/) - Photography community and image-sharing platform for real photo collections and creator profiles.
- [GitHub](https://github.com/) - Code-hosting and collaboration platform for real projects, public repositories and documentation.
- [GitHub Pages](https://pages.github.com/) - Website and project-documentation hosting directly from GitHub repositories.
- [Indie Page](https://indiepa.ge/) - Founder profile pages that showcase startup portfolios and entrepreneurial journeys.
- [Pinterest](https://www.pinterest.com/) - Visual discovery platform where Pins can connect useful images and ideas to websites.
- [Vimeo](https://vimeo.com/) - Video hosting, sharing and discovery platform for original product videos and tutorials. Check public visibility and plan requirements for the video.

</details>

### Search Submissions

<details>
<summary><strong>1 destination</strong></summary>

Submission to an independent search engine does not request Google indexing.

- [Active Search Results](https://www.activesearchresults.com/) - Independent search engine with an Add a Website route.

</details>

Already covered in other sections: [G2 review research](#keyword-research), [YouTube tutorials](#content-and-on-page-seo) and [Ubersuggest / Neil Patel integrations](#seo-websites-tools-skills-and-github-repos). Their supplied source references are attached to those existing destinations.

Ambiguous names and platforms without a useful SEO or submission role are retained in the [source archive](docs/backlink-prospects.md), with [review decisions](docs/source-review.md#destination-curation).

---

## AI Search and GEO

Build useful evidence, inspect crawler requirements and measure answer visibility.

<details>
<summary><strong>Content That Can Be Cited</strong> - 2 resources</summary>

- [Build useful evidence before chasing AI citations](https://x.com/seo_bint_ejamil/status/2108906394959204628) - Focus on specific questions, extractable answers, original research, accurate third-party context and repeatable measurement.
- [Good SEO as the foundation for GEO](https://x.com/alexgroberman/status/2107859240375509250) - The post discusses crawlability, useful original content, query fan-out, business information and customer decision questions. The author's attribution to a particular Google article was not verified; Google's official AI-features guidance is linked below.

</details>

<details>
<summary><strong>SaaS Visibility and Measurement</strong> - 3 resources</summary>

- [AI-search workflow for SaaS content and referral tracking](https://x.com/denohawari/status/2108636363868586010) - Review search-crawler access, indexing, buyer-question headings, integration pages, definitions and AI referral traffic. The revenue claim and cross-platform eligibility guarantees are unverified; check each crawler's current documentation.
- [A 30-day ChatGPT citation and buyer-question audit](https://x.com/TheCoolestCool/status/2105787365126226359) - Repeat a fixed set of buyer questions with web search, log cited URLs separately from brand recommendations, map recurring sources, and compare referral visits with leads. Publish evidence with methods and limitations. The schedule is an example; study correlations and numerical claims are not verified ranking rules or citation guarantees.
- [Review-led SEO, GEO and AEO workflow](https://x.com/om_patel5/status/2099683744781111419) - Mine customer complaints and People Also Ask, build linked topic clusters, reuse useful videos and inspect search queries and AI recommendations. The post's llms.txt, bot-eligibility and automatic-citation claims need verification; Google does not require special AI files.

**Track a single AI Overview query over time.** Repeat the same query on several dates and record whether an overview appears, its linked sources, the claims each supports, location/device and available search-context settings. Use gaps to plan useful evidence or answers. Changing citations are observations, not proof of what causes selection.

</details>

<details>
<summary><strong>Terminology</strong> - 1 resource</summary>

- [SEO, AEO, GEO and SXO terminology](https://x.com/james_dooley/status/2100907455890800881) - A short positioning framework connecting search discovery, answers, citations and conversion. A terminology reference rather than a documented ranking model.

- **SMO — Social Media Optimisation:** discovery, distribution and discussion across relevant social platforms.
- **DEO — Decision Engine Optimisation:** the supplied author's emerging framework for making suitability, pricing, availability, limitations and policies clear for comparison. This is a nonstandard label, not a demonstrated ranking system.

</details>

<details>
<summary><strong>AI Visibility Reporting</strong> - 1 reference</summary>

- [Bing AI Performance documentation](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/) - Citation and grounding-query reporting across supported AI experiences.

</details>

> [Google’s AI-features guidance](https://developers.google.com/search/docs/appearance/ai-features) says the usual SEO foundations apply to AI Overviews and AI Mode. Special AI files or schema are not required.

---

## SaaS and App SEO

Connect customer problems and commercial searches to useful product and comparison pages.

<details>
<summary><strong>Product-Led Search Assets</strong> - 2 resources</summary>

- [Build distribution into the product](https://x.com/hridoyreh/status/2108742814507159609) - Free tools, calculators, templates, public reports and integrations can give people a reason to discover and reference a product.
- [Search-focused channels from a SaaS marketing checklist](https://x.com/jessievbreugel/status/2108543866563432845) - The SEO-related ideas include competitor-alternative pages, free tools, AI search and integration marketplace listings.

**Validate calculators before launch.** Record authoritative formula sources and their dates. Test known examples, units, rounding, boundary values and invalid inputs, and check that the explanations match the outputs. Health-related calculations need qualified review; search traffic does not validate a formula.

</details>

<details>
<summary><strong>Comparison and Use-Case Pages</strong> - 2 resources</summary>

- [Competitor-alternative landing pages](https://x.com/hridoyreh/status/2108447368131531109) - Choose relevant competitors and create comparison pages for buyers evaluating alternatives. The source proposes listing your own product first; make comparisons accurate and useful to the buyer.
- [Website SEO playbook for mobile app founders](https://x.com/om_patel5/status/2099003320446616013) - Use competitor complaints to plan problem, alternative, roundup and use-case pages; add useful download CTAs and review Search Console queries.

</details>

<details>
<summary><strong>End-to-End Playbooks</strong> - 1 resource</summary>

- [Commercial-keyword SEO workflow for SaaS founders](https://x.com/mehrab_build/status/2107812981786710479) - Collect competitor keywords with SEO data tools, match the ranking page format, add original product evidence, link new pages and monitor weekly.

</details>

<details>
<summary><strong>Programmatic SEO for Product Use Cases</strong> - 1 workflow</summary>

1. **Map real use cases to demand.** Start with features or use cases the product actually supports and match them to commercial queries. Group overlapping searches by intent; each keyword variant does not need its own URL.
2. **Make each page useful and distinct.** Use a consistent template with a relevant product demo or example, an accurate capability explanation and a clear next action. Swapping a name into the same copy is not sufficient.
3. **Connect pages to helpful guides.** Answer genuine pre-purchase questions and link contextually between guides, related use cases and product pages.
4. **Measure and improve.** Review search-query coverage and user outcomes. Prioritize useful pages over a target page count or daily publishing quota.

Adapted from a supplied SaaS case study. Its revenue, signup, traffic and AI-recommendation outcomes are unverified. [Evidence and source review](docs/content-quality.md#programmatic-seo-case-study).

**Prioritize landing-page outcomes.** Compare search performance by landing page with signups, demos or other meaningful outcomes using comparable date ranges and a stated attribution model. Investigate pages with visits but few outcomes. Keep Search Console clicks distinct from analytics sessions, and account for small samples and delayed conversions.

**Review translated pages.** Check local terminology, units, examples, formulas and disclosures in each language. Link equivalent language versions and check language targeting. Expand where the localized page serves real demand; language and page counts are not success targets.

</details>

For launches and placements, use the [unique destination groups](#backlink-opportunities-and-dr). For customer language, use the [review-research sources](#keyword-research).

---

## Automation and Skills

Use the [websites, tools, repositories and reusable skills index](#seo-websites-tools-skills-and-github-repos) for implementations, or the [SEO MCP servers](#seo-mcp-servers) for connected data.

<details>
<summary><strong>AI-Assisted SEO Workflow</strong> - 1 article</summary>

- [How to use Claude Opus 5.5 for SEO so well it feels illegal](https://x.com/NicholasDulait/status/2108212094214529135) - Research commercial intent with real data, check existing URLs before creating pages, and compare AI edits against the original so tables, forms and useful examples survive. Also covers briefs, sitemap maintenance, local SEO and editorial outreach. Supplied text ends at Module 15; its promised GEO section is missing. Product promotion, fixed quotas and ranking claims are not verified requirements.

</details>

Skill announcements and tools whose actual repository or implementation could not be reviewed remain in the [source register](docs/source-review.md#resource-curation).

---

## Review Coverage

The original 100-row export contains 48 confirmed SEO sources, 26 outside SEO and 26 link-only sources with unknown relevance. Live X retrieval remains unavailable; supplied thread text is recorded separately from live media inspection.

User text recovered two backlink fragments, two Mehrab signal fragments and the grouped Google Sites workflow. The backlink fragments still lack v4 positions 1–4 and v3 position 10. The Mehrab threads are not claimed complete. The complete supplied Musicfy article was read from a local Markdown copy; its practical programmatic SEO advice is now included, without a standalone article link. The supplied Nicholas Dulait excerpt through Module 15 was also read and added as one annotated article link; its promised GEO sections were not supplied.

- [Source register, relevance decisions and pending content](docs/source-review.md)
- [Full directory source archive and original positions](docs/backlink-prospects.md)
- [Unique destination index](data/destinations.json)
- [Structured resources and curation policy](data/resources.json)
- [Awesome SEO collection review and additions](docs/awesome-seo-review.md)
- [Ranking claims and primary references](docs/content-quality.md)

### Official References

- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Helpful, reliable content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Title links](https://developers.google.com/search/docs/appearance/title-link)
- [Publication and update dates](https://developers.google.com/search/docs/appearance/publication-dates)
- [Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google Search spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Evaluating third-party SEO advice](https://developers.google.com/search/docs/fundamentals/third-party-seo)

For future pastes: add only new, useful SEO material; enrich an existing entry when the post adds useful information; use links and short takeaways for articles. Keep missing content and unsupported guarantees out of the curated recommendations.
