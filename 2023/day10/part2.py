from helpers import find_longest_cycle


def map_to_edges(path, s):
    edges, last = [], path[0]
    for x in range(1, len(path)):
        z, y = path[x][0], path[x][1]
        if s[z][y] not in "|-":
            edges.append([last, (z, y)])
            last = (z, y)

    edges.append([last, (path[0][0], path[0][1])])
    return edges


def is_inside_polygon(xp, yp, edges):
    cnt = 0
    for edge in edges:
        (x1, y1), (x2, y2) = edge
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp - y1) / (y2 - y1)) * (x2 - x1):
            cnt += 1
    return cnt % 2 == 1


# Using Ray Casting Algorithm: https://en.wikipedia.org/wiki/Point_in_polygon
def part2(puzzle_input):
    (path, s), edges = find_longest_cycle(puzzle_input), []

    edges = map_to_edges(path, s)

    count_inside = sum(
        1
        for x in range(len(s))
        for y in range(len(s[0]))
        if (x, y) not in path and is_inside_polygon(x, y, edges)
    )

    return count_inside
