# “I Have…” Investigation Router

The router starts with the evidence or observable already available, not with a favorite tool.

```text
I HAVE...
   |
   +-- username ----> identity discovery -> platform verification -> archive -> correlation
   +-- domain ------> RDAP -> certificates/DNS -> indexed services -> archive -> CTI context
   +-- URL ---------> passive scan/archive -> reputation context -> domain pivots
   +-- image -------> hash/metadata -> reverse search -> visual clues -> GEOINT validation
   +-- company -----> official registry -> identifiers -> filings/procurement -> relationship map
   +-- document ----> preserve/hash -> metadata/text -> entities -> primary-source verification
   +-- IOC ---------> multi-source enrichment -> infrastructure -> behavior context -> report
   +-- location ----> maps -> street imagery -> satellite/terrain -> alternative hypothesis
```

## Router contract

A route should return:

- recommended next **methodological step**;
- relevant source/tool categories;
- known caveats;
- expected output types;
- verification requirements;
- specialist project in the Ridd1kulusC0d3r ecosystem when one exists.

It should **not** imply that every available pivot must be used.

The executable routing data lives in [../knowledge/playbooks.json](../knowledge/playbooks.json) and [../knowledge/inputs.json](../knowledge/inputs.json).
