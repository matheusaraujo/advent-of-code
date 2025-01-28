from itertools import combinations


def part1(puzzle_input):
    return count_combinations([int(x) for x in puzzle_input], 150)


def count_combinations(containers, target):
    total_combinations = 0
    for r in range(len(containers)):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                total_combinations += 1

    return total_combinations
