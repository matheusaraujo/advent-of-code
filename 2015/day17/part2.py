from helpers import count_combinations


def part2(puzzle_input):
    return count_combinations([int(x) for x in puzzle_input], 150)[0][1]
