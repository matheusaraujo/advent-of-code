def part1(puzzle_input):
    s = [list((x.replace("\n", ""))) for x in puzzle_input]

    moves = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}

    changes = {
        "7": {"E": "S", "N": "W"},
        "J": {"S": "W", "E": "N"},
        "L": {"W": "N", "S": "E"},
        "F": {"N": "E", "W": "S"},
        "|": {"E": "E", "S": "S", "W": "W", "N": "N"},
        "-": {"E": "E", "S": "S", "W": "W", "N": "N"},
    }

    def move(i, j, d):
        k = 0
        while True:
            k += 1
            di, dj = moves[d]
            i, j = i + di, j + dj

            if s[i][j][0] == "." or i < 0 or j < 0:
                break

            if s[i][j][0] == "S":
                break

            s[i][j] = (s[i][j][0], k if s[i][j][1] == -1 else min(k, s[i][j][1]))

            d = changes[s[i][j][0]][d]

    m, n = len(s), len(s[0])

    for x in range(m):
        for y in range(n):
            s[x][y] = (s[x][y], -1)
            if s[x][y][0] == "S":
                i0, j0 = x, y
                s[x][y] = (s[x][y][0], 0)

    move(i0, j0, "E")
    move(i0, j0, "S")
    move(i0, j0, "N")
    move(i0, j0, "W")

    ans = 0
    for t in s:
        for u in t:
            ans = max(ans, u[1])

    return ans
