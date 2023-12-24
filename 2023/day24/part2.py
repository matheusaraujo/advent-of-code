from sympy import solve, symbols


# pylint: disable=too-many-locals
def part2(puzzle_input):
    points = []

    for line in puzzle_input:
        pos, vel = line.split(" @ ")
        (x, y, z), (dx, dy, dz) = pos.split(", "), vel.split(", ")
        points.append([int(x), int(y), int(z), int(dx), int(dy), int(dz)])

    p, v, t = (symbols(f"{ch}(:3)") for ch in "pvt")
    print(p, v, t)

    equations = []
    for i in range(3):
        x, y, z, dx, dy, dz = (
            points[i][0],
            points[i][1],
            points[i][2],
            points[i][3],
            points[i][4],
            points[i][5],
        )
        equations.append(x + t[i] * dx - p[0] - v[0] * t[i])
        equations.append(y + t[i] * dy - p[1] - v[1] * t[i])
        equations.append(z + t[i] * dz - p[2] - v[2] * t[i])

    solution = solve(equations, (*p, *v, *t))
    print(solution)
    return sum(solution[0][:3])
