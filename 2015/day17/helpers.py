from itertools import combinations


def count_combinations(containers, target):
    all_combinations = []
    for r in range(len(containers)):
        valid_combinations = [
            combo for combo in combinations(containers, r) if sum(combo) == target
        ]
        if valid_combinations:
            all_combinations.append((r, len(valid_combinations)))
    return all_combinations
