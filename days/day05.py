from pathlib import Path

from aoclib.io import read_lines
from aoclib.parsing import ints

# days/day05.py -> inputs/day05.small.txt (small) and inputs/day05.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt"),
    ("large", INPUT_DIR / f"{NAME}.txt"),
]


def part1(lines: list[str]) -> int:
    ranges = [tuple(int(n) for n in line.split('-')) for line in lines if '-' in line]
    ids = [int(line) for line in lines if line.isdigit()]
    r = 0
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                r += 1
                break
    return r


def part2(lines: list[str]) -> int:
    ranges = [tuple(int(n) for n in line.split('-')) for line in lines if '-' in line]
    merged = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return sum (end - start + 1 for start, end in merged)


if __name__ == "__main__":
    for label, path in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
