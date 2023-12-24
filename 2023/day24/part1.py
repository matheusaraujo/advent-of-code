# x1 + t1 * dx1 = xf1, y1 + t1 * dy1 = yf1
# x2 + t2 * dx2 = xf2, y2 + t2 * dy2 = yf2
# for xf1 = xf2 and yf1 = yf2
# { x1 + t1 * dx1 = x2 + t2 * dx2
# { y1 + t1 * yx1 = y2 + t2 * yx2
# therefore
# { t1 * dx1 - t2 * dx2 = x2 - x1
# { t1 * dy1 - t2 * dy2 = y2 - y1
# or
# | A | x |T| = |B|
# | dx1  -dx2 | x | t1 | = | x2 - x1 |
# | dy1  -dy2 |   | t2 | = | y2 - y1 |
# using Cramer's rule https://en.wikipedia.org/wiki/Cramer%27s_rule
# det (A) =  dx1 * (-dy2) - (-dx2) * dy1
# det t_1 = (x2 - x1) * (-dy2) - (-dx2) * (y2 - y1)
# det t_2 = dx1 * (y2 - y1) - (x2 - x1) * dy1
# t_1 = det t_1 / det (A)
# t_2 = det t_2 / det (A)


# pylint: disable=too-many-arguments, too-many-locals
def will_intersect(x1, dx1, y1, dy1, x2, dx2, y2, dy2, lim_min, lim_max):
    det = dx1 * (-dy2) - (-dx2) * dy1
    det_t1 = (x2 - x1) * (-dy2) - (-dx2) * (y2 - y1)
    det_t2 = dx1 * (y2 - y1) - (x2 - x1) * dy1

    if det == 0:  # parallel
        return False

    t1 = det_t1 / det
    t2 = det_t2 / det

    if t1 < 0 or t2 < 0:  # past
        return False

    x1f = x1 + dx1 * t1
    y1f = y1 + dy1 * t1

    x2f = x2 + dx2 * t2
    y2f = y2 + dy2 * t2

    return (
        lim_min <= x1f <= lim_max
        and lim_min <= y1f <= lim_max
        and lim_min <= x2f <= lim_max
        and lim_min <= y2f <= lim_max
    )


def part1(puzzle_input, lim_min, lim_max):
    points = []

    for line in puzzle_input:
        pos, vel = line.split(" @ ")
        x, y, _ = pos.split(", ")
        dx, dy, _ = vel.split(", ")
        points.append((int(x), int(dx), int(y), int(dy)))

    ans = 0
    for i, pi in enumerate(points):
        for j in range(i + 1, len(points)):
            ans += will_intersect(*pi, *points[j], lim_min, lim_max)

    return ans
