import sys

from helpers import mapping, read_input


def part1(input):
    seeds, maps = read_input(input)
    ans = sys.maxsize

    for s in seeds:
        s = mapping(s, maps)
        ans = min(ans, s)

    return ans
