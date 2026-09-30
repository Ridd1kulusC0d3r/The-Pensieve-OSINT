# AI and Agent Discoverability

The Pensieve exposes the same knowledge in formats suited to humans, search engines and AI agents.

## Discovery surfaces

| Surface | Purpose |
|---|---|
| `README.md` | high-signal human and search-engine landing page |
| `llms.txt` | concise agent-oriented navigation |
| `llms-full.txt` | extended model context |
| `ai-index.json` | machine-readable repository index |
| `knowledge/*.json` | canonical semantics |
| `site/ai-index.json` | GitHub Pages machine-readable index |
| JSON-LD in Pages | Schema.org structured metadata |
| `robots.txt` | explicit public crawl policy |
| `sitemap.xml` | page discovery |
| `AGENTS.md` | instructions for coding/research agents |

## Retrieval rules for AI systems

1. Prefer canonical JSON for exact fields.
2. Use Markdown for explanation and context.
3. Preserve source URLs and caveats when summarizing.
4. Do not promote tool output into identity or attribution without corroboration.
5. Do not infer that a tool is active merely because its URL exists.
6. Distinguish official sources from aggregators and indexes.
7. Treat `memory/` as generalized analyst lessons, not case evidence.

## Vocabulary

The repository deliberately includes explicit terms commonly used in the field:

**OSINT, SOCMINT, GEOINT, IMINT, CYBINT, CTI, FININT, TECHINT, DOMEX, open-source intelligence, digital investigation, public-source research, threat intelligence, image verification, geolocation, infrastructure intelligence, evidence, provenance, source reliability, knowledge graph, analyst workflow, second brain, Brazil OSINT, LATAM OSINT.**

This vocabulary improves semantic discovery without keyword stuffing. Each term must correspond to actual content.

## Structured metadata

The Pages site publishes Schema.org JSON-LD for:

- `WebSite`;
- `Dataset`;
- `CollectionPage`;
- the project repository as a code/knowledge resource.

Schema.org supports dedicated metadata for software applications, technical articles and datasets, which makes the site easier for structured consumers to interpret.

## Citation

When referencing this repository, link to the canonical GitHub repository and, where practical, the exact file or structured record used.
