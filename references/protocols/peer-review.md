# Protocol: anonymous peer review (Quick, Standard)

Karpathy's key step: reviewers judge the responses without knowing who wrote them.

1. Shuffle the seats to letters A, B, C… (random mapping; record it).
2. Write the review prompt to `<run>/review-prompt.md` (the responses can be long; agents read the file).
3. Spawn **one** reviewer at Quick, **one or two** at Standard. If you use two, give the second a different lens (e.g. "review as a fact-checker" vs "review as the person who has to act"), so they don't duplicate each other.

```
You are reviewing the outputs of a council. These advisors answered this question:
---
<framed question>
---
<Response A> … <Response E>
(If rebuttals are included, ignore the role names they use and judge on merit.)

1. Which response is strongest, and why?
2. Which has the biggest blind spot, and what is it missing?
3. What did ALL responses miss?
<Standard: you may run up to 2 web searches to check a disputed fact.>
Under 200 words. Be direct.
```

Known limitation: seat voices are recognisable, so anonymity is partial. The review still adds value through question 3 ("what did all of them miss?"), which is where most blind spots surfaced in testing.
