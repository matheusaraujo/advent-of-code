def predict_next(v):
    nv = [v[i] - v[i - 1] for i in range(1, len(v))]
    if all(x == 0 for x in nv):
        return v[-1]
    return v[-1] + predict_next(nv)


def part1(puzzle_input):
    return sum(predict_next([int(x) for x in line.split(" ")]) for line in puzzle_input)
