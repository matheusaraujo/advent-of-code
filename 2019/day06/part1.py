from helpers import make_graph


# g = graph
# c = current
# d = depth
def dfs(g, c, d):
    if c not in g:
        return d

    ans = d

    for n in g[c]:
        ans += dfs(g, n, d + 1)

    return ans


def part1(puzzle_input):
    g = make_graph(puzzle_input)

    return dfs(g, "COM", 0)
