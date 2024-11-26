from helpers import move


def part1(puzzle_input):
    [w1, w2] = [x.split(",") for x in puzzle_input]
    v, c = {}, []

    def f1(x, y, _):
        v[(x, y)] = 1

    move(w1, f1)

    def f2(x, y, _):
        if (x, y) in v:
            c.append(abs(x) + abs(y))

    move(w2, f2)

    return min(c)
