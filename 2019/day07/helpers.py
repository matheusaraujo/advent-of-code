def g(arr, i, mode):
    if mode == 0:
        return arr[arr[i]]
    return arr[i]


def s(arr, i, mode, v):
    if mode == 0:
        arr[arr[i]] = v
    else:
        arr[i] = v


def int_code(memory, i, input_array, output):
    di = 0

    while memory[i] != 99:
        opcode = memory[i] % 100
        m3 = (memory[i] // 10000) % 10
        m2 = (memory[i] // 1000) % 10
        m1 = (memory[i] // 100) % 10

        if opcode == 1:  # sum
            s(memory, i + 3, m3, g(memory, i + 1, m1) + g(memory, i + 2, m2))
            di = 4
        elif opcode == 2:  # multiply
            s(memory, i + 3, m3, g(memory, i + 1, m1) * g(memory, i + 2, m2))
            di = 4
        elif opcode == 3:  # get input
            s(memory, i + 1, m1, input_array.pop(0))
            di = 2
        elif opcode == 4:  # set output
            output = g(memory, i + 1, m1)
            i += 2
            break
        elif opcode == 5:  # jump-if-true
            di = g(memory, i + 2, m2) - i if g(memory, i + 1, m1) != 0 else 3
        elif opcode == 6:  # jump-if-false
            di = g(memory, i + 2, m2) - i if g(memory, i + 1, m1) == 0 else 3
        elif opcode == 7:  # less than
            s(
                memory,
                i + 3,
                m3,
                1 if g(memory, i + 1, m1) < g(memory, i + 2, m2) else 0,
            )
            di = 4
        elif opcode == 8:  # equals
            s(
                memory,
                i + 3,
                m3,
                1 if g(memory, i + 1, m1) == g(memory, i + 2, m2) else 0,
            )
            di = 4

        i += di

    return (output, i, memory[i] == 99)
