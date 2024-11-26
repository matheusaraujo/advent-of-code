import re


def part2(puzzle_input):
    n, numbers, ans, nid = len(puzzle_input), {}, 0, 0

    for i in range(0, n):
        for match in re.finditer(r"\d+", puzzle_input[i]):
            s, e = match.start(), match.end()
            for j in range(s, e):
                numbers[(i, j)] = (nid, int(puzzle_input[i][s:e]))
            nid += 1

    for i in range(0, n):
        for match in re.finditer(r"\*", puzzle_input[i]):
            s = match.start()

            positions = {
                (i, s - 1),
                (i, s + 1),
                (i - 1, s - 1),
                (i - 1, s),
                (i - 1, s + 1),
                (i + 1, s - 1),
                (i + 1, s),
                (i + 1, s + 1),
            }

            ns = []

            for p in positions:
                if p in numbers and not numbers[p] in ns:
                    ns.append(numbers[p])

            if len(ns) == 2:
                ans += ns[0][1] * ns[1][1]

    return ans
