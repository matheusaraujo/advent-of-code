import json


def sum_numbers(data):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(sum_numbers(item) for item in data)
    if isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum(sum_numbers(value) for value in data.values())

    return 0


def part2(puzzle_input):
    return sum_numbers(json.loads(puzzle_input[0]))
