import re


def part1(puzzle_input):
    d, m, c, i, ans = puzzle_input[0], {}, "AAA", 0, 0

    for j in range(2, len(puzzle_input)):
        f, l, r = re.findall(r"(.*) = \((.*),\s(.*)\)", puzzle_input[j])[0]
        m[f] = [l, r]

    while c != "ZZZ":
        c = m[c][0] if d[i] == "L" else m[c][1]
        i = i + 1 if i < len(d) - 1 else 0
        ans += 1

    return ans
