from math import ceil, floor, sqrt


def get_integer_roots(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)

    return floor(min(x1, x2)), ceil(max(x1, x2))
