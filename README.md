# The Pensieve OSINT

> **An analyst's second brain for Open-Source Intelligence.**  
> Curated tools, investigation workflows, public-data sources, verification resources, cyber/CTI pivots, Brazil/LATAM references and the Ridd1kulusC0d3r OSINT ecosystem.

[Português](README.pt-BR.md) · [Arsenal](docs/ARSENAL.md) · [Workflow](docs/WORKFLOW.md) · [Brazil & LATAM](docs/BRAZIL-LATAM.md) · [My OSINT ecosystem](docs/ECOSYSTEM.md) · [OPSEC & Ethics](docs/OPSEC-ETHICS.md)

---

## Why this repository exists

OSINT directories are easy to build and surprisingly easy to make useless. A thousand links without context is not an investigation system.

**The Pensieve OSINT** is organized around the analyst's actual questions:

```text
QUESTION
   ↓
SCOPE → PLAN → DISCOVER → COLLECT → VERIFY → CORRELATE → ANALYZE → REPORT
   ↓         ↓          ↓          ↓           ↓
  law     sources     evidence   confidence   decision
```

The repository combines:

- **tool discovery** — curated by investigative function;
- **method** — what to do before and after opening a tool;
- **input-oriented pivots** — username, e-mail, domain, IP, URL, image, company, document, location, IOC and more;
- **verification** — provenance, corroboration, source quality and uncertainty;
- **regional intelligence** — dedicated Brazil/LATAM public-data references;
- **cyber + CTI** — infrastructure, IOC enrichment and threat-intelligence resources;
- **automation** — frameworks, graphing and machine-readable catalogs;
- **responsible use** — privacy, legal boundaries, source preservation and analyst OPSEC.

## Start here

| Need | Go to |
|---|---|
| Find a tool by task | [OSINT Arsenal](docs/ARSENAL.md) |
| Follow a repeatable investigation process | [Analyst Workflow](docs/WORKFLOW.md) |
| Investigate Brazil/LATAM public sources | [Brazil & LATAM](docs/BRAZIL-LATAM.md) |
| Explore my related OSINT projects | [Ridd1kulusC0d3r OSINT Ecosystem](docs/ECOSYSTEM.md) |
| Use the catalog programmatically | [data/tools.csv](data/tools.csv) |
| Review legal, ethical and OPSEC boundaries | [OPSEC & Ethics](docs/OPSEC-ETHICS.md) |
| Contribute a tool or source | [CONTRIBUTING.md](CONTRIBUTING.md) |
| See what comes next | [ROADMAP.md](ROADMAP.md) |

## Investigation map

| Surface | Examples of pivots |
|---|---|
| Search & discovery | keyword, quote, document, cached page |
| Identity | name, username, e-mail, phone number |
| Social platforms | profile, handle, post, channel, media |
| Web infrastructure | domain, subdomain, DNS, certificate, IP, ASN |
| Media verification | image, video, metadata, frame, source |
| Geospatial | coordinates, map, satellite, terrain, shadow |
| Organizations | company, officer, registry, procurement, sanction |
| Transport | aircraft, vessel, airport, port |
| Documents | PDF, metadata, OCR, archives, public records |
| Cyber / CTI | IOC, malware, passive DNS, reputation, ATT&CK context |
| Research | academic paper, dataset, citation, historical record |
| Analysis | graph, timeline, evidence register, hypothesis testing |

## Core external references

These are useful starting points when the local catalog does not cover a niche:

- [Bellingcat Online Investigation Toolkit](https://bellingcat.gitbook.io/toolkit)
- [OSINT Framework](https://osintframework.com/)
- [Awesome OSINT](https://github.com/jivoi/awesome-osint)
- [Awesome OSINT Repositories](https://github.com/osintshifu/awesome-osint-repos)
- [OSINT.dev](https://osint.dev/)
- [IntelTechniques Search Tools](https://inteltechniques.com/tools/)
- [OSINT Combine](https://www.osintcombine.com/free-osint-tools)

## Ridd1kulusC0d3r OSINT ecosystem

This repository is the **hub**. The specialized work happens elsewhere:

- **[Mineiro Username Intelligence](https://github.com/Ridd1kulusC0d3r/Mineiro-OSINT-Extractor)** — username/public-presence workbench with evidence and correlation.
- **[T.O.C.A.I.A](https://github.com/Ridd1kulusC0d3r/tocaia-osint)** — behavioral OSINT and analysis of meaningful absence.
- **[OSINT Checklist](https://github.com/Ridd1kulusC0d3r/osintchecklist)** — method, decision flow, logbook and auditable investigation workflow.
- **[F.I.O. Lab](https://github.com/Ridd1kulusC0d3r/FIO)** — Brazilian public-data and identifier analysis laboratory.
- **[Tropeiro Intel](https://github.com/Ridd1kulusC0d3r/tropeiro-intel)** — defensive OSINT / CTI for phishing and fraud campaigns.
- **[OSINT](https://github.com/Ridd1kulusC0d3r/OSINT)** — study base, labs, templates and methodology.
- **[OSINT Uai](https://github.com/Ridd1kulusC0d3r/OsintUAI)** — podcast and educational material.
- **[T4lks](https://github.com/Ridd1kulusC0d3r/T4lks)** — talks, workshops and research material.

See the full map in [docs/ECOSYSTEM.md](docs/ECOSYSTEM.md).

## Curation standard

A resource should answer at least one of these questions:

1. **What input does it accept?**
2. **What evidence does it produce?**
3. **How can another analyst reproduce the result?**
4. **What are the limitations, cost, account or API requirements?**
5. **Is it still useful enough to keep?**

Tools can disappear, become paid, break APIs or quietly change behavior. Link validation is automated, but **a working URL is not proof that a tool is analytically reliable**.

## Responsible use

Use public, lawful and authorized sources. Minimize unnecessary personal data, preserve provenance, separate observation from inference and document uncertainty. Do not treat a username match, image similarity, shared infrastructure or graph edge as automatic proof of identity or attribution.

See [OPSEC & Ethics](docs/OPSEC-ETHICS.md).

---

**Status:** v0.1 foundation — curated arsenal, workflow, regional sources, own-project ecosystem, machine-readable catalog and link checking.
