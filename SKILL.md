---
name: council
description: "Run a question, decision or design task through an adaptive council of AI advisors and neutral expert panels that debate it, check facts (never on a single source), review each other, and produce a graded report, or an improved artifact in design mode. The size of the process (seats, working groups, rooms, rounds, fact checks) scales with how hard the question is, and a configuration is always proposed to the user before anything runs. Based on Karpathy's LLM Council. TRIGGERS: 'council this', 'run the council', 'convene the council', 'war room this', 'pressure-test this', 'stress-test this', 'debate this'. Do NOT trigger on ordinary 'should I', 'which option' or 'what would you do' questions unless the user asks for the council: a run spawns several to dozens of sub-agents."
---

# Council

One AI gives you one answer. A council gives you several independent perspectives, makes them argue, checks the facts they rely on, and hands you a decision document that says what is established, what is contested, and what you should do first.

This skill extends the original LLM Council skill (5 advisors → anonymous peer review → chairman) with five ideas:

1. **The process scales with the question.** A low-stakes choice gets a 2-minute, 7-agent council. A contested, high-stakes, fact-heavy question gets working groups, rooms, a fact desk between rounds and an internal audit.
2. **The user always chooses the configuration.** Before anything runs, the skill proposes a recommended setup, a smaller and a larger variant, and lets the user describe something else.
3. **Four modes, not just debate.** *Decide* (choose), *Design / Build* (create a method, plan or spec over successive versions), *Evaluate* (critique something that exists), *Explore* (map the positions). See `references/modes.md`.
4. **Neutral expert panels.** Experts inform, never recommend. There are at least two per domain, each with a different source base, and no claim may rest on a single source. See `references/experts.md`.
5. **Quality rules are binding.** Neutrality on contested causes, an honest case for the status quo, grades that match what was actually checked, the two-source rule, no self-awarded authority. See `references/quality-charter.md`.

All paths below are relative to this skill's base directory.

---

## The four steps

### Step 1 — Triage (silent, ~30 seconds)

1. **Scan for context** the way the original skill did: `CLAUDE.md`, any `memory/` folder, files the user referenced, previous council runs (`runs/` or `council-*` files) on the same topic. Keep it to the 2–3 files that matter.
2. **Detect the reader's language.** The report is written in the language of the question unless the user asks otherwise.
3. **Detect the mode**: Decide, Design / Build, Evaluate or Explore (`references/modes.md`).
4. **Rate the question** on the standard difficulty factors in `references/levels.md` (stakes, reversibility, need for fresh facts, contestedness, number of strands, personal or legal risk, time pressure).
5. **Add subject-specific factors.** Think about the subject itself: is there something these factors don't capture? (e.g. "medical safety", "regulatory deadline", "involves minors", "depends on a vote whose result isn't known yet"). Add each with a one-line reason. These factors can raise the level, add a working group, add an expert domain, or add a specialist seat.
6. **List the knowledge domains** the answer depends on, and pick the 1–4 that would change it if they were wrong. These become the expert panels (`references/experts.md`).
7. **Map the level** from the score (table in `references/levels.md`) and draft the configuration: mode, seats (from `references/seats.md`), working groups, expert domains and their source bases, rooms, rounds, fact desk, audit, outputs, and an estimate of agents and duration. In Design mode, also draft the acceptance criteria.

If the question is too vague to triage, ask **one** clarifying question first, then triage.

### Step 2 — Propose the configuration and WAIT

Never start a council without the user's choice. Present:

- the question as you understood it (one neutral sentence) and the **mode**;
- the difficulty factors you detected, including any subject-specific ones, in a compact list;
- the **expert domains** and their source bases (if the level has experts);
- in Design mode, the draft **acceptance criteria** (the user can edit them);
- **three options**, using the `AskUserQuestion` tool when available:
  - **Recommended** — the level the triage mapped to, with its exact configuration;
  - **Smaller** — one level down (or the same level with fewer rounds/seats), and what it gives up;
  - **Larger** — one level up (or the same level with more rounds, a red-team room, extra working group), and what it adds;
  - the user can always pick "Other" to describe their own configuration.
- for each option: seats, working groups, expert domains × experts, rooms × rounds, fact desk on/off, audit on/off, approximate agent count and duration. Use the option `preview` field to show the configuration as a small block.
- at most one or two clarifying questions that would change the configuration (e.g. "Which city?", "Is this for you or for your team?").

Format template: `references/configuration-proposal.md`.

If the user says "just run it", use the recommended option. If they modify it, restate the final configuration in one line and start.

### Step 3 — Run the chosen process

Create a run folder in the user's workspace: `council-runs/<slug>-<YYYYMMDD>/`. Every agent writes its output there, so the run can be audited, resumed or compared later. Write `charter.md` first (question, mode, reader profile, quality rules, seats); every agent reads it. If there are experts, write `experts.md`. In Design mode, write `criteria.md`.

Run the phases of the chosen level and mode. Each phase has a protocol file with the prompt template:

| Phase | Protocol | Used at |
|---|---|---|
| Research brief | `references/protocols/working-group.md` (single researcher variant) | Standard |
| Working groups (researcher → adversarial verifier) | `references/protocols/working-group.md` | Deep, Full |
| Expert hearings (2–3 experts per domain, in parallel) | `references/protocols/expert-hearing.md` | Standard (1 domain), Deep, Full |
| Opening positions | `references/protocols/opening.md` | all levels |
| Architect draft → revisions (Design mode) | `references/protocols/design-room.md` | Design / Build |
| Rebuttal round | `references/protocols/rebuttal.md` | Standard |
| Rooms (random subsets of seats) | `references/protocols/room.md` (Decide, Evaluate, Explore) or `design-room.md` (Design) + `scripts/draw_rooms.py` | Deep, Full |
| Fact desk | `references/protocols/fact-desk.md` | Deep, Full (and Standard if members ask) |
| Anonymous peer review | `references/protocols/peer-review.md` | Quick, Standard |
| Chairman synthesis | `references/protocols/chairman.md` | all levels |
| Internal quality audit → revision (Design: acceptance check) | `references/protocols/audit.md` | Standard (light), Deep, Full |

Orchestration rules:

- **Spawn independent agents in parallel** (all openings at once, both rooms of a round at once, all working-group researchers at once). Never let one opening see another.
- **Anonymize before review.** Shuffle seats to letters A, B, C… and keep the map for the transcript.
- **Fact desk between rounds.** Collect the rooms' "information requests", merge duplicates, answer them with web search, and grade every answer. Questions about the future are not guessed: they become dated decision rules ("check X on date Y; if Z then…").
- **Expert hearings on request.** Route the rooms' "expert requests" to the right domain's experts, all in parallel. Keep their answers separate, and show disagreement rather than resolving it.
- **Two-source rule.** No claim rests on one source. A single-source claim is ALLEGED and cannot by itself justify a recommendation, a required change or a risk rating.
- **Closed loop.** If a room raises a reframe flag (the question or the facts are fundamentally wrong), go back to Step 1 once, tell the user, and re-propose if the configuration changes.
- **Later facts override earlier ones**, but every change of grade is recorded (it feeds the "how the facts moved" panel of the process map).
- **Don't let any agent write the user's opinion for them.** On contested causes, advice is conditional on the user's own goals.
- **Keep the user posted** in one short line per phase.

### Step 4 — Deliver

1. Write the final verdict as markdown in the run folder (`verdict.md`), following `references/report-spec.md` for the chosen level and mode. In Design mode, the deliverable is the final `design-vN.md`; `verdict.md` then presents it: summary, acceptance check, rationale, open issues.
2. Build the HTML report: `python3 scripts/build_report.py --run <run-folder> --out council-report-<slug>-<date>.html`.
3. For Deep and Full runs, write `run.json` (schema in `references/run-json.md`) and build the process map: `python3 scripts/build_process_map.py --run <run-folder> --out council-process-<slug>-<date>.html`.
4. Assemble the transcript: `python3 scripts/build_report.py --run <run-folder> --transcript council-transcript-<slug>-<date>.md`.
5. Show the report to the user: open it on a desktop, or send it as a file in cloud and mobile sessions. Summarize the verdict in chat in a few lines, and list the files.
6. Offer the next step: an external review of the report, a revision pass (`verdict-v2.md`), or a re-run when facts change.

---

## When not to convene a council

- Questions with one right answer, pure creation tasks, summaries: just answer.
- A user who wants validation, not challenge: say what the council would do and let them choose.
- If the user explicitly declines the proposal, don't run a smaller council anyway.

## Files in this skill

- `references/levels.md` — difficulty factors, scoring, the four levels and their default configurations
- `references/modes.md` — Decide, Design / Build, Evaluate, Explore
- `references/experts.md` — expert panels, source bases, the two-source rule
- `references/configuration-proposal.md` — how to present the three options
- `references/seats.md` — the seat library (core, status-quo, context and specialist seats) and selection rules
- `references/quality-charter.md` — binding quality rules, grading scale, source tagging
- `references/report-spec.md` — report sections by level
- `references/run-json.md` — schema for the process map
- `references/protocols/*.md` — prompt templates for each phase
- `scripts/draw_rooms.py` — reproducible, balanced random room draw
- `scripts/build_report.py` — markdown verdict → HTML report (mobile-friendly tables) and transcript
- `scripts/build_process_map.py` — `run.json` → visual process map
- `templates/report.html`, `templates/process-map.html` — page templates
- `examples/` — worked examples

Methodology by Andrej Karpathy. Original Claude Code skill by @tenfoldmarc, inspired by @olelehmann. Extended into an adaptive council by @cleman.
