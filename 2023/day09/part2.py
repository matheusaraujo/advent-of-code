def predict_previous(v):
    nv = [v[i] - v[i - 1] for i in range(1, len(v))]
    if all(x == 0 for x in nv):
        return v[0]
    return v[0] - predict_previous(nv)


def part2(puzzle_input):
    return sum(
        predict_previous([int(x) for x in line.split(" ")]) for line in puzzle_input
    )
