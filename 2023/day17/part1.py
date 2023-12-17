from helpers import solve


def part1(puzzle_input):
    grid = [[int(c) for c in r] for r in puzzle_input]

    return solve(grid, 1, 3)
