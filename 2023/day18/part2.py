import re

from helpers import solve


def part2(puzzle_input):
    coords, x, y = [(0, 0)], 0, 0

    delta_dir = {
        "0": lambda x, y, m: (x, y + m),
        "1": lambda x, y, m: (x + m, y),
        "2": lambda x, y, m: (x, y - m),
        "3": lambda x, y, m: (x - m, y),
    }

    for line in puzzle_input:
        coords.append((x, y))
        matches = re.search(r"\(#([a-f0-9]{5})([a-f0-9])\)", line)
        distance, direction = int(matches.group(1), 16), matches.group(2)
        x, y = delta_dir[direction](x, y, int(distance))

    return int(solve(coords))
