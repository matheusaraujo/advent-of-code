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
        if 0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y] in d[2]:
            neighbors.append((x, y))

    return neighbors


def part1(puzzle_input):
    source, target = (0, puzzle_input[0].index(".")), (
        len(puzzle_input) - 1,
        puzzle_input[-1].index("."),
    )

    max_path, queue = [], [(source, set())]

    while queue:
        current, path = queue.pop(0)

        if current == target:
            if len(path) > len(max_path):
                max_path = path
            continue

        for neighbor in get_neighbors(puzzle_input, current):
            if neighbor not in path:
                queue.append((neighbor, path | set([neighbor])))

    return len(max_path)
