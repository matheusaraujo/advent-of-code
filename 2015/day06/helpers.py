import re


def extract_input(line):
    ma = re.findall(r"(.* )(\d+),(\d+) through (\d+),(\d+)", line)[0]
    op, x1, y1, x2, y2 = (
        ma[0].strip(),
        int(ma[1]),
        int(ma[2]),
        int(ma[3]),
        int(ma[4]),
    )
    return (op, x1, y1, x2, y2)


def solve(puzzle_input, turnon, turnoff, toggle):
    m = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in puzzle_input:
        op, x1, y1, x2, y2 = extract_input(line)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if op == "turn on":
                    m[i][j] = turnon(m[i][j])
                elif op == "turn off":
                    m[i][j] = turnoff(m[i][j])
                else:
                    m[i][j] = toggle(m[i][j])

    return sum(map(sum, m))
