# brute force solution, could be solved using Knapsack,
# https://en.wikipedia.org/wiki/Knapsack_problem

import re
from itertools import product


def solve(puzzle_input, f_restriction):
    weights = parse_input(puzzle_input)
    combs = combinations(len(weights), 100)
    max_score = 0

    for quantities in combs:
        max_score = max(max_score, calculate_score(quantities, weights, f_restriction))

    return max_score


def parse_input(puzzle_input):
    return [
        list(
            int(x)
            for x in re.match(
                r"(\w+): capacity (-?\d+), "
                + r"durability (-?\d+), "
                + r"flavor (-?\d+), "
                + r"texture (-?\d+), "
                + r"calories (-?\d+)",
                input_line,
            ).groups()[1:]
        )
        for input_line in puzzle_input
    ]


def combinations(n, target_sum):
    return [
        comb
        for comb in product(range(target_sum + 1), repeat=n)
        if sum(comb) == target_sum
    ]


def calculate_score(quantities, weights, f_restriction):
    properties = range(5)
    total_properties = [0] * 5

    for i, quantity in enumerate(quantities):
        for prop in properties:
            total_properties[prop] += weights[i][prop] * quantity

    if not f_restriction(total_properties):
        return 0

    total_properties = [max(0, total) for total in total_properties]

    total_score = 1
    for total in total_properties[:-1]:
        total_score *= total

    return total_score
