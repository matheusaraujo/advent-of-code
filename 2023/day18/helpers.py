# using shoelace formula
# https://en.wikipedia.org/wiki/Shoelace_formula
def calculate_area(c):
    area = 0
    if c[0] != c[-1]:
        c.append(c[0])

    for i in range(1, len(c)):
        x2, y2, x1, y1 = c[i][0], c[i][1], c[i - 1][0], c[i - 1][1]
        area += x1 * y2 - x2 * y1

    return abs(area) / 2


def calculate_perimeter(c):
    perimeter = 0
    for i in range(1, len(c)):
        x2, y2, x1, y1 = c[i][0], c[i][1], c[i - 1][0], c[i - 1][1]
        perimeter += abs(x2 - x1) + abs(y2 - y1)

    return perimeter


# from pick's theorem https://en.wikipedia.org/wiki/Pick%27s_theorem
# a = i + b / 2 - 1
#   a = area is given by _shoelace formula_
#   b = number of boundary points is given by _perimeter_
#   i = number of internal points is unknown
# therefore:
#   i = a - b / 2 + 1
# the answer for the problem is:
#   number of internal points (i) + number of boundary points (b)
# therefore:
#   i + b => a - b / 2 + 1 + b
#   a + b / 2 + 1
def solve(coords):
    a = calculate_area(coords)
    b = calculate_perimeter(coords)
    return a + b / 2 + 1
