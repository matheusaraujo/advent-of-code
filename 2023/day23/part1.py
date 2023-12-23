import sys

sys.setrecursionlimit(10000)

directions = [
    (1, 0, [".", "v"]),
    (-1, 0, [".", "^"]),
    (0, 1, [".", ">"]),
    (0, -1, [".", "<"]),
]


def get_neighbors(graph, node):
    neighbors = []
    for d in directions:
        x, y = node[0] + d[0], node[1] + d[1]
        if graph[x][y] in d[2]:
            neighbors.append((x, y))

    return neighbors


def dfs(graph, current, target, path):
    if current == target:
        path += [current]
        return path

    if current in path:
        return path

    max_path = path

    for neighbor in get_neighbors(graph, current):
        new_path = dfs(graph, neighbor, target, path + [current])
        if len(new_path) > len(max_path):
            max_path = new_path

    return max_path


def part1(puzzle_input):
    source, target = (0, puzzle_input[0].index(".")), (
        len(puzzle_input) - 1,
        puzzle_input[-1].index("."),
    )

    max_path = dfs(puzzle_input, source, target, [])

    return len(max_path) - 1
