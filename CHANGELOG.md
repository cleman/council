# Changelog

## 1.1.0 — 2026-10-20

### Added
- **Expert panels** (`references/experts.md`, `protocols/expert-hearing.md`): neutral experts who inform and never recommend. At least two per domain, each on a different source base (academic & official / practice & field / critical & independent). They are heard in parallel at the start and on request from rooms, and can be cross-examined. Disagreement between experts is reported, not averaged.
- **Two-source rule** in the quality charter: a claim with a single source is capped at ALLEGED and cannot by itself justify a recommendation, a required change or a risk rating.
- **Modes** (`references/modes.md`): Decide, Design / Build, Evaluate, Explore, detected at triage and shown in the proposal.
- **Design / Build mode**: acceptance criteria approved up front, an architect draft, design rooms that review modules against the criteria (`protocols/design-room.md`), versioned artifacts (`design-vN.md`) with a rationale, and a final acceptance check.
- Report formats for Design, Evaluate and Explore (`report-spec.md`).
- Process map: "Expert panel" and "Acceptance check" sections; report builder shows hearings, design versions and `Met / Partly / Not met` pills.

### Changed
- Rooms now return "Expert requests" separately from fact-desk "Information requests".
- Agent estimates per level include expert hearings.
- Smaller variants drop a whole expert domain rather than going below two experts in a domain.

## 1.0.0 — 2026-10-20

First release of `council`, derived from `llm-council` by @tenfoldmarc (commit 0dc0327).

### Added
- Triage on seven standard difficulty factors plus subject-specific factors.
- Four levels (Quick, Standard, Deep, Full) with default configurations and overrides.
- Mandatory configuration proposal: recommended, smaller and larger variants, plus "other".
- Working groups (researcher → adversarial verifier), rebuttal round, rooms with balanced random seat draws, fact desk between rounds, reframe loop.
- Seat library: Status-quo advocate (Abstainer), Context Realist, Stakeholder Voice, specialist seats.
- Binding quality charter (grading scale tied to method, symmetric source tagging, neutrality, honest status-quo case, dated decision rules, reader-first writing, no self-awarded authority).
- Protocol files with prompt templates for every phase.
- `scripts/build_report.py` (mobile-friendly report, transcript), `scripts/build_process_map.py`, `scripts/draw_rooms.py`.
- Worked examples: the original skill reviewing itself; a Full-level run on a contested political question.

### Changed
- Peer review uses 1–2 reviewers instead of 5 identical ones.
- Triggers are explicit only; the broad "strong triggers" were removed.
- Outputs are delivered as files in cloud and mobile sessions instead of assuming a desktop browser.
- The report is written in the language of the question by default.
