from helpers import simulate


def part1(puzzle_input, noun=None, verb=None):
    a = [int(x) for x in puzzle_input.split(",")]

    if noun is not None:
        a[1] = noun

    if verb is not None:
        a[2] = verb

    simulate(a)

    return a[0]
