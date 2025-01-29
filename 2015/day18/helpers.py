def simulate(grid, steps, eval_fn):
    for _ in range(steps):
        grid = [
            [eval_fn(i, j, grid) for j in range(len(grid[0]))] for i in range(len(grid))
        ]

    return sum(row.count("#") for row in grid)


def get_neighbors_on(i, j, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(
        1
        for di, dj in directions
        if 0 <= i + di < len(grid)
        and 0 <= j + dj < len(grid[0])
        and grid[i + di][j + dj] == "#"
    )


def get_light_next_state(i, j, grid):
    neighbors_on = get_neighbors_on(i, j, grid)
    if grid[i][j] == "#":
        return "#" if neighbors_on in (2, 3) else "."
    return "#" if neighbors_on == 3 else "."
