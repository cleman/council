# Protocol: chairman synthesis

At Quick level the orchestrating session may write the synthesis itself. At Standard and above, spawn a **separate agent** with no seat, so the synthesis isn't written by whoever ran the process.

## Prompt (Deep, Full)

```
You are the CHAIRMAN of a council. Read everything in <run>/: charter.md (binding),
the quality charter, any earlier report's review (avoid every flaw it lists), the research
files, every fact desk (later override earlier), all openings and all room outputs.
The last red-team room lists remaining charter breaches: fix all of them.

Write the verdict to <run>/verdict-draft.md in <reader language>, plain words, following
the Deep/Full structure in references/report-spec.md (keep only the sections that apply;
each point said once). Target 1,400–2,000 words.

Rules: every factual claim graded; key URLs inline; source leanings tagged on both sides;
no policy position presented as the council's advice; each side's case shown with its
evidence before any assessment; include "postponed/unknown" scenarios in the decision
guide; dated rules for what can't be known today; no self-awarded independence.
The chairman may side with a minority if its reasoning is stronger — say why.
Return a 5-line summary.
```

## Prompt (Quick, Standard) — the original structure

```
You are the Chairman of a council. Synthesize the advisors' responses and the peer
review(s) into a verdict in <reader language>:
## The 60-second version
## Where the council agrees
## Where the council clashes
## Blind spots the council caught
## The recommendation   (a real answer, not "it depends" unless it truly does — then say on what)
## The one thing to do first   (one step; neutral on contested causes)
## Limits
Be direct. Grade factual claims. Follow the quality charter.
```

## Revision pass

After the audit, resume the chairman with the audit file:

```
The internal audit is in <run>/audit.md. Apply ALL required fixes exactly, plus these
optional ones: <list>. No new repetition. Save to <run>/verdict.md (leave the draft
untouched) and list what you changed.
```
