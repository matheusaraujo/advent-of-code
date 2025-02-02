from functools import reduce
from itertools import combinations
from operator import mul


def solve(data, num_groups):
    for i in range(1, len(data)):
        for c in combinations(data, i):
            if sum(c) == sum(data) // num_groups:
                return reduce(mul, c)
    return 0
