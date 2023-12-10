from helpers import mapping


def connect(g, x, y, s):
    if (x, y) not in g:
        g[(x, y)] = []
    m = mapping[s]
    g[(x, y)].append((x + m[0][0], y + m[0][1]))
    g[(x, y)].append((x + m[1][0], y + m[1][1]))


def part1(puzzle_input):
    s = [list((x.replace("\n", ""))) for x in puzzle_input]

    i0, j0, m, n, g, v = 0, 0, len(s), len(s[0]), {}, {}

    for x in range(m):
        for y in range(n):
            if s[x][y] == "S":
                i0, j0 = x, y
            elif s[x][y] != ".":
                connect(g, x, y, s[x][y])

    ans = 0

    for x in mapping:
        connect(g, i0, j0, x[0])
        v, st = {}, [(i0, j0)]
        a = 0

        while st:
            n = st.pop()

            if n in v:
                continue

            v[n] = True
            if n in g:
                for x in g[n]:
                    if x not in v:
                        st.append(x)
                a += 1

        del g[(i0, j0)]
        ans = max(ans, a)

    return ans / 2
