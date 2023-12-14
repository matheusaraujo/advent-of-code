from itertools import permutations

from helpers import int_code


def part1(puzzle_input):
    program = [int(x) for x in puzzle_input.split(",")]

    arrangements = list(permutations(range(0, 5)))

    ans = 0
    for arrangement in arrangements:
        signal = 0
        for i in range(5):
            signal = int_code(program[:], 0, [arrangement[i], signal])[0]
        ans = max(ans, signal)

    return ans
