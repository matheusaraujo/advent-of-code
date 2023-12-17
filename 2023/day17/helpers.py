import heapq

right = (0, 1)
down = (1, 0)
left = (0, -1)
up = (-1, 0)

directions = [right, down, left, up]


def solve(grid, min_dc, max_dc):
    v = {}
    q = [(0, 0, 0, right, 1), (0, 0, 0, down, 1)]

    while q:
        c, x, y, d, dc = heapq.heappop(q)

        if (x, y, d, dc) in v:
            continue

        v[(x, y, d, dc)] = True

        nx, ny = x + d[0], y + d[1]

        if not 0 <= nx < len(grid) or not 0 <= ny < len(grid[0]):
            continue

        nc = c + grid[nx][ny]

        if nx == len(grid) - 1 and ny == len(grid[0]) - 1 and min_dc <= dc <= max_dc:
            return nc

        for dd in directions:
            if d[0] + dd[0] == 0 and d[1] + dd[1] == 0:
                continue
            ndc = dc + 1 if dd == d else 1
            if ndc > max_dc or (dc < min_dc and dd != d):
                continue

            heapq.heappush(q, (nc, nx, ny, dd, ndc))

    return None
