from helpers import Reindeer


def part2(puzzle_input):
    reindeers = [Reindeer(line) for line in puzzle_input]

    for t in range(1, 2504):
        for reindeer in reindeers:
            reindeer.position_at(t)
        max_distance = max(reindeer.position for reindeer in reindeers)
        for reindeer in reindeers:
            if reindeer.position == max_distance:
                reindeer.win_points()

    return max(reindeer.points for reindeer in reindeers)
