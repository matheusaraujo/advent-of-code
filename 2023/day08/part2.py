import re
from functools import reduce
from math import gcd


# least common multiple
def lcm(numbers):
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)


def part2(puzzle_input):
    d, m, c, i, ans = puzzle_input[0], {}, [], 0, []

    for j in range(2, len(puzzle_input)):
        f, l, r = re.findall(r"(.*) = \((.*),\s(.*)\)", puzzle_input[j])[0]
        m[f] = [l, r]
        if f.endswith("A"):
            c.append(f)

    for x in c:
        tmp_ans = 0
        while not x.endswith("Z"):
            x = m[x][0] if d[i] == "L" else m[x][1]
            i = i + 1 if i < len(d) - 1 else 0
            tmp_ans += 1
        ans.append(tmp_ans)

    return lcm(ans)
