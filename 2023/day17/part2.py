from helpers import solve


def part2(puzzle_input):
    grid = [[int(c) for c in r] for r in puzzle_input]

    return solve(grid, 4, 10)
