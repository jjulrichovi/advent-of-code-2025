from pathlib import Path

from aoclib.grid import browse_all, neighbors
from aoclib.io import read_lines

# days/day04.py -> inputs/day04.small.txt (small) and inputs/day04.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt"),
    ("large", INPUT_DIR / f"{NAME}.txt"),
]


def part1(lines: list[str]) -> int:
    return sum(
      (1 if sum(1 if lines[nh][nw] == "@" else 0 for nh, nw in neighbors((h, w), len(lines[0]), len(lines), True)) < 4 else 0)
      if lines[h][w] == "@" else 0 for h, w in browse_all(lines)
   )

def part2(lines: list[str]) -> int:
    lines = [list(line) for line in lines]
    total_removed = 0
    while True:
        removed = 0
        for h, w in browse_all(lines):
            if lines[h][w] != "@":
                continue
            if sum(1 if lines[nh][nw] == "@" else 0 for nh, nw in neighbors((h, w), len(lines[0]), len(lines), True)) < 4:
                lines[h][w] = "."
                removed += 1
        if removed == 0:
            break
        total_removed += removed
    return total_removed

if __name__ == "__main__":
    for label, path in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
