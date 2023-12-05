import sys

from helpers import read_input, mapping

def problem1(input):
    seeds, maps = read_input(input)
    ans = sys.maxsize

    for s in seeds:
        s = mapping(s, maps)
        ans = min(ans, s)

    return ans
    