# Analyst Workflow

A tool is a component. The investigation is the system.

## 1. Define the question

Write the question before collecting anything.

Good:

> Which public evidence supports or contradicts the hypothesis that these two online identities are related?

Bad:

> Find everything about this person.

Define:

- decision to support;
- target/unit of analysis;
- time window;
- allowed data classes;
- legal/ethical basis;
- stopping condition.

## 2. Build an input map

Normalize what you already have.

| Input | Normalize into |
|---|---|
| Name | spelling variants, transliterations |
| Username | exact handle, variants, platform context |
| E-mail | local part, domain, provider |
| Phone | E.164, country/area code |
| Domain | root domain, subdomains, DNS, certificates |
| IP | IP, ASN, netblock, historical context |
| URL | domain, path, parameters, archive state |
| Image | original file, hash, metadata, visual clues |
| Document | hash, metadata, author, timestamps, embedded URLs |
| Company | legal name, aliases, registry number, officers |
| IOC | type, first/last observed, source, confidence |

## 3. Source plan

Use source classes deliberately:

1. primary/official records;
2. platform-native public data;
3. archives and historical snapshots;
4. independent databases;
5. search engines and aggregators;
6. third-party enrichment.

Do not silently treat an aggregator as the original source.

## 4. Collect with provenance

For every meaningful observation, record:

- source URL;
- access time;
- query or input;
- exact observation;
- screenshot/export/hash when appropriate;
- collection limitations;
- analyst notes.

## 5. Verify

Use at least two independent signals for important claims whenever feasible.

Check:

- source authority;
- temporal consistency;
- location consistency;
- identifier reuse;
- contradictions;
- data freshness;
- collection coverage.

## 6. Correlate

A relation should have a reason.

Useful relation types:

- same identifier;
- same infrastructure;
- same document;
- same account reference;
- same organization;
- temporal co-occurrence;
- shared media;
- explicit public statement.

Avoid vague edges such as `related_to` without evidence.

## 7. Analyze competing explanations

For each conclusion, keep:

- primary hypothesis;
- alternative hypothesis;
- supporting evidence;
- contradicting evidence;
- information gaps;
- confidence;
- what would change the assessment.

## 8. Report

Separate:

**Observed fact** → what the source actually showed.  
**Assessment** → what you infer from the facts.  
**Confidence** → how strongly the evidence supports the assessment.

## Suggested tool sequence

```text
Search/Discovery
      ↓
Primary Source
      ↓
Archive / Historical Check
      ↓
Identity / Infrastructure / Media Pivot
      ↓
Verification
      ↓
Graph / Timeline
      ↓
Hypothesis Review
      ↓
Report
```

## Quality gates

Before closing a case:

- [ ] scope is explicit;
- [ ] collection is reproducible;
- [ ] important claims cite evidence;
- [ ] sources are not all copies of one another;
- [ ] contradictions are recorded;
- [ ] personal data is minimized;
- [ ] confidence is stated;
- [ ] alternative explanations were considered;
- [ ] report distinguishes fact from inference;
- [ ] sensitive data is not unnecessarily exposed.
