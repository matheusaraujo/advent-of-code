from int_code import IntCode


def part2(puzzle_input, single_input):
    program = [int(x) for x in puzzle_input.split(",")]
    computer = IntCode(program[:], [])

    return computer.execute([single_input])
