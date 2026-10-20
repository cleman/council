# Protocol: fact desk

The fact desk answers the council's information requests between rounds. It is where conflicts between sources get settled. In testing it resolved a 1,800-vs-2,397 conflict over an official figure (successive provisional counts of the same event), showed that a widely repeated rule of thumb was contradicted by city-level data, and established a legal point that changed a cell of the risk matrix.

## Collecting requests

After openings and after each round:
1. Gather every "Information requests" section.
2. Merge duplicates. A question asked by several seats goes first.
3. Split into **knowable now** and **not knowable today** (future votes, orders, routes, announcements).
4. If nothing knowable remains, skip the agent and write a short `factdesk<n>.md` yourself that turns the unknowables into dated decision rules.

## Prompt

```
You are FACT DESK <n> for a council. Read <run>/charter.md (binding).
Today is <date>; anything dated after today cannot be known — say so rather than guess.
Context: <files with the conflicting claims>.
Answer precisely, graded CORROBORATED / CREDIBLE / ALLEGED / CONTRADICTED / UNKNOWN, with
URLs and source leanings:
1. <question>
2. <question>
…
Where two earlier files conflict, say which is right and why (scope, date, source).
Write 300–600 words to <run>/factdesk<n>.md and return a 3–4 line summary.
```

Run one or two fact desks in parallel when the questions split cleanly (e.g. "politics & calendar" vs "law & local data").

## Rule

Later fact desks override earlier files. Record every grade change for `run.json` → `facts` (the "how the facts moved" panel).
