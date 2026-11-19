from pathlib import Path
import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

from aoclib.io import read_lines
from aoclib.parsing import ints

# days/day10.py -> inputs/day10.small.txt (small) and inputs/day10.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt"),
    ("large", INPUT_DIR / f"{NAME}.txt"),
]

def part1(lines: list[str]) -> int:
    
    def bfs(graph, buttons, currs, depth, target):
        nexts = set()
        for curr in currs:
            if curr == target:
                return depth
            for butt in buttons:
                new = list(curr)
                for b in butt:
                    new[b] = '#' if new[b] == '.' else '.'
                new = ''.join(new)            
                if new not in graph:
                    graph[new] = depth + 1
                    nexts.add(new)
        return bfs(graph, buttons, nexts, depth + 1, target)
    
    sum_depths = 0
    for line in lines:
        target = re.findall(r"\[[\.#]+\]", line)[0][1:-1]
        buttons = [ints(m) for m in re.findall(r"\(([0-9,]+)\)", line)]
        depth = bfs({'.'*len(target): 0}, buttons, {'.'*len(target)}, 0, target)
        #print(f"Target: {target}, Buttons: {buttons}, Voltages: {voltages}, Depth: {depth}")
        sum_depths += depth
    return sum_depths


def part2(lines: list[str]) -> int:
    # BFS does not work here - not even with prunning when reaching limit joltages - still takes too long for the big problems
    # Needed help to remind me about the linear programming problem construction
    # Was a struggle to make Python do this
    sum_depths = 0
    for line in lines:
        buttons = [ints(m) for m in re.findall(r"\(([0-9,]+)\)", line)]
        joltages = ints(re.findall(r"\{([0-9,]+)\}", line)[0])       
        # Constraint: Ax = joltages, x >= 0, x integer
        # Criteria: sum(x) = MIN
        A = np.zeros((len(joltages), len(buttons))) # row length = number of joltages, column length = number of buttons
        for j, butt in enumerate(buttons):
            for b in butt:
                A[b][j] = 1
        #print(f"A:\n{A}")
        depth = milp(
            c=np.ones(len(buttons)),  # criteria: minimize the sum of button presses (all buttons -> all ones in vector c)
            constraints=LinearConstraint(A, joltages, joltages),   # setting same upper and lower bound to have exact match 
            bounds=Bounds(0, np.inf), # button push must be positive
            integrality=np.ones(len(buttons))  # we need integers
        ).fun
        sum_depths += depth
    return sum_depths

if __name__ == "__main__":
    for label, path in INPUTS:
        if not path.exists():
            continue
        data = read_lines(path)
        print(f"--- {label} ({path.name}) ---")
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
