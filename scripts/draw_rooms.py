#!/usr/bin/env python3
"""Reproducible random room draw for a council.

Example:
  python3 draw_rooms.py --seats "Contrarian,First Principles,Expansionist,Outsider,Executor,Abstainer,Context Realist" \
      --rounds 3 --rooms 2 --size 4 --seed 20261020 --balance

Prints a readable table and, with --json, the draw as JSON (ready for run.json "rooms").
"""
import argparse
import json
import random
import sys
from collections import Counter


def draw(seats, rounds, rooms, size, rng):
    out = []
    for r in range(1, rounds + 1):
        for k in range(rooms):
            out.append({"label": f"R{r} · {chr(65 + k)}", "members": sorted(rng.sample(seats, size), key=seats.index)})
    return out


def balanced(result, seats, rounds, rooms, size):
    counts = Counter(m for room in result for m in room["members"])
    if any(counts[s] == 0 for s in seats):
        return False
    avg = rounds * rooms * size / len(seats)
    return max(counts.values()) <= avg + 2 and min(counts.values()) >= max(1, avg - 2)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--seats", required=True, help="comma-separated seat names (or slugs)")
    p.add_argument("--rounds", type=int, default=2)
    p.add_argument("--rooms", type=int, default=2, help="rooms per round")
    p.add_argument("--size", type=int, default=0, help="seats per room (default: ~60%% of seats)")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--balance", action="store_true", help="re-draw until every seat sits at least once and counts stay within average ± 2")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    seats = [s.strip() for s in a.seats.split(",") if s.strip()]
    size = a.size or max(2, round(len(seats) * 0.6))
    if size > len(seats):
        sys.exit("room size larger than the number of seats")

    rng = random.Random(a.seed)
    result = draw(seats, a.rounds, a.rooms, size, rng)
    tries = 1
    while a.balance and not balanced(result, seats, a.rounds, a.rooms, size) and tries < 1000:
        result = draw(seats, a.rounds, a.rooms, size, rng)
        tries += 1

    counts = Counter(m for room in result for m in room["members"])
    if a.json:
        print(json.dumps({"seed": a.seed, "tries": tries, "rooms": result, "counts": counts}, ensure_ascii=False, indent=2))
        return
    for room in result:
        print(f"{room['label']}: {', '.join(room['members'])}")
    print()
    print("Seats per member: " + ", ".join(f"{s} {counts[s]}" for s in seats))
    if a.balance:
        print(f"(balanced draw after {tries} attempt{'s' if tries > 1 else ''}, seed {a.seed})")


if __name__ == "__main__":
    main()
