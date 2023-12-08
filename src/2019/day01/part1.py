from math import floor


def calculate_module_fuel(mass):
    return floor(mass / 3) - 2


def part1(puzzle_input):
    return sum(calculate_module_fuel(int(mass)) for mass in puzzle_input)
