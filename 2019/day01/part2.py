from math import floor


def calculate_module_fuel(mass):
    m = floor(mass / 3) - 2
    return m + calculate_module_fuel(m) if m > 0 else 0


def part2(puzzle_input):
    return sum(calculate_module_fuel(int(mass)) for mass in puzzle_input)
