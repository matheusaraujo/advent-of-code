def part2(puzzle_input):
    floor = 0
    for i, c in enumerate(puzzle_input, start=1):
        if c == "(":
            floor = floor + 1
        elif c == ")":
            floor = floor - 1

        if floor == -1:
            return i
    return 0
