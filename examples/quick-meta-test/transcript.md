# LLM Council Transcript — 2026-10-20

## Original question
Install the llm-council skill and test it (meta-test: council the decision about the skill itself).

## Framed question
A Claude Code user just installed "llm-council" (prompt-only SKILL.md: 5 persona advisors → 5 anonymized peer reviewers → chairman; ~11 calls/run). Known weaknesses: same-model persona diversity, weak anonymization, 5 identical persona-less reviewers, cost + broad auto-triggers, no LICENSE, desktop-only "open the HTML file". Decision: (a) use as-is, (b) fork and fix, (c) skip and ask Claude for pros/cons when needed.

## Advisor responses
**Contrarian → (c) + delete strong triggers.** Nobody has shown it beats one well-prompted answer. Same-model consensus = correlated error, laundered into apparent rigor. `model` param only swaps Claude tiers, so the fork can't buy real diversity. Triggers are the real silent cost. Test council vs. single prompt on five past decisions before forking.

**First Principles → closest to (c).** Decision support adds value by (1) surfacing new considerations (needs real diversity) and (2) forcing commitment to criteria (needs structure). Personas deliver #2 and fake #1. The bottleneck is context, not perspectives. Better: criteria-and-weights first, one adversarial pass, name the missing info that would flip the answer. If kept: mandatory trigger only, cut peer review.

**Expansionist → (b) as a platform.** Mixed models as a measuring instrument; transcripts as a decision journal with outcome follow-ups; tiered "council-lite" mode; modular personas (security, customer, PR-merge, hiring councils); publish reports as artifact links.

**Outsider → (c) with one cheap test.** It's one AI grading its own homework in five costumes — theater that feels rigorous. Forking = maintaining software to make the theater more convincing. Broad triggers look like a bug to anyone. Compare once against "strongest case against my preferred option"; uninstall if nothing new. Kill triggers today.

**Executor → (b), timeboxed to 20 min.** 1) Delete STRONG TRIGGERS (2 min, do today regardless). 2) 5 reviewers → 1 (11→7 calls). 3) `model:` on 2–3 advisors, don't oversell it. 4) Publish as artifact / print inline. 5) Add LICENSE. Then one real test; if not better than a "steelman both sides" prompt, delete → (c).

## Peer reviews
Anonymization map: A = Executor, B = Outsider, C = Contrarian, D = Expansionist, E = First Principles.

| Reviewer | Strongest | Biggest blind spot | What all missed |
|---|---|---|---|
| 1 | A | D | Trigger fix is a local edit, do it now; supply-chain risk; no definition of "better"; require real context as input |
| 2 | A | D | No LICENSE → unclear right to share fork; tests are unblinded & n too small; context starvation |
| 3 | A | D | Fair test needs blind comparison on known-outcome decisions; read community SKILL.md before running |
| 4 | A | D | Security/provenance; context starvation; 4-min latency breaks flow |
| 5 | A | D | Input problem; cheap real diversity via giving advisors different evidence/tools; security; fork drift |

5/5 identical top-level verdicts — empirical confirmation of weakness #3 (persona-less reviewers are near-duplicates).

## Chairman verdict
### Where the council agrees
- The broad auto-triggers must go **today**, whatever else you decide (5/5 advisors).
- Mixed Claude tiers ≠ real diversity; don't oversell it (4/5, all reviewers).
- The skill's value over one good prompt is unproven; any next step should include a test with a kill condition (4/5).

### Where the council clashes
- **Fork vs. skip.** Executor/Expansionist: edits are cheap, so make them and learn. Contrarian/First Principles/Outsider: polishing an unproven premise is wasted effort. The disagreement is really about whether 20 minutes is "cheap" — it is.
- **Scope.** Expansionist wants a platform; everyone else (and every reviewer) calls that scope creep on an untested core.

### Blind spots the council caught
- **Context starvation**: advisors reason from a two-sentence summary, not the user's real constraints — this matters more than model diversity.
- **Test design**: proposed comparisons are unblinded, n=1, with no definition of "better".
- **Provenance**: read third-party skills before running (done here — the SKILL.md is clean, prompt-only); no LICENSE means a private fork is fine but sharing is murky.
- **The reviewers proved the point**: five identical verdicts = one review paid for five times.

### The recommendation
Option (b), minimal and timeboxed — Executor's plan — with First Principles' twist: make the council demand real context. Fork privately; delete strong triggers; collapse to 1 reviewer; replace "open the HTML" with publish/inline output. Skip the platform ideas until it earns a second use.

### The one thing to do first
Delete the STRONG TRIGGERS block from the skill's `description` so it only fires on "council this" / "run the council".
