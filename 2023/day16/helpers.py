from collections import defaultdict

mapping = {
    ".": {
        "R": lambda x, y: [(x, y + 1, "R")],
        "L": lambda x, y: [(x, y - 1, "L")],
        "D": lambda x, y: [(x + 1, y, "D")],
        "U": lambda x, y: [(x - 1, y, "U")],
    },
    "/": {
        "R": lambda x, y: [(x - 1, y, "U")],
        "L": lambda x, y: [(x + 1, y, "D")],
        "D": lambda x, y: [(x, y - 1, "L")],
        "U": lambda x, y: [(x, y + 1, "R")],
    },
    "\\": {
        "R": lambda x, y: [(x + 1, y, "D")],
        "L": lambda x, y: [(x - 1, y, "U")],
        "D": lambda x, y: [(x, y + 1, "R")],
        "U": lambda x, y: [(x, y - 1, "L")],
    },
    "|": {
        "R": lambda x, y: [(x - 1, y, "U"), (x + 1, y, "D")],
        "L": lambda x, y: [(x - 1, y, "U"), (x + 1, y, "D")],
        "D": lambda x, y: [(x + 1, y, "D")],
        "U": lambda x, y: [(x - 1, y, "U")],
    },
    "-": {
        "R": lambda x, y: [(x, y + 1, "R")],
        "L": lambda x, y: [(x, y - 1, "L")],
        "D": lambda x, y: [(x, y - 1, "L"), (x, y + 1, "R")],
        "U": lambda x, y: [(x, y - 1, "L"), (x, y + 1, "R")],
    },
}


def solve(contraption, x, y, d):
    q, rows, cols = [], len(contraption), len(contraption[0])

    q.append((x, y, d))
    v = defaultdict(list)

    while len(q) > 0:
        x, y, d = q.pop()
        v[(x, y)].append(d)

        next_dir = mapping[contraption[x][y]][d](x, y)
        for [nx, ny, nd] in next_dir:
            if -1 < nx < rows and -1 < ny < cols and nd not in v[(nx, ny)]:
                q.append((nx, ny, nd))

    return len(v)
