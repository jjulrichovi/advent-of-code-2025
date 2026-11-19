from pathlib import Path


def read_input(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def read_lines(path: str | Path) -> list[str]:
    return read_input(path).splitlines()


def read_ints(path: str | Path) -> list[int]:
    return [int(x) for x in read_lines(path)]


def read_grid(path: str | Path) -> list[list[str]]:
    return [list(line) for line in read_lines(path)]
