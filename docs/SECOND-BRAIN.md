# The Pensieve as an Analyst Second Brain

The Pensieve is not designed to be the biggest list of OSINT links. It is designed to preserve **analyst memory and decision context**.

## Memory model

```text
Knowledge             Analyst Memory            Temporal Memory
tools/sources         patterns/pitfalls         health/changes
      \                    |                    /
       \                   |                   /
        +------------ Knowledge Graph --------+
                         |
                         v
                  Retrieval / Routing
                         |
                         v
                Evidence-aware workflow
```

### 1. Declarative memory — what exists

Stored in `knowledge/`:

- tools and services;
- public/official sources;
- input and output types;
- intelligence disciplines;
- project ecosystem;
- playbooks;
- semantic relations.

### 2. Procedural memory — how to investigate

Stored in `knowledge/playbooks.json` and human-readable documentation.

Every playbook defines:

- input type;
- intended analytical question;
- ordered steps;
- recommended resources;
- known failure modes.

### 3. Episodic-pattern memory — what analysts learn

Stored in `memory/`.

Only reusable, sanitized lessons belong here. **Do not place sensitive case material, personal data, credentials, or private evidence in the public repository.**

### 4. Temporal memory — what changed

Generated into `data/health.json` and `data/HEALTH-DIFF.md`.

The system distinguishes:

- active;
- degraded;
- blocked from automated checks;
- redirected;
- unavailable;
- replaced.

A failed automated request is not automatically a dead service.

## Core reasoning rule

```text
observation != inference
correlation != identity
shared infrastructure != ownership
reputation label != attribution
absence != evidence unless collection coverage supports it
```

## Design target

The long-term interface should be able to answer:

- “I have a username. What can I verify next?”
- “Which passive sources accept a domain?”
- “What outputs from these tools are only leads?”
- “Which sources cover Brazil?”
- “Which project in this ecosystem implements this workflow?”
- “Which analytical steps have not yet been performed?”
- “What changed in the tool/source landscape since the last review?”

That is the distinction between a bookmark collection and an analyst second brain.
