def parse_input(puzzle_input):
    left = []
    right = []

    for line in puzzle_input:
        parts = line.split("   ")
        left.append(int(parts[0]))
        right.append(int(parts[1]))

    left.sort()
    right.sort()

    return left, right
