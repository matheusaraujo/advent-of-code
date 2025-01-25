from helpers import simulate


def part2(puzzle_input):
    part1 = simulate(puzzle_input)
    for i, instruction in enumerate(puzzle_input):
        if instruction.endswith(" -> b"):
            puzzle_input[i] = str(part1) + " -> b"
    return simulate(puzzle_input)
