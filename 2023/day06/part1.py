import re

from helpers import get_integer_roots


def extract_numbers(s):
    return [int(n) for n in re.findall(r"\d+", s)]


def part1(puzzle_input):
    times, distances, ans = (
        extract_numbers(puzzle_input[0]),
        extract_numbers(puzzle_input[1]),
        1,
    )

    for i, t in enumerate(times):
        # Tt - t^2 > D
        # - t^2 + Tt - D > 0
        x1, x2 = get_integer_roots(-1, t, -distances[i])
        ans *= x2 - x1 - 1

    return ans
