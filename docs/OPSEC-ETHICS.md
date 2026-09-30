# OPSEC, Ethics and Responsible Use

Open sources are public; that does not make every use automatically appropriate.

## Minimum standard

- work within applicable law, policy and authorization;
- collect only what is relevant to the stated purpose;
- minimize personal data;
- do not publish unnecessary sensitive information;
- preserve provenance;
- document uncertainty;
- avoid harassment, impersonation or deceptive interaction;
- respect platform terms and access controls;
- use synthetic or authorized data for training whenever possible.

## Analyst OPSEC

Prefer passive collection unless active interaction is explicitly authorized.

Separate:

- analyst identity;
- research browser profile;
- case notes;
- credentials/API keys;
- exported evidence.

Do not put secrets, session tokens, private keys or case-sensitive data in Git repositories.

## Evidence hygiene

For material used in an assessment:

- preserve source URL and access time;
- hash exported files where useful;
- keep originals separate from transformed copies;
- note timezone;
- note whether content was live, cached or archived;
- record tool/version when processing could affect the result.

## Correlation caution

The following are **signals, not automatic identity proof**:

- same username;
- same avatar;
- same display name;
- shared hosting;
- shared IP;
- similar writing style;
- common followers;
- same geolocation region;
- visually similar image.

Require corroboration proportional to the consequence of the conclusion.

## AI use

AI may help with:

- summarization;
- extraction;
- translation;
- clustering;
- query generation;
- report drafting.

AI should not silently become the source of a factual claim. Keep the underlying source evidence and mark model-generated synthesis.

## Publishing

Before publishing a report, ask:

1. Is this information necessary?
2. Is it supported?
3. Could redaction preserve the analytic value?
4. Does the report distinguish observation from inference?
5. Could a reasonable reader reproduce the conclusion?
