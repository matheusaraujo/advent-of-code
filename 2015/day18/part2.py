from helpers import get_light_next_state, simulate


def part2(grid):
    grid[0] = "#" + grid[0][1:-1] + "#"
    grid[-1] = "#" + grid[-1][1:-1] + "#"
    return simulate(grid, 100, get_light_next_state_with_stuck_corners)


def get_light_next_state_with_stuck_corners(i, j, grid):
    if (i, j) in [
        (0, 0),
        (0, len(grid[0]) - 1),
        (len(grid) - 1, 0),
        (len(grid) - 1, len(grid[0]) - 1),
    ]:
        return "#"
    return get_light_next_state(i, j, grid)
