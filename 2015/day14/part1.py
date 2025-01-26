from helpers import Reindeer


def part1(puzzle_input):
    return max(
        reindeer.position_at(2503)
        for reindeer in [Reindeer(line) for line in puzzle_input]
    )
