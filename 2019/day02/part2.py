from helpers import simulate


def part2(puzzle_input):
    puzzle_input = puzzle_input[0]
    original_arr = [int(x) for x in puzzle_input.split(",")]

    for noun in range(0, 100):
        for verb in range(0, 100):
            a = original_arr[:]
            a[1], a[2] = noun, verb
            simulate(a)
            if a[0] == 19690720:
                return noun * 100 + verb

    return -1
