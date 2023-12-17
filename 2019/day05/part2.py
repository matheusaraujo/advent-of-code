from helpers import simulate


def part2(puzzle_input, simulation_input):
    a = [int(x) for x in puzzle_input.split(",")]
    return simulate(a, simulation_input)
