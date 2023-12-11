from helpers import mapping


def connect(g, x, y, s):
    if (x, y) not in g:
        g[(x, y)] = []
    m = mapping[s]
    g[(x, y)].append((x + m[0][0], y + m[0][1]))
    g[(x, y)].append((x + m[1][0], y + m[1][1]))


def part2(puzzle_input):
    s = [list((x.replace("\n", ""))) for x in puzzle_input]

    i0, j0, M, N, g, v, path = 0, 0, len(s), len(s[0]), {}, {}, []

    for x in range(M):
        for y in range(N):
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
                if a > ans:
                    ans = a
                    path.append(n)
        del g[(i0, j0)]

    last, edges = path[0], []
    for x in range(1, len(path)):
        z, y = path[x][0], path[x][1]
        if s[z][y] != "|" and s[z][y] != "-":
            edges.append([last, (z, y)])
            last = (z, y)

    edges.append([last, (path[0][0], path[0][1])])

    def is_inside(xp, yp):
        cnt = 0
        for edge in edges:
            (x1, y1), (x2, y2) = edge
            if (yp < y1) != (yp < y2) and xp < x1 + ((yp - y1) / (y2 - y1)) * (x2 - x1):
                cnt += 1
        return cnt % 2 == 1

    ans = 0
    for x in range(M):
        for y in range(N):
            if (x, y) not in path:
                if is_inside(x, y):
                    ans += 1

    return ans
