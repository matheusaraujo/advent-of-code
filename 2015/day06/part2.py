import re


def part2(puzzle_input):
    m = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in puzzle_input:
        ma = re.findall(r"(.* )(\d+),(\d+) through (\d+),(\d+)", line)[0]
        op, x1, y1, x2, y2 = (
            ma[0].strip(),
            int(ma[1]),
            int(ma[2]),
            int(ma[3]),
            int(ma[4]),
        )

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if op == "turn on":
                    m[i][j] += 1
                elif op == "turn off":
                    m[i][j] = max(m[i][j] - 1, 0)
                else:
                    m[i][j] += 2

    return sum(map(sum, m))
