def get_empty_space(cosmos, galaxies):
    occupied_x = {g[0] for g in galaxies}
    occupied_y = {g[1] for g in galaxies}

    all_x = set(range(len(cosmos)))
    all_y = set(range(len(cosmos[0])))

    empty_x = list(all_x - occupied_x)
    empty_y = list(all_y - occupied_y)

    return (empty_x, empty_y)


def get_galaxies(cosmos):
    return [
        (x, y)
        for x, row in enumerate(cosmos)
        for y, cell in enumerate(row)
        if cell == "#"
    ]


def calculate_distance(g1, g2, expansion_factor, empty_x, empty_y):
    x1, x2 = min(g1[0], g2[0]), max(g1[0], g2[0])
    y1, y2 = min(g1[1], g2[1]), max(g1[1], g2[1])
    count_x = sum(1 for x in empty_x if x1 < x < x2)
    count_y = sum(1 for y in empty_y if y1 <= y <= y2)
    return (
        x2
        - x1
        + y2
        - y1
        + count_x * (expansion_factor - 1)
        + count_y * (expansion_factor - 1)
    )


def calculate_cosmos_distance(cosmos, expansion_factor):
    galaxies = get_galaxies(cosmos)
    empty_x, empty_y = get_empty_space(cosmos, galaxies)

    ans, n = 0, len(galaxies)

    for i in range(n):
        for j in range(i + 1, n):
            ans += calculate_distance(
                galaxies[i], galaxies[j], expansion_factor, empty_x, empty_y
            )

    return ans
