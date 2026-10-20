# Triage: difficulty factors and levels

## 1. Standard difficulty factors

Score each factor 0, 1 or 2. Write one short reason per factor; the user sees them in the proposal.

| Factor | 0 | 1 | 2 |
|---|---|---|---|
| **Stakes** — cost of a wrong call | small, easily absorbed | significant money, time, reputation | health, safety, freedom, livelihood, legal status |
| **Reversibility** | trivially reversible | reversible at a cost | hard or impossible to undo |
| **Fresh facts needed** | answerable from general knowledge | some facts to check | depends on recent events, prices, laws, dates |
| **Contestedness** | no real controversy | experts disagree | politically or socially divided; competing narratives |
| **Strands** — distinct sub-questions, options or stakeholders | one | two or three | four or more, or options that are really different questions |
| **Personal / legal risk** to the person asking | none | indirect | direct (arrest, sanctions, contract, immigration status…) |
| **Time pressure** | none | weeks | days; deadlines inside the decision window |

## 2. Subject-specific factors

After scoring, ask: *what does this subject need that the table does not capture?* Add 0–3 factors, each with a one-line reason and its effect. Examples:

- "Medical or safety question" → add a Domain Expert seat; grade claims against clinical sources.
- "Outcome depends on an unknown future event (vote, ruling, earnings)" → require dated decision rules; add scenarios.
- "Involves minors / vulnerable people" → add a risk-by-profile matrix; raise the level by one if Stakes < 2.
- "Strong local variation (city, country, jurisdiction)" → add the Context Realist seat.
- "Information environment is polluted (misinformation on several sides)" → add a verifier to every working group; tag source leanings.
- "Creative or strategic question with no facts to check" → drop working groups; keep rebuttal rounds.

Subject-specific factors can change the configuration directly (a seat, a working group, a matrix) even when they don't change the total score.

## 3. From score to level

Total of the 7 standard factors (0–14), then apply overrides.

| Score | Level |
|---|---|
| 0–3 | **Quick** |
| 4–7 | **Standard** |
| 8–10 | **Deep** |
| 11–14 | **Full** |

Overrides:
- Any factor at 2 for **Stakes** *and* **Personal / legal risk** → at least **Deep**.
- **Fresh facts needed** = 2 → at least **Standard** (Quick has no research).
- **Contestedness** = 2 → the quality charter's neutrality rules are mandatory, and a Status-quo seat is required.
- The user's choice always wins.

## 4. Default configurations

| | Quick | Standard | Deep | Full |
|---|---|---|---|---|
| **Research** | none | 1–2 researchers, one brief | 3 working groups, each researcher → adversarial verifier | 3–4 working groups, each researcher → verifier |
| **Expert panels** (`experts.md`) | — | 1 domain × 2 experts | 2–3 domains × 2 experts | 3–4 domains × 2–3 experts |
| **Seats** | 5 core | 5 core + 1 chosen | 7 (5 core + Status-quo + 1 context/specialist) | 7–9 |
| **Debate** | openings | openings → 1 rebuttal round | openings → 2 rounds × 2 rooms (≈60% of seats each, random, balanced) | openings → 3 rounds × 2 rooms; last round includes a red-team room |
| **Fact desk** | — | on request | between every round | between every round |
| **Reframe loop** | — | — | available (back to triage once) | available |
| **Peer review** | 1 anonymous reviewer | 1–2 anonymous reviewers | replaced by rooms + audit | replaced by rooms + audit |
| **Chairman** | yes | yes | yes (separate agent) | yes (separate agent) |
| **Audit** | — | light self-check against the charter | internal audit → revision | internal audit → revision; offer external review → v2 |
| **Outputs** | report + transcript | report + transcript | report + process map + transcript + run folder | same, plus revision history |
| **Agents (approx.)** | ~7 | ~14–17 | ~26–34 | ~36–50 |
| **Duration (approx.)** | 2–4 min | 6–10 min | 15–25 min | 25–45 min |

Why only one peer reviewer at Quick: five reviewers with the same prompt and no persona produce near-identical reviews (observed in testing: 5 of 5 picked the same "strongest" and "weakest" response). One reviewer gives the same signal for a fifth of the cost.

Agent counts include expert hearings (each hearing = one agent per expert). Design / Build mode adds an architect and its revisions (about 3–5 more agents at Deep/Full); see `modes.md`.

## 5. Smaller and larger variants

Build them from the recommended configuration:
- **Smaller:** drop one level, *or* keep the level and remove one round / one working group / one expert domain / two seats. Say what is lost in one line (e.g. "no verification of facts", "no rebuttal"). Never drop below two experts in a domain: drop the whole domain instead.
- **Larger:** add one level, *or* keep the level and add a round, a red-team room, a working group, an expert domain, a third (critical) expert in a contested domain, or a specialist seat. Say what is gained in one line.

Never offer a variant that breaks an override (e.g. no "Quick" when fresh facts are needed) unless you flag the trade-off explicitly.
