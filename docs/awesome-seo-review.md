# Awesome SEO collection review

Reviewed on 11 October 2026.

Read both [teles/awesome-seo](https://github.com/teles/awesome-seo) and [bmpi-dev/awesome-seo](https://github.com/bmpi-dev/awesome-seo). Compared their README resources with the current index and submission destinations. Selected **24 new destinations**, including the two collections themselves. Selected tool capabilities were checked against primary sites or upstream documentation; no software was installed or runtime-tested.

## Added destinations

| Resource | Group | Notes |
| --- | --- | --- |
| [Keyword Tool](https://keywordtool.io/) | Keyword Research and Competitors | Find autocomplete-based keyword ideas across search platforms; advanced metrics depend on the plan. |
| [SpyFu](https://www.spyfu.com/) | Keyword Research and Competitors | Research competitor organic keywords, ranking history and backlink opportunities; vendor estimates are not first-party analytics. |
| [Majestic](https://majestic.com/) | Keyword Research and Competitors | Inspect backlinks, referring domains and link context; its proprietary scores are not Google ranking scores. |
| [Similarweb](https://www.similarweb.com/) | Keyword Research and Competitors | Explore competitor traffic and channel research; use external measurements for context alongside your own analytics. |
| [Seobility](https://www.seobility.net/en/) | Technical Audits and Automation | Website audits, rank monitoring and backlink analysis; review current plan limits. |
| [Screpy](https://screpy.com/) | Technical Audits and Automation | Website audits, rank tracking, performance monitoring and SEO reporting. |
| [Raven Tools](https://raventools.com/) | Technical Audits and Automation | Site auditing, rank tracking, backlink research and reporting. |
| [PageSpeed Insights](https://pagespeed.web.dev/) | Performance and Accessibility | Inspect page performance and available real-user data; a test score is not a ranking guarantee. |
| [GTmetrix](https://gtmetrix.com/) | Performance and Accessibility | Analyze page loads, request waterfalls and performance changes; account and plan limits apply. |
| [WAVE](https://wave.webaim.org/) | Performance and Accessibility | Find accessibility issues and support manual evaluation; automated checks cannot establish complete compliance. |
| [Keyword Surfer](https://surferseo.com/keyword-surfer-extension/) | Browser Extensions | View keyword ideas and volume estimates in search results, with keyword collections and CSV export. |
| [META SEO inspector](https://www.omiod.com/meta-seo-inspector/) | Browser Extensions | Inspect page metadata and identify missing or inconsistent on-page information. |
| [Google Rich Results Test](https://search.google.com/test/rich-results) | Structured Data and Metadata | Test URLs or code for supported Google rich-result markup; a valid test does not guarantee display. |
| [advertools](https://github.com/eliasdabbas/advertools) | GitHub Repositories and Self-Hosted SEO | Python library for crawling, sitemap and robots.txt analysis, URL processing and server-log analysis. Some integrations require separate provider access. |
| [GEO/AEO Tracker](https://github.com/danishashko/geo-aeo-tracker) | GitHub Repositories and Self-Hosted SEO | Self-hosted dashboard for prompts, brand mentions and citations. Live tracking uses Bright Data; analysis may use OpenRouter and other paid APIs. Demo mode uses sample data, and its heuristic scores are not ranking factors. |
| [mesure-citations](https://github.com/thomasmerlaud/mesure-citations) | GitHub Repositories and Self-Hosted SEO | French-language Node CLI to maintain a fixed prompt corpus, record manual observations and compare mentions with linked citations. Does not query AI services automatically; no API key required. |
| [ai-crawler-bots](https://github.com/TryGeoSuite/ai-crawler-bots) | GitHub Repositories and Self-Hosted SEO | Node CLI and GitHub Action for robots.txt checks, live reachability and log analysis. Treat its visibility score as a heuristic; check current operator documentation rather than adopting its default bot policies blindly. |
| [NotFair Plugin](https://github.com/nowork-studio/notfair-plugin) | Reusable SEO Skills | SEO and analytics workflows for audits, keyword research, sitemaps, local SEO and content. Former NotFair and toprank links resolve to this one repo. Live account workflows need its OAuth-connected MCP and authorized provider access; documentation reviewed, not installed. |
| [Schema.org vocabulary](https://schema.org/docs/schemas.html) | SEO Reference Websites and Validators | Look up structured-data types and properties; Schema.org vocabulary is broader than Google's supported rich-result types. |
| [Open Graph protocol](https://ogp.me/) | SEO Reference Websites and Validators | Reference for social-preview metadata; distinct from Google structured-data eligibility. |
| [Google Search Central Blog](https://developers.google.com/search/blog) | SEO Learning and Updates | Official search announcements and documentation updates. |
| [Ahrefs Blog](https://ahrefs.com/blog/) | SEO Learning and Updates | Research and practical SEO tutorials from the tool provider; distinguish studies, opinions and current search-engine requirements. |
| [teles/awesome-seo](https://github.com/teles/awesome-seo) | More SEO Resource Collections | Broad discovery list of SEO tools and references; individual listings and claims need their own checks. |
| [bmpi-dev/awesome-seo](https://github.com/bmpi-dev/awesome-seo) | More SEO Resource Collections | SEO learning and tool collection with English and Chinese resources; includes older material and non-SEO monetization topics. |

## Existing entries and identity updates

Ahrefs, Semrush, Screaming Frog and Ubersuggest were already present and were not duplicated. Old HTTP links from the collections were replaced with the selected current HTTPS destinations. PageSpeed uses pagespeed.web.dev.

The NotFair and toprank project links both redirected to nowork-studio/notfair-plugin when opened. They are included as one skill collection, with its current setup and access requirements. Its sitemap-audit workflow was inspected as an example; the whole plugin has not been runtime-tested.

## Deferred and excluded material

- Moz and WebPageTest: primary destinations could not be read reliably in this review. They remain candidates, not new verified recommendations.
- SEOquake: the supplied provider URL redirected to a different SEO-checker page. The legacy extension listing was not imported.
- Year-specific older guides and the old Mobile-Friendly Test link: omitted in favor of current documentation and performance testing.
- General social scheduling, paid advertising, traffic monetization, affiliate courses and compliance-only scanners: outside the SEO hub's current purpose or insufficiently useful to add here.
- Remaining overlapping audit products, schema generators and GEO tools: not bulk imported. Unselected products were not all checked individually; inclusion in an awesome list alone is not evidence of capability or quality.
- Promises about automatic indexing, FAQ click gains, photo geotagging, special AI files or guaranteed citability were not adopted.

## Technical qualifications

GEO/AEO Tracker needs external services for live results; running its sample dashboard does not measure a real brand. Citation tools measure a chosen prompt/model/context configuration, not a universal visibility score.

Crawler-audit scores are tool heuristics. Training permissions and search discovery are separate choices; check each provider's current crawler documentation before changing robots.txt.

Schema.org validation and Google's Rich Results Test serve different purposes. Valid markup does not guarantee a rich result. Added the Schema.org vocabulary reference alongside the existing validator.

For larger-site crawl questions, use [Google's current crawl-budget guidance](https://developers.google.com/crawling/docs/crawl-budget). For JavaScript rendering, [Google's dynamic-rendering guidance](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering) discusses alternatives; a vendor workaround is not a universal requirement.
