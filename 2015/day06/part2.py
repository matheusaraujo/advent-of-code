from helpers import solve


def part2(puzzle_input):
    def turnon(x):
        return x + 1

    def turnoff(x):
        return max(x - 1, 0)

    def toggle(x):
        return x + 2

    return solve(puzzle_input, turnon, turnoff, toggle)
