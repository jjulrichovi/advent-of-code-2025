from pathlib import Path

from aoclib.io import read_lines
from aoclib.parsing import ints

# days/day12.py -> inputs/day12.small.txt (small) and inputs/day12.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt"),
    ("large", INPUT_DIR / f"{NAME}.txt"),
]


def read_shapes_and_regions(lines):
    shps = []
    regs = []
    curr = None
    for line in lines:
        line = line.strip()
        if not line:
            curr = None
        elif line.endswith(":"):
            curr = []
            shps.append(curr)
        elif curr is not None:
            curr.append([c == "#" for c in line])
        else:
            r = ints(line)
            w, h, cnts = r[0], r[1], r[2:]
            #print(f"Region {w}x{h} {cnts}")
            regs.append((w, h, cnts))
    return shps, regs


def normalize(cells):
    # offsets relative to the first cell
    cells = sorted(cells, key=lambda c: (c[1], c[0]))
    fx, fy = cells[0]
    return tuple((x - fx, y - fy) for x, y in cells)


def rotations(shape):
    cells = [(x, y) for y, row in enumerate(shape) for x, c in enumerate(row) if c]
    result = set()
    for _ in range(4):
        cells = [(-y, x) for x, y in cells]  # rotate 90 deg
        result.add(normalize(cells))
        result.add(normalize([(-x, y) for x, y in cells]))  # flip
    return sorted(result)


def get_shape_types(w, h, shapes, counts):
    """One entry per shape used: [size, count left, placement masks grouped by anchor cell]."""
    shape_types = []
    for s, n in zip(shapes, counts):
        if n == 0:
            continue
        by_anchor = {}
        for cells in rotations(s):
            max_x = max(x for x, _ in cells)
            min_x = min(x for x, _ in cells)
            max_y = max(y for _, y in cells)
            for ay in range(h - max_y):
                for ax in range(w):
                    if not (0 <= ax + min_x and ax + max_x < w):
                        continue
                    mask = 0
                    for dx, dy in cells:
                        mask |= 1 << ((ay + dy) * w + ax + dx)
                    by_anchor.setdefault(ay * w + ax, []).append(mask)
        shape_types.append([sum(map(sum, s)), n, by_anchor])
    shape_types.sort(key=lambda t: t[0], reverse=True)  # large shapes first
    return shape_types


def solve(w, h, pos, board, shape_types, reserve, failed):
    counts = tuple(t[1] for t in shape_types)
    if not any(counts):
        return True
    # skipped cells are marked in board, so (board, counts) also fixes pos and reserve
    state = (board, counts)
    if state in failed:
        return False
    while pos < w * h and board >> pos & 1:
        pos += 1
    if pos >= w * h:
        return False
    for t in shape_types:
        if t[1] == 0:
            continue
        t[1] -= 1
        for m in t[2].get(pos, ()):
            if not m & board and solve(w, h, pos + 1, board | m, shape_types, reserve, failed):
                return True
        t[1] += 1
    # leave this cell empty
    if reserve > 0 and solve(w, h, pos + 1, board | 1 << pos, shape_types, reserve - 1, failed):
        return True
    failed.add(state)
    return False


def part1(lines: list[str]) -> int:
    shapes, regions = read_shapes_and_regions(lines)
    sum_fitting = 0
    for w, h, counts in regions:
        area = sum(n * sum(map(sum, s)) for s, n in zip(shapes, counts))
        if area > w * h:
            continue
        # trivial - each shape gets its full box block => no interlocking with other blocks requied
        used = [s for s, n in zip(shapes, counts) if n > 0]
        bw = max(len(s[0]) for s in used)
        bh = max(len(s) for s in used)
        if sum(counts) <= (w // bw) * (h // bh):
            sum_fitting += 1
            continue
        shape_types = get_shape_types(w, h, shapes, counts)
        # reserve = cells that may stay empty; failed = states proven unsolvable (per region)
        if solve(w, h, 0, 0, shape_types, w * h - area, set()):
            sum_fitting += 1
    return sum_fitting


if __name__ == "__main__":
    for label, path in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print("Part 1:", part1(data))
