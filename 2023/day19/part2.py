from helpers import read_workflows


def invert_op(operation):
    k, d, v = operation[0], operation[1], int(operation[2:])
    if d == "<":
        return f"{k}>{str(int(v)-1)}"
    return f"{k}<{str(int(v)+1)}"


def create_graph(workflows):
    graph = {}
    for idx_wf, operations in workflows.items():
        for idx_op, operation in enumerate(operations):
            graph[(idx_wf, idx_op)] = {}
            if operation[0] is True:
                graph[(idx_wf, idx_op)][(operation[1], 0)] = operation[0]
            else:
                graph[(idx_wf, idx_op)][operation[1], 0] = operation[0]
                graph[(idx_wf, idx_op)][idx_wf, idx_op + 1] = invert_op(operation[0])
    return graph


def calculate_combinations_in_path(path):
    ranges = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}

    for p in path:
        if p is True:
            continue

        k, d, v = p[0], p[1], int(p[2:])
        if d == ">":
            ranges[k][0] = max(ranges[k][0], v + 1)
        elif d == "<":
            ranges[k][1] = min(ranges[k][1], v - 1)

    ans = 1
    for _, (start, end) in ranges.items():
        ans *= end - start + 1
    return ans


def search_a0(node, graph, path):
    if node == ("A", 0):
        return calculate_combinations_in_path(path)

    if node == ("R", 0):
        return 0

    ans = 0
    for adj in graph[node]:
        ans += search_a0(adj, graph, path + [graph[node][adj]])

    return ans


def part2(puzzle_input):
    workflows, _ = read_workflows(puzzle_input)
    graph = create_graph(workflows)
    return search_a0(("in", 0), graph, [])
