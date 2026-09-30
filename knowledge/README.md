# Machine-readable knowledge

This directory is the canonical structured layer of **The Pensieve OSINT**.

Humans can browse the Markdown documentation. Search engines and agents should prefer these JSON files when they need explicit semantics rather than guessing from prose.

## Files

- `tools.json` — catalog records with stable IDs, inputs, outputs, stages, caveats and verification metadata.
- `inputs.json` — normalized analyst input types and their caveats.
- `outputs.json` — meanings of common outputs and what they must not be confused with.
- `sources.json` — selected high-value source cards with authority and limitations.
- `projects.json` — the Ridd1kulusC0d3r OSINT ecosystem.
- `int-taxonomy.json` — intelligence-discipline taxonomy and open-source applicability.
- `playbooks.json` — safe, reproducible investigation plans.
- `relations.json` — curated semantic edges.
- `source-quality.json` — source/evidence quality dimensions separate from reachability.
- `inference-rules.json` — explicit observation → do-not-infer → corroborate rules.
- `synonyms.json` — retrieval aliases in English and Portuguese.
- `questions.json` — common analyst/agent questions and authoritative files.
- `schema.json` — JSON Schema for tool records.

## Design rules

1. Stable IDs are more important than pretty labels.
2. A tool result is never silently promoted to a factual conclusion.
3. Every important relation should be explainable through evidence or methodology.
4. Public GitHub content contains methods and synthetic/general examples, not sensitive case data.
5. AI-generated synthesis must remain grounded in underlying source evidence.

The generated CSV and GitHub Pages search index are **derived artifacts**. Update canonical knowledge first, then run `python scripts/build_catalog.py`.
