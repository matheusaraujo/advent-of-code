from helpers import move


def part1(puzzle_input):
    v = {(0, 0): True}
    x, y = 0, 0

    for m in puzzle_input:
        x, y = move(x, y, m, v)

    return len(v)
