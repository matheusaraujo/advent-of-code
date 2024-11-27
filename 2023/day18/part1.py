from helpers import solve


def part1(puzzle_input):
    coords, x, y = [(0, 0)], 0, 0

    delta_dir = {
        "D": lambda x, y, m: (x + m, y),
        "U": lambda x, y, m: (x - m, y),
        "L": lambda x, y, m: (x, y - m),
        "R": lambda x, y, m: (x, y + m),
    }

    for line in puzzle_input:
        coords.append((x, y))
        [direction, distance, _] = line.split(" ")
        x, y = delta_dir[direction](x, y, int(distance))

    return int(solve(coords))
