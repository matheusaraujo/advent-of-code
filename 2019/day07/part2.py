from itertools import permutations

from helpers import IntCode


def part2(puzzle_input):
    puzzle_input = puzzle_input[0]
    program = [int(x) for x in puzzle_input.split(",")]

    arrangements = list(permutations(range(5, 10)))

    ans = 0

    for arrangement in arrangements:
        amps = []

        for i in range(5):
            amps.append(IntCode(program[:], [arrangement[i]]))

        signal = 0

        while any(not amp.halt for amp in amps):
            for i in range(5):
                signal = amps[i].execute([signal])

        ans = max(ans, signal)

    return ans
