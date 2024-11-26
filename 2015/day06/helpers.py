import re


def extract_input(line):
    match = re.findall(r"(.* )(\d+),(\d+) through (\d+),(\d+)", line)[0]
    instruction, x1, y1, x2, y2 = (
        match[0].strip(),
        int(match[1]),
        int(match[2]),
        int(match[3]),
        int(match[4]),
    )
    return (instruction, x1, y1, x2, y2)


def solve(puzzle_input, turnon, turnoff, toggle):
    m = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in puzzle_input:
        instruction, x1, y1, x2, y2 = extract_input(line)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if instruction == "turn on":
                    m[i][j] = turnon(m[i][j])
                elif instruction == "turn off":
                    m[i][j] = turnoff(m[i][j])
                else:
                    m[i][j] = toggle(m[i][j])

    return sum(map(sum, m))
