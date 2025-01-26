from helpers import find_next_password


def part2(puzzle_input):
    return find_next_password(find_next_password(puzzle_input[0]))
