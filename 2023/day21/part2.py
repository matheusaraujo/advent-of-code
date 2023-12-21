directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def part2(_map, steps_limit):
    i, j = len(_map) // 2, len(_map[0]) // 2
    pos = set()
    pos.add((i, j))

    for _ in range(steps_limit):
        n_pos = set()

        for p in pos:
            for d in directions:
                i, j = p[0] + d[0], p[1] + d[1]

                i = max(0, min(i, len(_map) - 1))
                j = max(0, min(j, len(_map[i]) - 1))

                if _map[i][j] != "#":
                    n_pos.add((i, j))

        pos = n_pos

    return len(pos)
