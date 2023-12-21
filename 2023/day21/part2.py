from helpers import solve


# for part2, the simulation is impractical due to the number of steps:
#    26501365 = 65 + (131 * 202300)
# so i ran the simulation for first 500 steps and looked for the pattern empirically
# the input is a grid 131x131 and the starting point is exactly on the middle (65)
# based on that, we have for every n repetition of the map S = 65 + (131 * n) steps
# so we can calculate the first 3 n elements, n_0, n_1, n_2
# and use a simplified version of lagrange to extrapolate this equation until n_s
# for x = [0, 1, 2] and y = [y0, y1, u2] we can reduce lagrange to:
#    f(x) = (x^2 - 3x + 2) * y0/2 - (x^2 - 2x) * y1 + (x^2 - x) * y2/2
#    f(x) = x^2 (y0/2 - y1 + y2/2) + x (-3 * y0/2 + 2 * y1 - y2/2) + y0
#  therefore:
#    a = y0 / 2 - y1 + y2 / 2
#    b = -3 * y0/2 + 2 * y1 - y2/2
#    c = y0
def part2(_map, steps):
    points = [65 + 131 * i for i in range(3)]
    n_s = (steps - 65) / 131

    y0, y1, y2 = [solve(_map, p) for p in points]

    # lagrange
    a = y0 / 2 - y1 + y2 / 2
    b = -3 * y0 / 2 + 2 * y1 - y2 / 2
    c = y0

    return a * n_s**2 + b * n_s + c
