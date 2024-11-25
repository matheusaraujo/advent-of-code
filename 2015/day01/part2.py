def part2(puzzle_input):
    floor = 0
    for i, char in enumerate(puzzle_input[0], start=1):
        if char == "(":
            floor = floor + 1
        if char == ")":
            floor = floor - 1

        if floor == -1:
            return i
    return 0
