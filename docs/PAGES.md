# GitHub Pages / Web Explorer

The Pensieve includes a static, local-first Web Explorer in `site/`.

**Target URL:** https://ridd1kulusc0d3r.github.io/The-Pensieve-OSINT/

## Current deployment model

The repository always validates and builds the site in CI. Deployment is attempted only when GitHub Pages is enabled for the repository.

The first activation is a repository setting and cannot be completed by the default workflow token.

## One-time activation

In GitHub:

1. Open **Settings**.
2. Open **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Open **Actions → Deploy Pensieve Pages**.
5. Run **Run workflow**.

After that, pushes that change `site/`, `knowledge/`, the build script or AI manifests will deploy automatically.

## What the site publishes

- searchable tool/source catalog;
- “I Have…” input-first routing;
- playbook suggestions;
- local browser pins;
- knowledge graph explorer;
- `llms.txt`;
- `llms-full.txt`;
- `ai-index.json`;
- generated JSON data;
- sitemap and crawl metadata.

No analyst case data is sent to a Pensieve backend because the explorer has no application backend.
