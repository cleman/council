# `run.json` — data for the process map

At the end of a Deep or Full run, write `<run>/run.json`. `scripts/build_process_map.py` turns it into the visual process map, and `scripts/build_report.py` uses `level` and `process` for the report's "How this council worked" box.

All text fields are plain text (no HTML). Seat ids are short slugs reused everywhere.

```json
{
  "title": "How the council reached its verdict",
  "question": "Should I personally take part in the protests of autumn 2026?",
  "date": "2026-10-20",
  "lang": "en",
  "level": "Full",
  "process": [
    "Working groups: 3, each a researcher then an adversarial verifier.",
    "Seven seats wrote independent opening positions.",
    "Three rounds of two rooms, 4 of 7 seats drawn at random.",
    "Fact desk between rounds; reframe loop available (not used).",
    "Chairman draft → internal audit → revision."
  ],
  "stats": [
    {"value": "26", "label": "agent runs"},
    {"value": "0", "label": "reframe flags raised"}
  ],
  "seats": [
    {"id": "con", "name": "Contrarian", "color": "#e03131"},
    {"id": "abs", "name": "Abstainer", "color": "#495057", "new": true}
  ],
  "stages": [
    {
      "title": "Working groups",
      "subtitle": "a researcher, then an adversarial verifier",
      "cards": [
        {"title": "WG1 · Events & policing", "pipe": ["research", "verify"],
         "text": "Violence started around midday at assembly points."}
      ],
      "note": "",
      "desk": null
    },
    {
      "title": "Round 1",
      "subtitle": "leverage & risk",
      "cards": [
        {"title": "Room A · Is there a leverage window?", "members": ["exp", "fp", "lr", "out"],
         "text": "Leverage differs by strand.", "flag": "reframe? NO"}
      ],
      "desk": {"title": "Fact desk 3", "items": ["2,397 arrests confirmed as the latest count"]}
    }
  ],
  "loop": {"used": false, "text": "Any room could send the council back to triage. None did."},
  "final": {
    "title": "Chairman → audit → revision",
    "cards": [
      {"title": "Chairman's draft", "text": "12 sections, written by a separate agent."},
      {"title": "Internal quality audit", "text": "11 required fixes."}
    ],
    "verdict": "It depends on your demand and your risk profile. Staying home is legitimate.",
    "first_step": "Write: I want [outcome] from [decision-maker] by [date]."
  },
  "rooms": [
    {"label": "R1 · A", "members": ["exp", "fp", "lr", "out"]},
    {"label": "R1 · B", "members": ["abs", "con", "lr", "out"]}
  ],
  "rooms_note": "Each room drew 4 of the 7 seats at random (seed 20261020).",
  "facts": [
    {"claim": "2,397 arrests on 17 Oct",
     "trail": [
       {"grade": "CORROBORATED", "who": "WG1"},
       {"grade": "CONTRADICTED", "who": "Fact desk 2"},
       {"grade": "CORROBORATED", "who": "Fact desk 3: latest provisional count"}
     ]}
  ],
  "convergence": {
    "converged": ["Four strands, not one movement"],
    "settled": ["Non-EU temporary card at a union march: Avoid"],
    "open": ["Abstainer vs Context Realist: stay home or decide by city and hour?"]
  }
}
```

Grades accepted in `facts.trail[].grade`: `VERIFIED`, `CORROBORATED`, `CREDIBLE`, `ALLEGED`, `CONTRADICTED`, `UNKNOWN`, and free labels such as `NOT FOUND`, `OPEN`, `FLAGGED` (shown in grey).

Any section can be omitted; the map renders what is present.
