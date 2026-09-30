# Agent Instructions

This repository is intentionally structured for AI/coding/research agents.

## Read order

1. `llms.txt`
2. `ai-index.json`
3. `knowledge/README.md`
4. the relevant `knowledge/*.json` file
5. explanatory Markdown under `docs/`
6. sanitized lessons under `memory/`

## Data authority

- `knowledge/*.json` is canonical structured knowledge.
- `data/tools.csv` is a generated/export format.
- `site/data/*` is generated for GitHub Pages.
- Markdown explains semantics but should not override explicit structured fields without a documented migration.

## Analytical constraints

Do not silently convert:
- a candidate account into a verified identity;
- shared infrastructure into ownership;
- a visual match into identity;
- a public record into a timeless/current fact;
- a reputation label into threat-actor attribution;
- no search result into evidence of absence.

Preserve caveats and source URLs in generated summaries.

## Editing

When adding a tool:
1. update `knowledge/tools.json`;
2. ensure its ID is unique;
3. validate inputs/outputs;
4. add caveats;
5. run `python scripts/validate_knowledge.py`;
6. run `python scripts/build_catalog.py`;
7. update documentation only if the new record changes navigation or methodology.

Never commit secrets, private case data or unnecessary personal information.
