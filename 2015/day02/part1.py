from helpers import solve


def equation(l, w, h):
    return 2 * l * w + 2 * l * h + 2 * w * h + l * w


def part1(puzzle_input):
    return solve(puzzle_input, equation)
