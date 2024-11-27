def is_valid(a, b):
    c, bb = 0, []
    for x in a:
        if x == "#":
            c += 1
        elif c > 0:
            bb.append(c)
            c = 0
    if c > 0:
        bb.append(c)
    return bb == b


def brute_force(a, b, i):
    if i == len(a):
        return is_valid(a, b)
    if a[i] != "?":
        return brute_force(a, b, i + 1)

    a1, a2 = a[:], a[:]
    a1[i], a2[i] = "#", "."
    return brute_force(a1, b, i + 1) + brute_force(a2, b, i + 1)


def count_arrangement(line):
    line = line.split(" ")
    a, b = list(line[0]), [int(x) for x in line[1].split(",")]
    return brute_force(a, b, 0)


def part1(puzzle_input):
    return sum(count_arrangement(line) for line in puzzle_input)
