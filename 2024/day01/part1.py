from helpers import parse_input


def part1(puzzle_input):
    left, right = parse_input(puzzle_input)

    return sum(abs(l - r) for l, r in zip(left, right))
