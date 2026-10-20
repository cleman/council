# Modes

The same machinery (research, varied perspectives, adversarial checking, synthesis) serves four kinds of work. Triage detects the mode. The configuration proposal shows it, and the user can change it.

| Mode | The user wants… | Example | Output |
|---|---|---|---|
| **Decide** | a choice between options, or yes/no | "Should I join the protest?" "Launch at $97 or $497?" | A verdict: decision guide, risks, first step |
| **Design / Build** | something created: a method, a plan, a product, a spec | "Create an adaptive modular running training method." "Design the website for it." | An artifact improved over rounds (v1 → v2 → v3), with acceptance criteria and a rationale |
| **Evaluate** | a critique of something that already exists | "Review my landing page." "Audit this training plan." | A graded assessment: strengths, weaknesses, required and optional fixes |
| **Explore** | understanding, not a decision | "What are the serious positions on X?" | A map of positions, evidence and open questions |

Detection hints: imperative verbs like *create, design, build, write a method/plan* → Design. A thing to judge (*review, audit, critique, what's weak*) → Evaluate. *Should, which, whether* → Decide. *What are, why, how does, positions on* → Explore. When unsure, put your best guess in the proposal and let the user correct it.

---

## Decide

Everything in `SKILL.md` and the protocols as written. Seats argue positions. Rooms debate leverage, risk, decision guide and profile matrix. Report: `report-spec.md` → Decide.

## Design / Build

### 0. Acceptance criteria first
Before any design work, write `<run>/criteria.md`: 8–15 **checkable** criteria that define "good" for this artifact. Derive them from the user's goal, the experts' opening hearing and the triage factors. Examples for a training method:
- every plan adapts when 1 or 2 sessions are missed;
- weekly load never rises more than the agreed limit without an explicit justification;
- each module states its prerequisites, goal, duration and exit test;
- every physiological claim is CORROBORATED or flagged.

"Perfect" is not a criterion. The user approves the criteria list in the configuration step, or right after it for Deep/Full.

### Seats become critics of the design

| Seat | In Design mode it asks… |
|---|---|
| Contrarian | How does this fail? Injury, drop-out, misuse, edge cases |
| First Principles | What is the artifact for? Which parts are essential? |
| Expansionist | What would make it remarkably better or more widely useful? |
| Outsider | Can a first-time user understand and use it unaided? |
| Executor | Can it actually be built, run and maintained? In what order? |
| Status-quo advocate | What do existing solutions already do well? What does this really add? |
| Context Realist | Does it hold across profiles, levels, places and constraints? |
| Specialists | Domain checks (e.g. physiotherapist, accessibility, data protection) |

### Process
1. **Working groups** map the field: the state of knowledge, existing solutions and their reviews, the users' needs.
2. **Opening expert hearing**: what the evidence says on each decisive question.
3. **Architecture draft** (`design-v1.md`): one agent (the "architect", no seat) writes the first version: structure, modules, rules, rationale. Every claim cites the hearings or working groups.
4. **Design rounds** (rooms): each room reviews **a module or a cross-cutting concern** against the criteria. Typical room focuses: structure & modularity, adaptation logic, safety & limits, user experience, evidence check. Rooms output *required changes* (with the criterion they serve), *optional improvements*, *expert requests* and a reframe flag.
5. **Revision**: the architect applies the required changes → `design-v2.md`. Repeat for the number of rounds the level allows.
6. **Acceptance check**: the auditor scores each criterion *met / partly / not met* with evidence. Unmet criteria go back for one more revision or are listed as open.

Room protocol variant: `protocols/design-room.md`.

### Outputs
- `design-vN.md`: the artifact (method, plan, spec…), the main deliverable.
- `rationale.md`: why each major choice was made, with the evidence and the alternatives rejected.
- `criteria.md` with the final acceptance check.
- Report: `report-spec.md` → Design.

**Building something large** (software, a website): use **two councils in sequence**. First the content or method, then the product spec. Then build with normal Claude Code work, convening a Quick or Standard council in Evaluate mode at each milestone.

## Evaluate

- **Working groups / experts** establish the reference: standards, best practice, comparable works.
- **Seats** review the existing thing from their angles. At Deep/Full, rooms each take one dimension.
- **Output:** strengths, weaknesses (graded), required fixes (precise: where, what, why), optional improvements, and an indicative score with its rubric. Never a score without a rubric.

## Explore

- **No verdict.** Seats represent the main serious positions on the question. Name them by position, not by thinking style, plus the Outsider and the Contrarian.
- **Experts** map the evidence for each position.
- **Output:** a map of positions: what each holds, its strongest evidence, its weakest point, where they really disagree (values vs facts), and the open questions that would settle it.

---

## Effect on levels

Modes don't change the level scale. Two adjustments apply:
- **Design / Build** at Deep/Full: replace "rounds × 2 debate rooms" with "rounds × 2–3 design rooms" and add the architect agent. Count about 3–5 extra agents.
- **Explore** rarely needs Full: suggest Standard or Deep unless the user asks for more.
