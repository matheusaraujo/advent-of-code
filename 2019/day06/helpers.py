def make_graph(puzzle_input):
    mm, g = [(x.split(")")[0], x.split(")")[1]) for x in puzzle_input], {}

    for m in mm:
        if not m[0] in g:
            g[m[0]] = []
        g[m[0]].append(m[1])

    return g
