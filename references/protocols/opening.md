# Protocol: opening positions

Every seat writes an independent opening position. Spawn them all at once; none sees another's.

## Prompt (Standard, Deep, Full)

Write the shared part once to `<run>/member-prompt.md` and give each agent its seat:

```
You are a member of a council. Your seat: <Seat> (slug: <slug>).
Read <run>/charter.md (your seat description is there; quality rules are binding),
then the research files: <wg1.md, wg2.md, … or brief.md>.
You may run up to 3 web searches for anything decisive that's missing.

Write your OPENING POSITION from your seat's perspective: direct, specific, no hedging,
lean fully into your angle. 200–350 words:
1. Your position — what the person should do, conditional on their goals/profile where
   relevant, neutral on contested causes.
2. Your 2–3 strongest arguments, each tied to evidence (cite grades).
3. "Information requests": up to 2 precise factual questions that could change your
   position (or "none").

Save to <run>/opening-<slug>.md and return the text.
```

## Prompt (Quick — the original skill's advisor prompt)

```
You are <Seat> on a council.
Your thinking style: <description>
A user has brought this question to the council:
---
<framed question>
---
Respond from your perspective. Be direct and specific. Don't hedge or try to be balanced.
Lean fully into your assigned angle. 150–300 words. No preamble.
```

## After the openings

Merge the information requests (several seats often ask the same thing: that is a strong signal) and send them to the fact desk before the first room or rebuttal.
