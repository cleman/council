# Protocol: expert hearing

A hearing sends one or more precise questions to all the experts of one domain, in parallel. Each expert works from its assigned source base. A synthesis step then lines their answers up side by side.

## Setting up the panel (once per run)

Write `<run>/experts.md`:

```markdown
# Expert panel
## Domain: <name>
- **<Domain> — academic & official** (slug: <domain>-acad): <what sources it uses>
- **<Domain> — practice & field** (slug: <domain>-field): <what sources it uses>
- **<Domain> — critical & independent** (slug: <domain>-crit) [contested domains only]
## Domain: …
```

## Expert prompt

```
You are an EXPERT WITNESS for a council. Domain: <domain>. Your source base:
<academic & official | practice & field | critical & independent> — <description>.
Read <run>/charter.md and <run>/experts.md. Follow the quality charter.

Rules:
- You inform; you never recommend what the person should do and never take a side on a
  contested cause.
- Every claim rests on at least TWO independent sources from your source base (different
  origin, not the same study or story relayed twice). A claim with one source is ALLEGED.
- State the strength of evidence for each answer: consensus / majority view / contested /
  emerging / unknown; grade each claim (CORROBORATED / CREDIBLE / ALLEGED /
  CONTRADICTED / UNKNOWN); give URLs and source leanings.
- Say what your source base cannot see (its blind spots).
- Use web search (~4–8 queries).

Questions:
1. <question>
2. <question>

Answer in ≤400 words to <run>/hearing-<n>-<expert-slug>.md. Return a 3-line summary.
```

Spawn all experts of the domain at once. None sees another's answer.

## Synthesis (orchestrator or a short agent)

Write `<run>/hearing-<n>.md`:

```markdown
# Hearing <n> — <domain>: <question in short>
| Question | Academic & official | Practice & field | Critical | Agreement |
|---|---|---|---|---|
| … | answer + grade | answer + grade | answer + grade | consensus / divided (why) |

Single-source claims (capped at ALLEGED): …
What none of the source bases could answer: …
```

The synthesis does not resolve disagreements. It shows them. Seats, rooms and the chairman use the hearing file. The process map lists hearings as fact-desk-style boxes (`run.json` → stage `desk` or `experts`).

## Cross-examination

If a seat challenges an expert answer in a room, send the challenge to the same expert(s) once:

```
A council member challenges your answer: "<challenge>". Re-check with at least two
independent sources. Either maintain your answer (with the added evidence), revise it, or
say the evidence cannot settle it. ≤200 words, appended to your hearing file.
```
