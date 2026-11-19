from itertools import combinations  
from pathlib import Path

from aoclib.io import read_lines
from aoclib.parsing import ints

# days/day09.py -> inputs/day09.small.txt (small) and inputs/day09.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt"),
    ("large", INPUT_DIR / f"{NAME}.txt"),
]


def part1(lines: list[str]) -> int:
    points = {(*ints(line),) for line in lines}
    return max((abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1) for p1, p2 in set(combinations(points, 2)))
    

def part2(lines: list[str]) -> int:
    points = [(*ints(line),) for line in lines]
    n = len(points)
    edges = [(points[i], points[(i + 1) % n]) for i in range(n)]

    def area(p1, p2) -> int:
        return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

    def point_inside(x: float, y: float) -> bool:
        crossings = sum([1  if ax == bx and min(ay, by) < y < max(ay, by) and ax > x else 0 for (ax, ay), (bx, by) in edges])
        return crossings % 2 == 1

    def edge_cuts_rect(e1, e2, rx_lo, rx_hi, ry_lo, ry_hi) -> bool:
        (e1x, e1y), (e2x, e2y) = e1, e2
        if e1x == e2x:  # vertical edge
            return rx_lo < e1x < rx_hi and min(e1y, e2y) < ry_hi and max(e1y, e2y) > ry_lo
        return ry_lo < e1y < ry_hi and min(e1x, e2x) < rx_hi and max(e1x, e2x) > rx_lo
    
    # Largest first - find first valid one is the answer.
    rects = sorted(combinations(points, 2), key=lambda p: area(*p), reverse=True)
    for p1, p2 in rects:
        rx_lo, rx_hi = sorted((p1[0], p2[0]))
        ry_lo, ry_hi = sorted((p1[1], p2[1]))
        if any(edge_cuts_rect(p1, p2, rx_lo, rx_hi, ry_lo, ry_hi) for p1, p2 in edges):
            continue
        if point_inside(rx_lo + 0.5, ry_lo + 0.5):
            return area(p1, p2)
    return 0


if __name__ == "__main__":
    for label, path in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
