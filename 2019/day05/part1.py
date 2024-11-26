from helpers import simulate


def part1(puzzle_input):
    a = [int(x) for x in puzzle_input[0].split(",")]
    return simulate(a, 1)
