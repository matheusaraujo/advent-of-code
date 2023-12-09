def is_nice_string(line):
    r1, r2, n = 0, 0, len(line)

    for idx in range(n - 2):
        if line[idx] == line[idx + 2]:
            r1 += 1

        tmp = line[idx : idx + 2]
        if line.find(tmp, idx + 2) != -1:
            r2 += 1

    return r1 > 0 and r2 > 0


def part2(puzzle_input):
    return sum(is_nice_string(line) for line in puzzle_input)
