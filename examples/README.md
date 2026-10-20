# Examples

## `quick-meta-test/` — the original skill reviewing itself

**Question:** "Should I use the llm-council skill as-is, fork and fix it, or skip it?"

Run with the original process: 5 advisors → 5 anonymous peer reviewers → chairman. `transcript.md` holds the advisors, the reviews and the verdict.

What it taught us: all five reviewers chose the same "strongest" and "weakest" response. Identical reviewers without a persona add cost, not signal. The Quick level now uses one reviewer.

## `protest-2026/` — a Full-level run on a contested question

**Question:** "Should I personally take part in the current French protest movement?" (20 October 2026). The person asked the council to weigh all sources, independent and official, and said explicitly that this was not a political statement.

- [`report.html`](protest-2026/report.html): the final verdict (v3, revised after an external review), with every working file collapsed underneath.
- [`process-map.html`](protest-2026/process-map.html): the visual map of the debate.
- [`transcript.md`](protest-2026/transcript.md): everything, in order.
- [`run/`](protest-2026/run/): the raw run folder: charter, working-group drafts and verified reports, 7 openings, 6 rooms, 5 fact desks, the internal audit, every verdict version, and `run.json`.

Notes:
- **Not included:** the earlier council's files and the two external reviews, which were the user's own documents. The charter and some research files still mention them by name (`prior-*.md`). Their lessons are now in `references/quality-charter.md`.
- **Method:** research relied on search-engine summaries; no web page could be opened in that environment. The v3 verdict therefore uses CORROBORATED as its top grade.
- **Facts are as of 20 October 2026.** This example shows the method. It is not current information about any event.
- **Room draw:** the run predates the `--balance` option of `draw_rooms.py`. One seat sat in all six rooms and another in only one.
