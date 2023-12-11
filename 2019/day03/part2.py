from helpers import move


def part2(puzzle_input):
    [w1, w2] = [x.split(",") for x in puzzle_input]
    v, c = {}, []

    def f1(x, y, k):
        v[(x, y)] = k

    move(w1, f1)

    def f2(x, y, k):
        if (x, y) in v:
            c.append(k + v[x, y])

    move(w2, f2)

    return min(c)
