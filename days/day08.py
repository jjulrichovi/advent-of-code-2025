from functools import reduce
from math import prod
from pathlib import Path

from aoclib.grid import dist
from aoclib.io import read_lines
from aoclib.parsing import ints

import operator

# days/day08.py -> inputs/day08.small.txt (small) and inputs/day08.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt", 10),
    ("large", INPUT_DIR / f"{NAME}.txt", 1000),
]


def part1(lines: list[str], no_connections: int) -> int:
    points = {(*ints(line),) for line in lines}
    distances = {(dist(p1, p2), p1, p2) for i, p1 in enumerate(points) for j, p2 in enumerate(points) if i > j}
    circuits= []
    for d, p1, p2 in sorted(distances, key=lambda x: x[0])[:no_connections]:
        for c in circuits:
            if p1 in c and p2 in c:  # same ciscuit, ignore
                break
            elif p1 in c or p2 in c:
                px = p1 if p1 not in c else p2
                c.add(px)
                for cx in circuits:
                    if cx is not c and px in cx:
                        c.update(cx)
                        circuits.remove(cx)
                        break
                break
        else:
            circuits.append({p1, p2})
    sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    return prod([len(c) for c in sorted_circuits[:3]])


def part2(lines: list[str]) -> int:
    points = {(*ints(line),) for line in lines}
    distances = {(dist(p1, p2), p1, p2) for i, p1 in enumerate(points) for j, p2 in enumerate(points) if i > j}
    circuits= []
    for d, p1, p2 in sorted(distances, key=lambda x: x[0]):
        for c in circuits:
            if p1 in c and p2 in c:  # same ciscuit, ignore
                break
            elif p1 in c or p2 in c:
                px = p1 if p1 not in c else p2
                c.add(px)
                for cx in circuits:
                    if cx is not c and px in cx:
                        c.update(cx)
                        circuits.remove(cx)
                        break
                break
        else:
            circuits.append({p1, p2})
        if len(circuits) == 1 and len(circuits[0]) == len(points):
            print(f"Fully connected. Last points added: {p1}, {p2}. Distance: {d}")
            return p1[0]*p2[0]
    return 0

if __name__ == "__main__":
    for label, path, connections in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print("Part 1:", part1(data, connections))
        print("Part 2:", part2(data))
