from helpers import move


def part2(puzzle_input):
    puzzle_input = puzzle_input[0]
    v = {(0, 0): True}
    x1, y1, x2, y2 = 0, 0, 0, 0

    for i in range(0, len(puzzle_input), 2):
        m1, m2 = puzzle_input[i], puzzle_input[i + 1]
        x1, y1 = move(x1, y1, m1, v)
        x2, y2 = move(x2, y2, m2, v)

    return len(v)
