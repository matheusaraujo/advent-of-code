from itertools import permutations

from helpers import int_code


def part2(puzzle_input):
    program = [int(x) for x in puzzle_input.split(",")]

    arrangements = list(permutations(range(5, 10)))

    ans = 0

    print("begin")

    for arrangement in arrangements:
        memories, memories_i, outputs_i, halted_i = [], [], [], []
        result = (0, 0, False)

        for i in range(5):
            memories.append(program[:])
            memories_i.append(0)
            outputs_i.append(0)
            halted_i.append(False)

        while True:
            _input = 0
            for i in range(5):
                result = int_code(
                    memories[i],
                    memories_i[i],
                    [arrangement[i], result[0]],
                    outputs_i[i],
                )
                outputs_i[i] = result[0]
                memories_i[i] = result[1]
                halted_i[i] = result[2]

                _input = result[0]

            if all(halted_i):
                break

        print(">>>>>>", arrangement, result)
        ans = max(ans, _input)

    return ans
