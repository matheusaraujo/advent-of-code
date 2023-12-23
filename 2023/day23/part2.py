def get_neighbors(grid, x, y):
    neighbors = []
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] in ".<>^v":
                neighbors.append((nx, ny))
    return neighbors


def get_single_path(graph, start, head):
    count = 1
    while len(graph[head]) == 2:
        nn = [n for _, n in graph[head] if n != start][0]
        start, head = (head, nn)
        count += 1
    return (count, head)


def build_graph(grid):
    graph = {}
    for x, _ in enumerate(grid):
        for y, _ in enumerate(grid[x]):
            if grid[x][y] in ".<>^v":
                graph[(x, y)] = [(1, n) for n in get_neighbors(grid, x, y)]
    return graph


def reduce_graph(graph):
    new_graph = {}
    for k, v in graph.items():
        if len(v) != 2:
            new_graph[k] = [get_single_path(graph, k, n[1]) for n in v]
    return new_graph


def dfs(graph, source, target):
    queue = [(source, 0, set([source]))]
    max_path = 0

    while queue:
        node, dist, visited = queue.pop()
        if node == target:
            max_path = max(max_path, dist)

        for d, nn in graph[node]:
            if nn not in visited:
                queue.append((nn, dist + d, visited | set([nn])))

    return max_path


def part2(puzzle_input):
    source, target = (0, puzzle_input[0].index(".")), (
        len(puzzle_input) - 1,
        puzzle_input[-1].index("."),
    )
    graph = build_graph(puzzle_input)
    graph = reduce_graph(graph)

    return dfs(graph, source, target)
