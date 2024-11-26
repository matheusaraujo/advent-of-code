from helpers import IntCode


def part2(puzzle_input, single_input=2):
    program = [int(x) for x in puzzle_input[0].split(",")]
    computer = IntCode(program[:], [])

    return computer.run([single_input])
