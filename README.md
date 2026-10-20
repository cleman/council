# Council — an adaptive LLM council skill for Claude Code

Put a question or decision in front of a council of AI advisors. They research it, argue, check each other's facts, and hand you a decision report that says what is established, what is contested, and what to do first.

The council **scales with the question**, and it **always asks before it starts**. A low-stakes choice gets a 2-minute council of 7 agents. A contested, high-stakes, fact-heavy question gets working groups, debate rooms, a fact desk between rounds and an internal audit. You choose between a recommended setup, a smaller one and a larger one, or describe your own.

Built on [tenfoldmarc/llm-council-skill](https://github.com/tenfoldmarc/llm-council-skill), which adapted [Andrej Karpathy's LLM Council](https://x.com/karpathy/status/1962263486196867115) to Claude Code sub-agents.

---

## What's new compared with the original

| | Original `llm-council` | `council` |
|---|---|---|
| Process size | Fixed: 5 advisors, 5 peer reviewers, 1 chairman | **Four levels** (Quick, Standard, Deep, Full), chosen by triage |
| Before running | Starts immediately | **Proposes a configuration** (recommended + smaller + larger + "other") and waits |
| Triage | — | Standard difficulty factors **plus factors specific to the subject** |
| Research | None | Researchers, and at Deep/Full **working groups** with an **adversarial verifier** |
| Debate | One round, then anonymous review | Rebuttal round (Standard); **rooms** of randomly drawn seats over several rounds (Deep/Full) |
| Facts | Not checked | **Fact desk** between rounds; graded claims; dated rules for what can't be known yet |
| Seats | 5 fixed | 5 core + **Status-quo advocate**, **Context Realist** and specialists chosen per question |
| Peer review | 5 identical reviewers | 1–2 reviewers (5 identical ones gave identical reviews in testing) |
| Quality | — | A **binding quality charter**: neutrality on contested causes, an honest case for not acting, grades that match the method, symmetric source tagging, no self-awarded authority |
| Loop | — | **Reframe loop**: a room can send the council back to triage |
| Output | HTML + transcript | Report (mobile-friendly, 60-second version, glossary), **visual process map**, transcript, run folder |
| Triggers | Broad ("which option", "validate this"…) | Explicit only ("council this"…), since a run spawns many agents |

## Install

```bash
git clone https://github.com/cleman/council ~/.claude/skills/council
```

Then start Claude Code (`claude`). The skill appears as `council`.

Optional: Python 3 (standard library only) for the report and process-map builders in `scripts/`.

## Use

```
council this: <your question, with as much context as you can give>
```

Other triggers: `run the council`, `convene the council`, `war room this`, `pressure-test this`, `stress-test this`, `debate this`.

What happens:

1. **Triage.** The question is rated on stakes, reversibility, need for fresh facts, contestedness, number of strands, personal or legal risk and time pressure, plus anything the subject itself calls for.
2. **Proposal.** You get the recommended configuration and a smaller and a larger variant, each with its seats, research, rounds, fact desk, audit and approximate cost. Pick one or describe another.
3. **Run.** Agents work in parallel, writing to a run folder you can inspect.
4. **Report.** A decision report, a process map (Deep/Full) and a full transcript.

## The four levels

| Level | Typical question | Process | ≈ Agents | ≈ Time |
|---|---|---|---|---|
| **Quick** | "Workshop at $97 or course at $497?" | 5 seats → 1 anonymous reviewer → chairman | 7 | 2–4 min |
| **Standard** | A real decision with some facts to check | brief research → 5–6 seats → rebuttal → 1–2 reviewers → chairman + self-check | 12–15 | 6–10 min |
| **Deep** | High stakes, contested, needs current facts | 3 working groups (researcher → verifier) → 7 seats → 2 rounds × 2 rooms → fact desk → chairman → internal audit → revision | 22–28 | 15–25 min |
| **Full** | Big, divided questions with personal risk | Deep + 3 rounds, red-team room, reframe loop, offer of external review | 30–40 | 25–45 min |

Details: [`references/levels.md`](references/levels.md).

## Outputs

```
council-report-<slug>-<date>.html      decision report (60-second version → full analysis → glossary)
council-process-<slug>-<date>.html     visual map of the debate (Deep, Full)
council-transcript-<slug>-<date>.md    everything, in order
council-runs/<slug>-<date>/            working files: charter, research, openings, rooms,
                                       fact desks, audit, verdict versions, run.json
```

See [`examples/protest-2026/`](examples/protest-2026/) for a complete Full-level run: [report](examples/protest-2026/report.html) · [process map](examples/protest-2026/process-map.html) · [transcript](examples/protest-2026/transcript.md).

## Repository layout

```
SKILL.md                          the orchestrator Claude follows
references/
  levels.md                       difficulty factors, scoring, levels, variants
  configuration-proposal.md       how the three options are presented
  seats.md                        seat library and selection rules
  quality-charter.md              binding quality rules and grading scale
  report-spec.md                  report sections by level
  run-charter-template.md         the per-run charter every agent reads
  run-json.md                     data schema for the process map
  protocols/                      prompt templates: working group, opening, rebuttal,
                                  room, fact desk, peer review, chairman, audit
scripts/
  draw_rooms.py                   reproducible, balanced random room draw
  build_report.py                 verdict markdown → HTML report (+ transcript)
  build_process_map.py            run.json → process map
templates/                        report.html, process-map.html
examples/                         worked examples
```

## Where this came from

This version grew out of three runs on the same afternoon:

1. **The original skill reviewing itself** (Quick-like). It showed that five persona-less reviewers return the same review five times. See [`examples/quick-meta-test/`](examples/quick-meta-test/).
2. **Council 1** on a contested, fast-moving political question (5 advisors + research + rebuttal). An external review scored it 7.5/10. It found a "neutral" first step that took sides, no real case for abstaining, factual conflicts settled too fast, and jargon.
3. **Council 2** on the same question, with working groups, 7 seats, rooms, a fact desk and an audit. An external review scored it 8/10. It found grades stronger than the method allowed, the government's case not shown, a missing "vote postponed" scenario, and a self-described "independent" audit. Those fixes are now rules in [`references/quality-charter.md`](references/quality-charter.md).

## Known limits

- All seats run on the same model family. This gives diversity of perspective, not of training. Karpathy's original used different providers.
- Seat voices are recognisable, so "anonymous" review is only partly blind.
- In environments where web pages can't be opened, research relies on search summaries. The quality charter caps grades accordingly.
- Large runs cost many sub-agent calls. That is why the skill asks first and doesn't trigger on casual phrasing.

## Credits

- Methodology: [Andrej Karpathy's LLM Council](https://x.com/karpathy/status/1962263486196867115)
- Claude Code adaptation: inspired by [@olelehmann](https://x.com/olelehmann)
- Original skill: [@tenfoldmarc](https://github.com/tenfoldmarc/llm-council-skill). The first commit of this repository is that skill, unchanged.
- Adaptive council, quality charter, rooms, fact desk, reports: [@cleman](https://github.com/cleman)

## License

MIT, see [LICENSE](LICENSE). The original repository states "MIT" in its README but ships no LICENSE file. This repository credits the original author in the copyright notice and keeps the original as its first commit.
