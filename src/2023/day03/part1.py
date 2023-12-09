import re


def part1(puzzle_input):
    n, symbols, ans = len(puzzle_input), {}, 0

    for i in range(0, n):
        for match in re.finditer(r"[^\d|.|\n]", puzzle_input[i]):
            s, e = match.start(), match.end()
            symbols[(i, s)] = puzzle_input[i][s:e]

    for i in range(0, n):
        for match in re.finditer(r"\d+", puzzle_input[i]):
            s, e = match.start(), match.end()
            n = int(puzzle_input[i][s:e])

            if (i, s - 1) in symbols or (i, e) in symbols:
                ans += n
            else:
                for k in range(s - 1, e + 1):
                    if (i - 1, k) in symbols or (i + 1, k) in symbols:
                        ans += n
                        break

    return ans
