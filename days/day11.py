from pathlib import Path

from aoclib.io import read_lines

# days/day11.py -> inputs/day11.small.txt (small) and inputs/day11.txt (large)
INPUT_DIR = Path(__file__).parent.parent / "inputs"
NAME = Path(__file__).stem
INPUTS = [
    ("small", INPUT_DIR / f"{NAME}.small.txt"),
    ("large", INPUT_DIR / f"{NAME}.txt"),
]


def part1(lines: list[str]) -> int:

    def get_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end: return [path]
        pths = []
        for n in graph[start]:
            if n not in path:
                newpths = get_all_paths(graph, n, end, path)
                for np in newpths:
                    pths.append(np)
        return pths
    
    graph = {}
    for line in lines:
        fr, tos = line.split(":")
        graph[fr] = tos.strip().split()
        #print(f"{fr} -> {graph[fr]}")
    
    all_paths = get_all_paths(graph, 'you', 'out')
    #[print(" -> ".join(path)) for path in all_paths]
    return len(all_paths)


def part2(lines: list[str]) -> int:

    def cnt_paths(graph, start, end, dac, fft, cache={}):
        dac = dac or start == 'dac'
        fft = fft or start == 'fft'
        if start == end:
            return 1 if dac and fft else 0
        k= (start, dac, fft)
        if k not in cache:
            cache[k] = sum(
                    cnt_paths(graph, n, end, dac, fft, cache)
                    for n in graph.get(start, [])
                )
        return cache[k]
    
    graph = {}
    for line in lines:
        fr, tos = line.split(":")
        graph[fr] = tos.strip().split()
    
    return cnt_paths(graph, 'svr', 'out', False, False, {})


if __name__ == "__main__":

        path = INPUT_DIR / f"{NAME}.small.p1.txt"
        print(f"--- small ({path}) ---")
        data = read_lines(path)
        print("Part 1:", part1(data))
        path = INPUT_DIR / f"{NAME}.txt"
        print(f"--- large ({path}) ---")
        data = read_lines(path)
        print("Part 1:", part1(data))

        path = INPUT_DIR / f"{NAME}.small.p2.txt"
        print(f"--- small ({path}) ---")
        data = read_lines(path)
        print("Part 2:", part2(data))
        path = INPUT_DIR / f"{NAME}.txt"
        print(f"--- large ({path}) ---")
        data = read_lines(path)
        print("Part 2:", part2(data))
