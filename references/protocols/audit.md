# Protocol: internal quality audit

An adversarial agent checks the chairman's draft against the quality charter and spot-checks the facts that matter most. In testing it found 11 required fixes in a draft that looked finished: a sentence that took sides, two legal points that understated the risk, inconsistent grades, glossary terms never used.

It is an **internal** audit — same process, same model. The report must call it that and must not headline its score (quality charter §10). The strongest check remains an external review by a person; offer one after delivery.

## Prompt

```
You are the QUALITY AUDITOR of a council. Read <run>/charter.md, the quality charter,
any previous external review of an earlier report (the bar to beat), and
<run>/verdict-draft.md. Spot-check facts against the research and fact-desk files (later
override earlier). You may run up to 4 web searches to verify the 3–4 most
decision-relevant claims.

Audit against: neutrality on contested causes; honest status-quo case; each side's case
shown with its evidence; internal consistency (tables vs text vs grades); exact
categories; complete risk picture; grading honesty (method vs grade); symmetric source
tagging; reader-friendliness (language, jargon, glossary, repetition, phone tables);
actionability; scenarios incl. "postponed/unknown".

Write to <run>/audit.md (≤500 words): an indicative score /10, then numbered REQUIRED
fixes (section, current wording, replacement or instruction), then optional improvements.
Return the score and the required fixes.
```

## Light self-check (Standard)

Instead of a separate auditor, the chairman ends with:

```
Before saving, re-read your verdict against the quality charter's ten rules. Fix any
breach and add one line at the end: "Self-check: <rules you had to fix>".
```
