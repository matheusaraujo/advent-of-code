directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solve(_map, steps):
    i, j = len(_map) // 2, len(_map[0]) // 2
    pos = set()
    pos.add((i, j))

    for _ in range(steps):
        n_pos = set()

        for p in pos:
            for d in directions:
                i, j = p[0] + d[0], p[1] + d[1]

                if _map[i % len(_map)][j % len(_map[0])] != "#":
                    n_pos.add((i, j))

        pos = n_pos

    return len(pos)
