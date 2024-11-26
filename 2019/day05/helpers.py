def g(arr, i, mode):
    if mode == 0:
        return arr[arr[i]]
    return arr[i]


def s(arr, i, v):
    arr[arr[i]] = v


def simulate(memory, simulation_input):
    i, di, simulation_output = 0, 0, -1
    while memory[i] != 99:
        opcode = memory[i] % 100
        _ = (memory[i] // 10000) % 10
        b = (memory[i] // 1000) % 10
        c = (memory[i] // 100) % 10

        if opcode == 1:  # sum
            s(memory, i + 3, g(memory, i + 1, c) + g(memory, i + 2, b))
            di = 4
        elif opcode == 2:  # multiply
            s(memory, i + 3, g(memory, i + 1, c) * g(memory, i + 2, b))
            di = 4
        elif opcode == 3:  # get input
            s(memory, i + 1, simulation_input)
            di = 2
        elif opcode == 4:  # set output
            simulation_output = g(memory, i + 1, 0)
            di = 2
        elif opcode == 5:  # jump-if-true
            di = g(memory, i + 2, b) - i if g(memory, i + 1, c) != 0 else 3
        elif opcode == 6:  # jump-if-false
            di = g(memory, i + 2, b) - i if g(memory, i + 1, c) == 0 else 3
        elif opcode == 7:  # less than
            s(memory, i + 3, 1 if g(memory, i + 1, c) < g(memory, i + 2, b) else 0)
            di = 4
        elif opcode == 8:  # equals
            s(memory, i + 3, 1 if g(memory, i + 1, c) == g(memory, i + 2, b) else 0)
            di = 4

        i += di

    return simulation_output
