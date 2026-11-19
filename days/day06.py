from functools import reduce
import operator
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

OPS = {"+": operator.add, "*": operator.mul}

def part1(lines: list[str]) -> int:
    problem = [ints(line) for line in lines[:-1]]
    operators = lines[-1].split()
    return sum(reduce(OPS[op], col) for col, op in zip(zip(*problem), operators))

def part2(lines: list[str]) -> int:
    problems = [line[::-1] for line in lines[:-1]]
    operators = lines[-1][::-1]
    total = 0
    nos = []
    for i in range(len(operators)):
        no_str = "".join([line[i] for line in problems if line[i] != " "])
        if not no_str:
            continue
        nos.append(int(no_str))
        if operators[i] != " ":
            total += reduce(OPS[operators[i]], nos)
            nos = []
    return total

if __name__ == "__main__":
    for label, path in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
