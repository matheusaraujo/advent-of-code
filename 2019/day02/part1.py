from helpers import simulate


def part1(puzzle_input):
    puzzle_input = puzzle_input[0]
    a = [int(x) for x in puzzle_input.split(",")]
    a[1], a[2] = 12, 2

    simulate(a)

    return a[0]
