from helpers import count_combinations


def part2(puzzle_input):
    return next(
        count
        for _, count in count_combinations([int(x) for x in puzzle_input], 150)
        if count > 0
    )
