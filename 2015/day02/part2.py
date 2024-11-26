from helpers import solve


def equation(length, width, height):
    return length * width * height + 2 * (length + width)


def part2(puzzle_input):
    return solve(puzzle_input, equation)
