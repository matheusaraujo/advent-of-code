from helpers import solve


def part2(puzzle_input):
    return solve(puzzle_input, lambda total_properties: total_properties[4] == 500)
