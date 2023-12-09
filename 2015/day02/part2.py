from helpers import solve


def equation(l, w, h):
    return l * w * h + 2 * (l + w)


def part2(puzzle_input):
    return solve(puzzle_input, equation)
