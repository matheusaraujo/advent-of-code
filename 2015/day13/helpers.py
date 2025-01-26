import re
from itertools import permutations


def solve(puzzle_input, people_to_add):
    happiness, people, result = {}, set(), 0

    for line in puzzle_input:
        p1, gain_lose, units, p2 = re.match(
            r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)", line
        ).groups()
        happiness[(p1, p2)] = int(units) if gain_lose == "gain" else -int(units)
        people.add(p1)
        people.add(p2)

    for p1, s in people_to_add:
        people.add(p1)
        for p2 in people:
            happiness[(p1, p2)] = happiness[(p2, p1)] = s

    for perm in permutations(people):
        score = 0
        for i, _ in enumerate(perm):
            score += happiness[(perm[i], perm[(i - 1) % len(perm)])]
            score += happiness[(perm[i], perm[(i + 1) % len(perm)])]
        result = max(result, score)

    return result
