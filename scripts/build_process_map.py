#!/usr/bin/env python3
"""Build the visual process map of a council run from <run>/run.json.

  python3 build_process_map.py --run council-runs/<slug>-<date> --out council-process-<slug>-<date>.html

Schema: references/run-json.md. Every section is optional. Standard library only.
"""
import argparse
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "templates" / "process-map.html"

GRADE_CLASS = {"VERIFIED": "ver", "CORROBORATED": "ver", "CREDIBLE": "cre", "ALLEGED": "all",
               "CONTRADICTED": "con", "UNKNOWN": "unk"}

LABELS = {
    "en": {"flow": "1 · The flow", "flow_sub": "The debate runs down the left; the fact desk feeds verified answers back in between rounds.",
           "debate": "Debate", "desk": "Fact desk", "rooms": "2 · Who sat in which room", "seat": "Seat", "total": "Rooms",
           "facts": "3 · How the facts moved", "facts_sub": "Each claim's grade as successive stages checked it.",
           "conv": "4 · What converged, what stayed open", "converged": "Converged", "settled": "Settled late",
           "open": "Still open", "first": "First step:", "new": "NEW", "loop_used": "Reframe loop used.",
           "loop_unused": "Closed loop, available but not used."},
    "fr": {"flow": "1 · Le déroulé", "flow_sub": "Le débat se lit à gauche ; le fact desk réinjecte des réponses vérifiées entre les tours.",
           "debate": "Débat", "desk": "Fact desk", "rooms": "2 · Qui a siégé dans quelle salle", "seat": "Siège", "total": "Salles",
           "facts": "3 · Comment les faits ont évolué", "facts_sub": "La note de chaque affirmation au fil des vérifications.",
           "conv": "4 · Ce qui a convergé, ce qui reste ouvert", "converged": "Convergence", "settled": "Tranché en fin de débat",
           "open": "Toujours ouvert", "first": "Première étape :", "new": "NOUVEAU", "loop_used": "Boucle de recadrage utilisée.",
           "loop_unused": "Boucle de recadrage disponible, non utilisée."},
}

e = lambda s: html.escape(str(s), quote=True)


def dot(seat, big=False):
    size = ' style="background:{c}{x}"'.format(c=e(seat.get("color", "#868e96")), x=";width:16px;height:16px" if big else "")
    return f'<i class="dot"{size} title="{e(seat.get("name", ""))}"></i>'


def card(c, seats):
    parts = [f'<div class="card mini{" room" if c.get("members") else ""}"><b>{e(c.get("title", ""))}</b>']
    if c.get("pipe"):
        parts.append('<div class="pipe">' + "→".join(f"<i>{e(p)}</i>" for p in c["pipe"]) + "</div>")
    if c.get("members"):
        parts.append('<div class="members">' + "".join(dot(seats.get(m, {"name": m}), True) for m in c["members"]) + "</div>")
    if c.get("text"):
        cls = "focus" if c.get("members") else ""
        parts.append(f'<div class="{cls}">{e(c["text"])}</div>' if cls else e(c["text"]))
    if c.get("flag"):
        parts.append(f'<span class="flag">{e(c["flag"])}</span>')
    parts.append("</div>")
    return "".join(parts)


def grid(cards, seats):
    n = len(cards)
    cls = "r3" if n >= 3 else "r2" if n == 2 else ""
    return f'<div class="row {cls}">' + "".join(card(c, seats) for c in cards) + "</div>"


def desk(d):
    if not d:
        return '<div class="spacer"></div>'
    items = "".join(f"<li>{e(i)}</li>" for i in d.get("items", []))
    return f'<aside class="desk"><b>{e(d.get("title", ""))}</b><ul>{items}</ul></aside>'


def build(data):
    L = LABELS.get(data.get("lang", "en"), LABELS["en"])
    seats = {s["id"]: s for s in data.get("seats", [])}
    b = [f'<h1>{e(data.get("title", "How the council reached its verdict"))}</h1>']
    if data.get("question"):
        b.append(f'<p class="lede">{e(data["question"])}' + (f' · {e(data.get("level"))}' if data.get("level") else "") + "</p>")
    if data.get("stats"):
        b.append('<div class="stats">' + "".join(f'<div class="stat"><b>{e(s["value"])}</b><span>{e(s["label"])}</span></div>' for s in data["stats"]) + "</div>")
    if seats:
        b.append('<div class="legend">' + "".join(f'<span class="seat">{dot(s)}{e(s["name"])}</span>' for s in seats.values()) + "</div>")

    # flow
    stages = data.get("stages", [])
    if stages or data.get("final"):
        b.append(f'<h2>{L["flow"]}</h2><p class="sub">{L["flow_sub"]}</p><div class="flow">')
        b.append(f'<div class="lane-h">{L["debate"]}</div><div class="lane-h fact">{L["desk"]}</div>')
        for i, st in enumerate(stages):
            sub = f' <small>· {e(st["subtitle"])}</small>' if st.get("subtitle") else ""
            inner = grid(st.get("cards", []), seats) if st.get("cards") else ""
            if st.get("seats_list"):
                chips = "".join(f'<span class="s">{dot(seats[s])}{e(seats[s]["name"])}' + (f'<span class="new">{L["new"]}</span>' if seats[s].get("new") else "") + "</span>" for s in st["seats_list"] if s in seats)
                inner = f'<div class="card"><div class="seats7">{chips}</div>' + (f'<div class="out">{e(st["note"])}</div>' if st.get("note") else "") + "</div>"
            elif st.get("note"):
                inner += f'<div class="out">{e(st["note"])}</div>'
            b.append(f'<section class="stage"><span class="num">{i}</span><h3>{e(st.get("title", ""))}{sub}</h3>{inner}</section>')
            b.append(desk(st.get("desk")))
        loop = data.get("loop")
        if loop:
            head = L["loop_used"] if loop.get("used") else L["loop_unused"]
            b.append('<div class="loop"><svg width="46" height="34" viewBox="0 0 46 34" aria-hidden="true"><path d="M40 28 H12 a9 9 0 0 1 0-18 H34" fill="none" stroke="currentColor" stroke-width="2.5" stroke-dasharray="4 3" style="color:var(--loop)"/><path d="M30 5 l6 5 -6 5" fill="none" stroke="currentColor" stroke-width="2.5" style="color:var(--loop)"/></svg>'
                     f'<div><strong style="color:var(--loop)">{head}</strong> {e(loop.get("text", ""))}</div></div>')
        fin = data.get("final")
        if fin:
            cards = "".join(card(c, seats) for c in fin.get("cards", []))
            if fin.get("verdict"):
                fs = f'<div class="out"><strong>{L["first"]}</strong> {e(fin["first_step"])}</div>' if fin.get("first_step") else ""
                cards += f'<div class="card mini verdict"><b>Verdict</b>{e(fin["verdict"])}{fs}</div>'
            n = len(fin.get("cards", [])) + (1 if fin.get("verdict") else 0)
            cls = "r3" if n >= 3 else "r2" if n == 2 else ""
            b.append(f'<section class="stage"><span class="num">{len(stages)}</span><h3>{e(fin.get("title", ""))}</h3><div class="row {cls}">{cards}</div></section><div class="spacer"></div>')
        b.append("</div>")

    # rooms matrix
    rooms = data.get("rooms", [])
    if rooms and seats:
        b.append(f'<h2>{L["rooms"]}</h2>')
        if data.get("rooms_note"):
            b.append(f'<p class="sub">{e(data["rooms_note"])}</p>')
        head = f'<tr><th>{L["seat"]}</th>' + "".join(f"<th>{e(r['label'])}</th>" for r in rooms) + f'<th>{L["total"]}</th></tr>'
        rows = []
        for sid, s in seats.items():
            cells = "".join(f"<td>{dot(s)}</td>" if sid in r["members"] else '<td class="empty">·</td>' for r in rooms)
            total = sum(sid in r["members"] for r in rooms)
            rows.append(f'<tr><td><span class="seat">{dot(s)}{e(s["name"])}</span></td>{cells}<td class="tot">{total}</td></tr>')
        b.append('<div style="overflow-x:auto"><table class="mx">' + head + "".join(rows) + "</table></div>")

    # facts
    facts = data.get("facts", [])
    if facts:
        b.append(f'<h2>{L["facts"]}</h2><p class="sub">{L["facts_sub"]}</p><div class="evo">')
        for f in facts:
            steps = []
            for t in f.get("trail", []):
                g = str(t.get("grade", "")).upper()
                steps.append(f'<span class="g {GRADE_CLASS.get(g, "unk")}">{e(g)}</span><span class="who">{e(t.get("who", ""))}</span>')
            b.append(f'<div class="ev"><div class="claim">{e(f.get("claim", ""))}</div><div class="trail">' + '<span class="arr">→</span>'.join(steps) + "</div></div>")
        b.append("</div>")

    # convergence
    conv = data.get("convergence")
    if conv:
        cols = [("converged", "var(--ok)"), ("settled", "var(--warn)"), ("open", "var(--loop)")]
        b.append(f'<h2>{L["conv"]}</h2><div class="conv">')
        for key, color in cols:
            items = "".join(f"<li>{e(x)}</li>" for x in conv.get(key, []))
            if items:
                b.append(f'<div class="card"><h4 style="color:{color}">{L[key]}</h4><ul>{items}</ul></div>')
        b.append("</div>")

    if data.get("date"):
        b.append(f'<footer>{e(data.get("title", "Council"))} · {e(data["date"])}</footer>')
    return "\n".join(b)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--run", required=True, help="run folder containing run.json")
    p.add_argument("--out", required=True)
    a = p.parse_args()
    data = json.loads((pathlib.Path(a.run) / "run.json").read_text(encoding="utf-8"))
    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("{{LANG}}", e(data.get("lang", "en"))).replace("{{TITLE}}", e(data.get("title", "Council process"))).replace("{{BODY}}", build(data))
    pathlib.Path(a.out).write_text(page, encoding="utf-8")
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
