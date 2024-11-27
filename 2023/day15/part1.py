from helpers import hashing


def part1(puzzle_input):
    return sum(hashing(s) for s in puzzle_input[0].split(","))
