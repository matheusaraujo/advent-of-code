import re


def part1(puzzle_input):
    return sum(int(x) for x in re.findall(r"-?\d+", puzzle_input[0]))
