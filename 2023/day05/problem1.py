import sys

from helpers import read_input, mapping

def problem1(input):
    
    seeds, maps = read_input(input)
    ans = sys.maxsize

    for s in seeds:
        for m in maps: s = mapping(s, m)
        ans = min(ans, s)

    return ans
    