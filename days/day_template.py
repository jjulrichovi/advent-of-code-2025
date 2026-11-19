from pathlib import Path

from aoclib.io import read_lines

# days/day05.py -> inputs/day05.small.txt (small) and inputs/day05.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt"),
    ("large", INPUT_DIR / f"{NAME}.txt"),
]


def part1(lines: list[str]) -> int:
    return 0


def part2(lines: list[str]) -> int:
    return 0


if __name__ == "__main__":
    for label, path in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
