from helpers import get_light_next_state, simulate


def part1(grid):
    return simulate(grid, 100, get_light_next_state)
