import sys

from helpers import mapping, read_input


def part1(puzzle_input):
    seeds, maps = read_input(puzzle_input)
    ans = sys.maxsize

    for s in seeds:
        s = mapping(s, maps)
        ans = min(ans, s)

    return ans
