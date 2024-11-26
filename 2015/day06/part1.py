from helpers import solve


def part1(puzzle_input):
    def turnon(_):
        return 1

    def turnoff(_):
        return 0

    def toggle(x):
        return 1 if x == 0 else 0

    return solve(puzzle_input, turnon, turnoff, toggle)
