from int_code import IntCode


def part1(puzzle_input, single_input):
    program = [int(x) for x in puzzle_input.split(",")]

    computer = IntCode(program[:], [single_input])

    outputs = []

    while not computer.halt:
        output = computer.execute([])
        if not computer.halt:
            outputs.append(str(output))

    return ",".join(outputs)
