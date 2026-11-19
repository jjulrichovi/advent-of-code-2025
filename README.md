# Advent of Code 2025

Python solutions plus a small helper library.

## Setup (new machine or new venv)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`requirements.txt` installs pytest and the project itself in editable mode
(`-e .`), so `import aoclib` works from anywhere. Edits to `aoclib` apply
immediately; re-run `pip install -e .` only for a new venv or when adding a
new top-level package (list it in `pyproject.toml` under `packages`).

## Layout

| Path | Purpose |
| --- | --- |
| `aoclib/` | Generic helpers (`io`, `parsing`, `grid`) |
| `days/` | One file per day; `day_template.py` is the template |
| `inputs/` | `dayNN.small.txt` (example) and `dayNN.txt` (real input) |
| `tests/` | Unit tests for `aoclib` only |

## New day

1. Copy `days/day_template.py` to `days/dayNN.py`.
2. Copy `inputs/day_template.small.txt` and `inputs/day_template.txt` to
   `inputs/dayNN.small.txt` and `inputs/dayNN.txt`, and paste the data in.
3. Implement `part1` / `part2`.

Running a day file processes the small input first, then the large one if it
exists. Use the "Run current day" launch config (F5) or:

```powershell
python days\day05.py
```

## Tests

```powershell
pytest
```

Also available in the VS Code Testing panel.
