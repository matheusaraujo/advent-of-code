import sys

from helpers import chunk_array


def part1(puzzle_input, cols=6, rows=25):
    layers = chunk_array(list(puzzle_input[0]), cols * rows)

    fewest0, ans = sys.maxsize, 0
    for layer in layers:
        c0, c1, c2 = layer.count("0"), layer.count("1"), layer.count("2")
        if c0 < fewest0:
            ans = c1 * c2
            fewest0 = c0

    return ans
