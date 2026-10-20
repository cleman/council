# Changelog

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
