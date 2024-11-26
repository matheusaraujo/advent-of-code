def meets_criteria(n):
    n = str(n)
    has_double = False
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
        has_double = has_double or n[i] == n[i + 1]

    return has_double


def part1(puzzle_input):
    puzzle_input = puzzle_input[0]
    r = [int(x) for x in puzzle_input.split("-")]
    return sum(meets_criteria(x) for x in range(r[0], r[1]))
