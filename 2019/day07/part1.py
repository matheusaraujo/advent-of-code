from itertools import permutations

from helpers import IntCode


def part1(puzzle_input):
    puzzle_input = puzzle_input[0]
    program = [int(x) for x in puzzle_input.split(",")]

    arrangements = list(permutations(range(0, 5)))

    ans = 0
    for arrangement in arrangements:
        signal = 0
        for i in range(5):
            signal = IntCode(program[:], [arrangement[i]]).execute([signal])
        ans = max(ans, signal)

    return ans
