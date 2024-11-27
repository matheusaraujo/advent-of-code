up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]

mapping = {
    "|": [up, down],
    "-": [left, right],
    "L": [up, right],
    "J": [up, left],
    "7": [down, left],
    "F": [down, right],
}


def connect(g, x, y, s):
    if (x, y) not in g:
        g[(x, y)] = []
    m = mapping[s]
    g[(x, y)].append((x + m[0][0], y + m[0][1]))
    g[(x, y)].append((x + m[1][0], y + m[1][1]))


def find_longest_cycle(puzzle_input):
    s = puzzle_input

    i0, j0, m, n, g, v, path = 0, 0, len(s), len(s[0]), {}, {}, []

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
                for x1 in g[n]:
                    if x1 not in v:
                        st.append(x1)
                a += 1
                if a > ans:
                    ans = a
                    path.append(n)
        del g[(i0, j0)]

    return (path, s)
