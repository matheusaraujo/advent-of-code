def dfs(g, c, v, d):
    if c in v or c not in g:
        return d

    v[c], ans = True, d

    for t in g[c]:
        ans += dfs(g, t, v, d + 1)

    return ans


def part1(puzzle_input):
    mm, g = [(x.split(")")[0], x.split(")")[1]) for x in puzzle_input], {}

    for m in mm:
        if not m[0] in g:
            g[m[0]] = []
        g[m[0]].append(m[1])

    return dfs(g, "COM", {}, 0)
