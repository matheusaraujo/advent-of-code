import random

from sympy import solve, symbols


# for a given hailstone n with position (x, y, z) and velocity (dx, dy, dz)
# and the rock with initial position (x0, y0, z0) and velocity (dx0, dy0, dz0)
# they will collide at Tn:
# { x0 + Tn * dx0 = x + Tn * dx
# { y0 + Tn * dy0 = y + Tn * yx
# { z0 + Tn * dz0 = z + Tn * zx
# therefore:
# { x + Tn * dx - x0 - dx0 * Tn = 0
# { y + Tn * dy - y0 - dy0 * Tn = 0
# { z + Tn * dz - z0 - dz0 * Tn = 0
# for each hailstone we have 3 equations and 7 variables
#   Tn and rock position and velocity (6 variables)
# so if we have 3 hailstone, we have 9 equations and 9 variables
# (3 for rock initial position, 3 for rock velocity and 3 Tn, 1 for each hailstone)
# it's enough to do the maths
# instead of manually implement the system solver, it was used `sympy`
# after all, it's christmas
# pylint: disable=too-many-locals
def part2(puzzle_input):
    number_of_points_to_use, points = min(3, len(puzzle_input)), []
    points_to_use = random.sample(range(0, len(puzzle_input)), number_of_points_to_use)

    for i in points_to_use:
        pos, vel = puzzle_input[i].split(" @ ")
        (x, y, z), (dx, dy, dz) = pos.split(", "), vel.split(", ")
        points.append([int(x), int(y), int(z), int(dx), int(dy), int(dz)])

    x0, y0, z0, dx0, dy0, dz0 = symbols("x0 y0 z0 dx0 dy0 dz0")
    t = symbols(f"t(:{number_of_points_to_use})")

    equations = []
    for i, point in enumerate(points):
        x, y, z, dx, dy, dz = point
        equations.append(x + t[i] * dx - x0 - dx0 * t[i])
        equations.append(y + t[i] * dy - y0 - dy0 * t[i])
        equations.append(z + t[i] * dz - z0 - dz0 * t[i])

    x0, y0, z0 = solve(equations, (x0, y0, z0, dx0, dy0, dz0, *t))[0][:3]

    return x0 + y0 + z0
