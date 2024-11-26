def is_nice_string(line):
    v, r = 0, 0

    vowels = {"a", "e", "i", "o", "u"}
    forbidden = {"ab", "cd", "pq", "xy"}

    for idx, char in enumerate(line):
        if char in vowels:
            v += 1

        if idx < len(line) - 1:
            pair = line[idx : idx + 2]

            if pair in forbidden:
                return False
            if char == line[idx + 1]:
                r += 1

    return v > 2 and r > 0


def part1(puzzle_input):
    return sum(is_nice_string(line) for line in puzzle_input)
