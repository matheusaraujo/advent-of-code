from helpers import count_combinations


def part1(puzzle_input):
    return sum(c for (_, c) in count_combinations([int(x) for x in puzzle_input], 150))
