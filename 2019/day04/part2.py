def meets_criteria(n):
    n, d = str(n), {}
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
        d[n[i]] = d.get(n[i], 0) + 1

    d[n[-1]] = d.get(n[-1], 0) + 1

    return any(c == 2 for c in d.values())


def part2(puzzle_input):
    puzzle_input = puzzle_input[0]
    r = [int(x) for x in puzzle_input.split("-")]
    return sum(meets_criteria(x) for x in range(r[0], r[1]))
