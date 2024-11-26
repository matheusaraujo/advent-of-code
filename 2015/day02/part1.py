from helpers import solve


def equation(length, width, height):
    return (
        2 * length * width + 2 * length * height + 2 * width * height + length * width
    )


def part1(puzzle_input):
    return solve(puzzle_input, equation)
