#!/usr/bin/env python3
"""Build a council report (HTML) and/or transcript (markdown) from a run folder.

  python3 build_report.py --run council-runs/<slug>-<date> --out council-report-<slug>-<date>.html
  python3 build_report.py --run council-runs/<slug>-<date> --transcript council-transcript-<slug>-<date>.md

The verdict is the newest of verdict-vN.md, verdict.md, verdict-draft.md (or --verdict).
Working files found in the run folder are appended, collapsed, under "Behind the verdict".
Standard library only.
"""
import argparse
import datetime
import html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "templates" / "report.html"

RATING = {"go": "ok", "caution": "warn", "avoid": "bad"}

# (heading, glob patterns) in display order; prompts and the verdict itself are excluded
GROUPS = [
    ("Charter & room draw", ["charter.md", "rooms.txt"]),
    ("Research", ["brief*.md", "wg[0-9].md", "wg[0-9]-draft.md"]),
    ("Opening positions", ["opening-*.md", "advisor-*.md"]),
    ("Rebuttals", ["rebuttal-*.md"]),
    ("Rooms", ["r[0-9]-room*.md"]),
    ("Fact desks", ["factdesk*.md"]),
    ("Peer reviews", ["review-[0-9]*.md"]),
    ("Internal audit (same process, not independent)", ["audit*.md"]),
    ("Earlier drafts and versions", ["verdict-draft.md", "verdict.md", "verdict-v*.md"]),
]

LABELS = {
    "en": {"behind": "Behind the verdict", "behind_sub": "The working files of this run, collapsed by default.",
           "how": "How this council worked", "generated": "Generated", "level": "Level",
           "footer": "Produced with the council skill. Facts as of {date}. Not legal, medical or financial advice."},
    "fr": {"behind": "Coulisses du verdict", "behind_sub": "Les fichiers de travail de cette session, repliés par défaut.",
           "how": "Comment ce conseil a travaillé", "generated": "Généré le", "level": "Niveau",
           "footer": "Produit avec la skill council. Faits arrêtés au {date}. Ne constitue pas un avis juridique, médical ou financier."},
}


# ---------------------------------------------------------------- markdown → html
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    s = re.sub(r"(?<![\"'>=])(https?://[^\s<)\]]+)", r'<a href="\1" target="_blank" rel="noopener">link</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def cell(c, header, label=""):
    c = c.strip()
    tag = "th" if header else "td"
    dl = f' data-label="{html.escape(label)}"' if label and not header else ""
    key = re.sub(r"\s*\(\d+\)$", "", c).lower()
    cls = RATING.get(key) or ("warn" if key.startswith("check ") else None)
    if not header and cls:
        return f'<{tag}{dl}><span class="pill {cls}">{inline(c)}</span></{tag}>'
    return f"<{tag}{dl}>{inline(c)}</{tag}>"


def md(text):
    out, para, items, kind, table, quote = [], [], [], None, [], []

    def close_para():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    def close_list():
        nonlocal items, kind
        if kind:
            out.append(f"<{kind}>" + "".join(items) + f"</{kind}>")
            items, kind = [], None

    def close_table():
        nonlocal table
        if table:
            heads = [h.strip() for h in table[0].strip().strip("|").split("|")]
            rows = []
            for i, r in enumerate(table):
                cells = r.strip().strip("|").split("|")
                rows.append("<tr>" + "".join(cell(c, i == 0, heads[j] if j < len(heads) else "") for j, c in enumerate(cells)) + "</tr>")
            out.append('<div class="wrap"><table class="rt">' + "".join(rows) + "</table></div>")
            table = []

    def close_quote():
        nonlocal quote
        if quote:
            out.append("<blockquote>" + inline(" ".join(quote)) + "</blockquote>")
            quote = []

    def close_all():
        close_para(); close_list(); close_table(); close_quote()

    in_code = False
    code = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("```"):
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
                code, in_code = [], False
            else:
                close_all(); in_code = True
            continue
        if in_code:
            code.append(line); continue
        if not s:
            close_all(); continue
        if s.startswith("|"):
            close_para(); close_list(); close_quote()
            if not re.fullmatch(r"\|[\s:|-]+\|?", s):
                table.append(s)
            continue
        close_table()
        if s.startswith(">"):
            close_para(); close_list()
            quote.append(s.lstrip("> ").strip()); continue
        close_quote()
        m = re.match(r"^(#{1,5})\s+(.*)", s)
        if m:
            close_all()
            lvl = min(max(len(m.group(1)), 2), 5)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); continue
        m = re.match(r"^(?:[-*]\s+(?:\[[ x]\]\s+)?|(\d+)\.\s+)(.*)", s)
        if m:
            close_para()
            k = "ol" if m.group(1) else "ul"
            if kind != k:
                close_list(); kind = k
            items.append("<li>" + inline(m.group(2)) + "</li>"); continue
        if kind and line.startswith("  "):
            items[-1] = items[-1][:-5] + " " + inline(s) + "</li>"; continue
        close_list()
        para.append(s)
    close_all()
    return "\n".join(out)


# ---------------------------------------------------------------- run folder helpers
def pick_verdict(run, explicit):
    if explicit:
        return pathlib.Path(explicit)
    versions = sorted(run.glob("verdict-v*.md"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0))
    for p in [*reversed(versions), run / "verdict.md", run / "verdict-draft.md"]:
        if p.exists():
            return p
    raise SystemExit(f"no verdict found in {run}")


def grouped_files(run, verdict):
    seen = {verdict.resolve()}
    for heading, patterns in GROUPS:
        files = []
        for pat in patterns:
            for p in sorted(run.glob(pat)):
                if p.resolve() not in seen and "prompt" not in p.name:
                    files.append(p)
                    seen.add(p.resolve())
        if files:
            yield heading, files


def load_run_json(run):
    p = run / "run.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"warning: run.json ignored ({e})")
    return {}


# ---------------------------------------------------------------- outputs
def build_html(run, verdict_path, out, lang, process_lines, level):
    L = LABELS.get(lang, LABELS["en"])
    text = verdict_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = "Council report"
    if lines and lines[0].startswith("# "):
        title, text = lines[0][2:].strip(), "\n".join(lines[1:])

    process_box = ""
    if process_lines:
        lis = "".join(f"<li>{inline(x)}</li>" for x in process_lines)
        head = L["how"] + (f" · {L['level']}: {html.escape(level)}" if level else "")
        process_box = f'<div class="process"><strong>{head}</strong><ol>{lis}</ol></div>'

    work = []
    for heading, files in grouped_files(run, verdict_path):
        work.append(f"<h3>{html.escape(heading)}</h3>")
        for f in files:
            body = md(f.read_text(encoding="utf-8")) if f.suffix == ".md" else f"<pre>{html.escape(f.read_text(encoding='utf-8'))}</pre>"
            work.append(f"<details><summary>{html.escape(f.name)}</summary><div>{body}</div></details>")
    working = f"<h2>{L['behind']}</h2><p class=\"muted\">{L['behind_sub']}</p>" + "\n".join(work) if work else ""

    today = datetime.date.today().isoformat()
    page = TEMPLATE.read_text(encoding="utf-8")
    for k, v in {
        "{{LANG}}": lang,
        "{{TITLE}}": html.escape(title),
        "{{SUBTITLE}}": html.escape(f"{L['generated']} {today}" + (f" · {L['level']}: {level}" if level else "")),
        "{{PROCESS_BOX}}": process_box,
        "{{VERDICT}}": md(text),
        "{{WORKING_FILES}}": working,
        "{{FOOTER}}": html.escape(L["footer"].format(date=today)),
    }.items():
        page = page.replace(k, v)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out}")


def build_transcript(run, verdict_path, out):
    parts = [f"# Council transcript — {run.name}", ""]
    for heading, files in grouped_files(run, verdict_path):
        parts += [f"## {heading}", ""]
        for f in files:
            parts += [f"### {f.name}", "", f.read_text(encoding="utf-8").strip(), ""]
    parts += ["## Final verdict", "", verdict_path.read_text(encoding="utf-8").strip(), ""]
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {out}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--run", required=True, help="run folder")
    p.add_argument("--out", help="HTML report path")
    p.add_argument("--transcript", help="markdown transcript path")
    p.add_argument("--verdict", help="verdict markdown (default: newest verdict in the run folder)")
    p.add_argument("--lang", help="report language code (default: run.json 'lang' or en)")
    p.add_argument("--process", action="append", default=[], help="a line for the 'How this council worked' box (repeatable)")
    a = p.parse_args()

    run = pathlib.Path(a.run)
    meta = load_run_json(run)
    verdict = pick_verdict(run, a.verdict)
    lang = a.lang or meta.get("lang", "en")
    if not (a.out or a.transcript):
        p.error("give --out and/or --transcript")
    if a.out:
        build_html(run, verdict, pathlib.Path(a.out), lang, a.process or meta.get("process", []), meta.get("level", ""))
    if a.transcript:
        build_transcript(run, verdict, pathlib.Path(a.transcript))


if __name__ == "__main__":
    main()
