# Presenting the configuration

The proposal is the only gate before agents are spawned. Keep it short enough to read on a phone.

## Message before the question

```
**Question as I understand it:** <one neutral sentence>

**Difficulty:** <score>/14 → <Level>
- Stakes 2 — <reason>
- Fresh facts 2 — <reason>
- Contestedness 2 — <reason>
- … (only factors scored ≥ 1)
- Subject-specific: <factor> — <reason and effect>

<optional: one or two clarifying questions that change the configuration>
```

## The choice (AskUserQuestion)

One question, header "Council", four options at most (the tool adds "Other" automatically):

1. **`<Level> (Recommended)`** — description: one line on what it does and its cost (≈ agents, ≈ minutes).
2. **`Smaller: <Level or variant>`** — description: what it gives up.
3. **`Larger: <Level or variant>`** — description: what it adds.

Put the exact configuration in each option's `preview`:

```
Research   3 working groups (researcher → verifier)
           WG1 events · WG2 calendar · WG3 law & risk
Seats      7: Contrarian, First Principles, Expansionist,
           Outsider, Executor, Status-quo, Context Realist
Debate     openings → 2 rounds × 2 rooms (4 of 7, random)
Fact desk  between rounds
Audit      internal audit → revision
Outputs    report · process map · transcript
Cost       ≈ 25 agents · ≈ 20 min
```

If `AskUserQuestion` is not available, print the three options as a numbered list with the same content and ask the user to reply with a number or their own configuration.

## After the answer

- Recommended / Smaller / Larger → restate the final configuration in one line and start.
- "Other" → interpret, restate the resulting configuration, and ask for a one-word confirmation only if it changes cost by more than ~50%.
- Clarifying answers → apply them to the charter (reader profile, location, constraints).
