from helpers import make_graph


# g = graph
# c = current
# t = target
# p = path
def find_path(g, c, t, p):
    if c == t:
        return [c] + p

    if c not in g:
        return None

    for n in g[c]:
        np = find_path(g, n, t, p)
        if np:
            return [c] + np

    return None


def part2(puzzle_input):
    g = make_graph(puzzle_input)

    path_to_you = find_path(g, "COM", "YOU", [])
    path_to_santa = find_path(g, "COM", "SAN", [])

    i = 0
    while path_to_you[i] == path_to_santa[i]:
        i += 1

    return len(path_to_you) - i - 1 + len(path_to_santa) - i - 1
