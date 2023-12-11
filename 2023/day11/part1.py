def expand_universe(universe):
    xs, ys = list(range(len(universe))), list(range(len(universe[0])))

    for x, row in enumerate(universe):
        for y, cell in enumerate(row):
            if cell == "#":
                if x in xs:
                    xs.remove(x)
                if y in ys:
                    ys.remove(y)

    print(len(universe), len(universe[0]))

    row = '.' * len(universe[0])
    for x in reversed(xs):
        universe.insert(x, row)

    for i, _ in enumerate(universe):
        for y in reversed(ys):
            universe[i] = universe[i][:y] + '.' + universe[i][y:]

    return universe

def get_galaxies(universe):
    galaxies = []

    for x, row in enumerate(universe):
        for y, cell in enumerate(row):
            if cell == "#":
                galaxies.append((x, y))

    return galaxies

def part1(universe):
    universe = expand_universe(universe)
    galaxies = get_galaxies(universe)

    def calculate_manhattan_distance(g1, g2):
        return abs(g1[0] -g2[0]) + abs(g1[1] - g2[1])

    ans, n = 0, len(galaxies)

    for i in range(n):
        for j in range(i+1, n):
            d = calculate_manhattan_distance(galaxies[i], galaxies[j])
            ans += d

    return ans
