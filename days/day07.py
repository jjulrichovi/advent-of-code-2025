from pathlib import Path

from aoclib.io import read_lines

# days/day07.py -> inputs/day07.small.txt (small) and inputs/day07.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt"),
    ("large", INPUT_DIR / f"{NAME}.txt"),
]


def part1(lines: list[str]) -> int:
    manifolds = [list(line) for line in lines]
    manifolds[0] = ["|" if c == "S" else c for c in manifolds[0]]
    split_cnt = 0
    for i in range(len(manifolds) - 1):
        for b in range(len(manifolds[i])):
            if manifolds[i][b] == "|":
                if manifolds[i + 1][b] == ".": 
                    manifolds[i + 1][b] = "|"
                elif manifolds[i + 1][b] == "^":
                    split_cnt += 1
                    if b > 0 and manifolds[i + 1][b - 1] == ".": 
                        manifolds[i + 1][b - 1] = "|"
                    if b < len(manifolds[i]) - 1 and manifolds[i + 1][b + 1] == ".": 
                        manifolds[i + 1][b + 1] = "|"
    return split_cnt

def part1_recursive(lines: list[str]) -> int:
    manifolds = [list(line) for line in lines]
    def dfs(y: int, x: int, i: int, b: int) -> int:
        if i >= y or b < 0 or b >= x:
            return 0
        if manifolds[i][b] == ".":
            manifolds[i][b] = "|"
            return dfs(y, x, i + 1, b)
        elif manifolds[i][b] == "^":
            return 1 + dfs(y, x, i + 1, b - 1) + dfs(y, x, i + 1, b + 1)
        else:
            return 0
    return dfs(len(manifolds), len(manifolds[0]), 1, manifolds[0].index("S"))

def part2(lines: list[str]) -> int:
    manifolds = [list(line) for line in lines]
    visited = [[False] * len(manifolds[0]) for _ in range(len(manifolds))]
    options = [[0] * len(manifolds[0]) for _ in range(len(manifolds))]
    def dfs2(y: int, x: int, i: int, b: int) -> int:
        if i >= y or b < 0 or b >= x:
            return 0
        if manifolds[i][b] == ".":
            if visited[i][b]:
                return options[i][b]
            visited[i][b] = True
            options[i][b] = dfs2(y, x, i + 1, b)
            return options[i][b]
        elif manifolds[i][b] == "^":
            return 1 + dfs2(y, x, i + 1, b - 1) + dfs2(y, x, i + 1, b + 1)
        else:
            return 0
    return 1 + dfs2(len(manifolds), len(manifolds[0]), 1, manifolds[0].index("S"))

if __name__ == "__main__":
    for label, path in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print(f"Part 1: {part1(data)}, Part 1 Recursive: {part1_recursive(data)}")
        print("Part 2:", part2(data))
