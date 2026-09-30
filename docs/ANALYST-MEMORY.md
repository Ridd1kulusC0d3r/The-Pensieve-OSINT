# Analyst Memory

`memory/` preserves reusable tradecraft lessons.

## What belongs here

- common false-positive patterns;
- source-specific quirks;
- normalization lessons;
- verification heuristics;
- recurring analytical failure modes;
- sanitized lessons learned;
- query patterns that do not expose private case data.

## What does not belong here

- case subjects;
- private identifiers;
- credentials;
- tokens;
- private screenshots;
- sensitive evidence;
- personal data that is unnecessary for teaching the pattern.

## Pattern format

Each pattern should contain:

1. **Observation** — what analysts commonly see.
2. **Possible explanations** — competing hypotheses.
3. **Do not infer** — the tempting unsupported conclusion.
4. **Useful checks** — lawful verification directions.
5. **Confidence impact** — how the pattern should change assessment confidence.

This memory layer is intentionally public-safe and reusable.
