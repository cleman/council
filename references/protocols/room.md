# Protocol: rooms (Deep, Full)

A room is a debate between a random subset of seats (about 60%) on one focus question. Two rooms run in parallel per round, each on a different focus. Rooms replace the anonymous peer review at Deep and Full levels.

## Drawing the rooms

```
python3 scripts/draw_rooms.py --seats "Contrarian,First Principles,Expansionist,Outsider,Executor,Abstainer,Context Realist" \
    --rounds 3 --rooms 2 --size 4 --seed <YYYYMMDD> --balance
```

`--balance` re-draws until every seat sits in at least one room and no seat sits in more than (average + 2). Save the output to `<run>/rooms.txt`. Use the date as the seed so the draw is reproducible.

## Choosing each round's focus

A pattern that works:

| Round | Room A | Room B |
|---|---|---|
| 1 | Leverage / value: is there a real window or upside, per option? | Risk: how risky is each option, really, and when is not acting right? |
| 2 | Build the decision guide (goal × scenario → action) | Build the profile × option matrix (Go / Caution / Avoid) |
| 3 | Integrate into a draft recommendation + status-quo paragraph + dated rules | Red team: settle contested cells, list what would flip the advice, check against the charter |

Fewer rounds: merge rounds 2 and 3.

## Room prompt

Write once to `<run>/room-prompt.md`:

```
You are the MODERATOR and SCRIBE of a council room. Read <run>/charter.md (binding),
the research files, every fact-desk and hearing file present (later ones override earlier
ones; expert disagreements stay visible),
and the opening position of each member in your room. Also read the previous room
outputs listed below.

Run a genuine debate among ONLY your room's members, voicing each faithfully to their
seat and opening position. Members change their minds only when an argument or fact
warrants it — say why. 2–3 exchanges. Prioritise the round's focus question. Members must
cite grades; nobody may treat a CONTRADICTED or UNKNOWN fact as established. Watch for
breaches of the charter (neutrality, honest status-quo case, categories, risk
completeness).

Output file (≤800 words):
## Debate (condensed, speaker-labelled)
## Agreements
## Live disagreements (who vs who, and the crux)
## Information requests (max 3, precise; or "none")   → fact desk
## Expert requests (max 3, precise, with the domain; or "none")   → expert hearing
## Reframe flag (YES/NO — YES only if the question or the research is fundamentally
   wrong and triage must be redone; explain)

Save to the output path and return the last five sections.
```

Each room call adds: room id, members, previous room outputs, round focus, output path (`<run>/r<round>-room<A|B>.md`).

## Reframe loop

If any room returns `Reframe flag: YES`, stop, tell the user why, go back to triage once with the new understanding, and re-propose the configuration if it changes. In testing, rooms raised no false alarms: six rooms over three rounds all judged that the facts refined the question rather than overturning it.
