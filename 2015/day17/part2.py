from itertools import combinations


def part2(puzzle_input):
    return count_combinations_min_containers([int(x) for x in puzzle_input], 150)


def count_combinations_min_containers(containers, target):
    for r in range(len(containers)):
        valid_combinations = [
            combo for combo in combinations(containers, r) if sum(combo) == target
        ]
        if valid_combinations:
            return len(valid_combinations)
    return 0
