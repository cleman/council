# Report specification

The verdict is written as markdown (`verdict.md`) in the run folder, then rendered by `scripts/build_report.py`. The first line is a `# Title`. Use `##` for sections. Pipe tables are rendered as tables on desktop and as cards on phones; cells containing exactly `Go`, `Caution`, `Avoid` (or `Check …`) become coloured pills.

## Quick and Standard

```
# <Question, short>

<one line: method and grading note>

## The 60-second version          (3–5 bullets)
## Where the council agrees        (high-confidence points)
## Where the council clashes       (real disagreements, both sides, the crux)
## Blind spots the council caught  (from peer review / rebuttal)
## The recommendation              (a real answer, conditional only where it must be)
## The one thing to do first       (one step, neutral on contested causes)
## Limits                          (method, date, unknowns)
## Glossary                        (only if acronyms were used)
```

## Deep and Full

Use the sections that apply; drop the ones that don't. Order matters: the reader should be able to stop after section 2.

```
# <Question, short>

<grading note: method, grade definitions, source tagging>

## The 60-second version
## 1. Bottom line                       (≤120 words; conditional; neutral on the cause)
## 2. Your first step                   (neutral: define your goal; map it to the strands/options)
## 3. The case for not acting           (Status-quo seat's paragraph, accepted as fair)
## 4. The case for acting               (equally honest, graded)
## 5. Decision guide                    (table: goal/strand × scenario → action; include "postponed/unknown" scenarios)
## 6. Risk or fit by profile            (table: profile × option → Go / Caution / Avoid, notes in plain words)
## 7. Practical plan                    (one checklist; legal points; reconciled advice)
## 8. Rules for what can't be known today (dated: check X on date Y; if Z then…)
## 9. What the evidence says            (each side's case with its evidence, then a graded claims table with tagged sources)
## 10. Where the council disagreed      (open disagreements and their crux)
## 11. Limits of this report
## 12. Glossary
```

## Process box

The report template shows a short "How this council worked" box above the verdict. `build_report.py` fills it from `run.json` if present (fields `level`, `process`), otherwise from the `--process` argument.

## File names (user's workspace)

```
council-report-<slug>-<YYYYMMDD>.html
council-process-<slug>-<YYYYMMDD>.html     (Deep, Full)
council-transcript-<slug>-<YYYYMMDD>.md
council-runs/<slug>-<YYYYMMDD>/            (all working files)
```

Revisions after review: `verdict-v2.md` → `council-report-<slug>-<date>-v2.html`. Keep earlier versions.
