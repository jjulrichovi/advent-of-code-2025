from collections.abc import Iterator, Sequence

Point = tuple[int, int]

DIRS4: list[Point] = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W
DIRS8: list[Point] = [(dx, dy) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dx, dy) != (0, 0)]


def neighbors(p: Point, width: int, height: int, diagonal: bool = False) -> Iterator[Point]:
    """Yield in-bounds neighbours of p (x, y)."""
    for dx, dy in DIRS8 if diagonal else DIRS4:
        x, y = p[0] + dx, p[1] + dy
        if 0 <= x < width and 0 <= y < height:
            yield (x, y)


def browse_all(grid: Sequence[Sequence]) -> Iterator[Point]:
    for h in range(len(grid)):
        for w in range(len(grid[h])):
            yield (h, w)


def manhattan(a: Point, b: Point) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dist(p1: list[int], p2: list[int]) -> int:
    return sum((a - b)**2 for a, b in zip(p1, p2))