from collections import Counter

from helpers import parse_input


def part2(puzzle_input):
    left, right = parse_input(puzzle_input)
    count = Counter(left)
    return sum(item * count[item] for item in right if item in count)
