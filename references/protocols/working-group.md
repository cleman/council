# Protocol: working groups and research brief

A working group (WG) is a **researcher** followed by an **adversarial verifier**. The verifier is what turns a research summary into something the council can rely on: in testing, verifiers corrected 5–8 claims per group (wrong scope of a figure, a source misread, an outdated date, a missing counter-source).

## Choosing the groups

Split the subject so that groups don't overlap. A pattern that works for decisions about acting in the world:

- **WG1 — Facts & narratives:** what happened, who claims what, and the evidence for each side.
- **WG2 — Options, calendar & leverage:** the options or strands, their dates, deadlines, decision-makers, odds.
- **WG3 — Rules, risk & profiles:** law, contracts, safety; how risk differs by profile; alternatives.

Adapt to the subject (e.g. Market / Product / Unit economics for a launch decision). Subject-specific factors may add a WG4.

**Standard level** uses a single researcher (or two in parallel on different scopes) and no verifier.

## Researcher prompt

```
You are the RESEARCHER of Working Group <n> (<scope>) for a council.
Read <run>/charter.md first (quality rules are binding).
<If a previous run exists: "Read <files>. Your job is to UPDATE and CORRECT, not redo.">

Tasks (use web search, fresh results for news; at least <8–10> queries; include
independent AND official sources; deliberately search beyond the mainstream on contested
topics, and tag every source's leaning):
1. <task>
2. <task>
…
N. Anything in prior material that now looks wrong.

Write a concise report (500–800 words), every claim graded
CORROBORATED / CREDIBLE / ALLEGED / CONTRADICTED / UNKNOWN with a URL,
to <run>/wg<n>-draft.md. Say plainly if you could not open primary texts.
Return a 3-line summary.
```

## Verifier prompt

```
You are the adversarial VERIFIER of Working Group <n>.
Read <run>/charter.md, then <run>/wg<n>-draft.md.
Pick the 6–8 claims that matter most for the person's decision and re-check them
(~8 queries). Look for over- and under-grading, outlet bias in either direction, figures
whose scope is misread, outdated items, and missing counter-evidence. Downgrade anything
resting only on interested sources unless corroborated.
Write the FINAL report to <run>/wg<n>.md (500–800 words): corrected content, grades, URLs,
plus "Verifier notes" (what you changed and why) and "Still UNKNOWN".
Return a 3-line summary.
```

Run all researchers in parallel; start each verifier as soon as its researcher is done.
