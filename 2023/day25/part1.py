import random


def get_group(node, groups):
    return next(n for n in groups if node in n)


def part1(puzzle_input):
    nodes, edges, groups = set(), set(), []

    for line in puzzle_input:
        node, connections = line.split(": ")
        connections = connections.split(" ")
        nodes.update({node, *connections})
        edges.update({(node, w) for w in connections})

    while True:
        groups = [{v} for v in nodes]

        while len(groups) > 2:
            node1, node2 = random.choice([*edges])

            group1 = get_group(node1, groups)
            group2 = get_group(node2, groups)

            if group1 != group2:
                group1.update(group2)
                groups.remove(group2)

        # look for 3 disconnected edges
        if sum(get_group(u, groups) != get_group(v, groups) for u, v in edges) == 3:
            break

    return len(groups[0]) * len(groups[1])
