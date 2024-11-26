from helpers import IntCode


def part1(puzzle_input, single_input=1):
    program = [int(x) for x in puzzle_input[0].split(",")]

    computer = IntCode(program[:], [single_input])

    outputs = []

    while not computer.halted():
        output = computer.run([])
        if not computer.halted():
            outputs.append(str(output))

    return ",".join(outputs)
