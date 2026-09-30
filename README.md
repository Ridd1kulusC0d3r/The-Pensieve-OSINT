# The Pensieve OSINT

> **An analyst second brain for Open-Source Intelligence.**  
> Searchable arsenal · evidence-aware playbooks · analyst memory · knowledge graph · Brazil/LATAM sources · machine-readable knowledge for AI agents.

[Web Explorer](https://ridd1kulusc0d3r.github.io/The-Pensieve-OSINT/) · [Português](README.pt-BR.md) · [Arsenal](docs/ARSENAL.md) · [I Have… Router](docs/ROUTER.md) · [Second Brain](docs/SECOND-BRAIN.md) · [AI Discovery](docs/AI-DISCOVERY.md) · [Brazil & LATAM](docs/BRAZIL-LATAM.md)

---

## Not another bookmark dump

A directory can tell you that a tool exists. An analyst second brain should also remember what input you have, which methodological step comes next, what a tool can produce, what that output does not prove, which sources should corroborate it, which failure patterns should lower confidence, which specialist project handles the job, and what changed since the last review.

~~~text
WHAT I HAVE
    ↓
NORMALIZE → PLAN → DISCOVER → COLLECT → VERIFY → CORRELATE → ANALYZE → REPORT
    │             │                         │
    │             └──── tools/sources ──────┤
    └──── input semantics                   │
                                            ↓
                         caveats + analyst memory + confidence
~~~

## Start here

| Need | Entry point |
|---|---|
| Search/filter the arsenal | [Web Explorer](https://ridd1kulusc0d3r.github.io/The-Pensieve-OSINT/) |
| Start from a username/domain/image/etc. | [“I Have…” Router](docs/ROUTER.md) |
| Browse tools by function | [OSINT Arsenal](docs/ARSENAL.md) |
| Follow a repeatable investigation process | [Analyst Workflow](docs/WORKFLOW.md) |
| Understand the memory architecture | [Second Brain](docs/SECOND-BRAIN.md) |
| Explore relationships | [Knowledge Graph](docs/KNOWLEDGE-GRAPH.md) |
| Reuse analyst lessons | [Analyst Memory](memory/README.md) |
| Work with Brazil/LATAM public sources | [Brazil & LATAM](docs/BRAZIL-LATAM.md) |
| Navigate my related OSINT projects | [Ridd1kulusC0d3r OSINT Ecosystem](docs/ECOSYSTEM.md) |
| Consume structured data | [knowledge/](knowledge/) |
| Let an AI agent understand the repo | [llms.txt](llms.txt) · [ai-index.json](ai-index.json) · [AGENTS.md](AGENTS.md) |
| Review legal/ethical boundaries | [OPSEC & Ethics](docs/OPSEC-ETHICS.md) |

## “I Have…” routing

The interface starts with the observable, not the analyst's favorite tool.

| You have | Typical route |
|---|---|
| **username** | discovery → platform-native verification → archive → correlation |
| **domain** | RDAP → certificates/DNS → indexed services → archive → CTI context |
| **URL** | passive scan/archive → reputation context → infrastructure pivots |
| **IP** | registration/ASN → indexed services → defensive CTI context |
| **image** | preserve/hash → metadata → reverse search → GEOINT validation |
| **company** | official registry → identifiers → filings/procurement → relationship map |
| **document** | preserve/hash → metadata/OCR → entities → primary-source verification |
| **IOC** | multi-source enrichment → infrastructure → behavior context → reporting |
| **location** | maps → street imagery → satellite/terrain → alternative hypothesis |

Machine-readable playbooks live in [knowledge/playbooks.json](knowledge/playbooks.json).

## Second-brain layers

| Layer | Stored in | Purpose |
|---|---|---|
| **Declarative memory** | knowledge/ | tools, sources, inputs, outputs, taxonomy, projects |
| **Procedural memory** | knowledge/playbooks.json | repeatable investigation plans |
| **Analyst memory** | memory/ | false positives, pitfalls, reusable lessons |
| **Relational memory** | knowledge/relations.json | graph relationships |
| **Temporal memory** | data/health.json | source/tool reachability changes |
| **Retrieval layer** | GitHub Pages | search, filters, “I Have…”, graph explorer |
| **AI discovery layer** | llms.txt, ai-index.json, JSON-LD | explicit machine navigation |

## Machine-readable knowledge

The canonical layer is **JSON**, not the CSV export.

~~~text
knowledge/
├── tools.json
├── inputs.json
├── outputs.json
├── sources.json
├── projects.json
├── playbooks.json
├── int-taxonomy.json
├── relations.json
└── schema.json
~~~

data/tools.csv is generated for convenience by scripts/build_catalog.py.

### For AI agents

Read in this order:

1. [llms.txt](llms.txt)
2. [ai-index.json](ai-index.json)
3. [knowledge/README.md](knowledge/README.md)
4. the relevant canonical JSON
5. explanatory docs and analyst-memory patterns

See [AGENTS.md](AGENTS.md) for constraints. The repository deliberately states non-equivalences such as:

> username match ≠ identity proof  
> shared infrastructure ≠ ownership  
> reputation label ≠ attribution  
> archive capture time ≠ publication time  
> no result ≠ evidence of absence

## Intelligence taxonomy

Pensieve maps open-source work across **OSINT, SOCMINT, GEOINT, IMINT, CYBINT, CTI, FININT, TECHINT and DOMEX**. HUMINT, SIGINT, MASINT and MEDINT are included only for taxonomy context, not as operational collection guidance.

See [Intelligence Taxonomy](docs/INTELLIGENCE-TAXONOMY.md).

## Ridd1kulusC0d3r OSINT ecosystem

Pensieve is the navigation and memory layer. Specialized work remains specialized:

- **[Mineiro Username Intelligence](https://github.com/Ridd1kulusC0d3r/Mineiro-OSINT-Extractor)** — username/public-presence evidence and correlation.
- **[T.O.C.A.I.A](https://github.com/Ridd1kulusC0d3r/tocaia-osint)** — behavioral OSINT, collection coverage and meaningful absence.
- **[OSINT Checklist](https://github.com/Ridd1kulusC0d3r/osintchecklist)** — method, logbook, evidence, entities, timeline and findings.
- **[F.I.O. Lab](https://github.com/Ridd1kulusC0d3r/FIO)** — Brazilian public-data and identifier research.
- **[Tropeiro Intel](https://github.com/Ridd1kulusC0d3r/tropeiro-intel)** — defensive OSINT / CTI for phishing and fraud campaigns.
- **[OSINT](https://github.com/Ridd1kulusC0d3r/OSINT)** — fundamentals, labs and templates.
- **[OSINT Uai](https://github.com/Ridd1kulusC0d3r/OsintUAI)** — podcast and educational material.
- **[T4lks](https://github.com/Ridd1kulusC0d3r/T4lks)** — talks, workshops and research.

Full map: [docs/ECOSYSTEM.md](docs/ECOSYSTEM.md).

## Curation and health

A working URL is not proof of analytical quality, and an automated 403 is not proof that a service is dead. Pensieve therefore separates catalog status, best-effort reachability, analytical caveats and human review date.

Weekly health snapshots are produced by [scripts/health_check.py](scripts/health_check.py). Link and knowledge validation run in GitHub Actions.

## Responsible use

Use public, lawful and authorized sources. Minimize unnecessary personal data, preserve provenance, separate observation from inference and document uncertainty. Public analyst memory must contain **sanitized methods and patterns, not sensitive case data**.

See [OPSEC & Ethics](docs/OPSEC-ETHICS.md).

---

**Status: v0.3 Second Brain foundation** — structured knowledge, searchable Pages interface, input-first routing, playbooks, analyst memory, knowledge graph, AI-agent manifests, health monitoring and regional intelligence packs.
