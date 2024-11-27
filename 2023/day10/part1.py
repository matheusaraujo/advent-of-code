from helpers import find_longest_cycle


def part1(puzzle_input):
    (cycle, _) = find_longest_cycle(puzzle_input)
    return len(cycle) / 2
