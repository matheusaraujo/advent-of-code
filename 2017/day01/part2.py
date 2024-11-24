def part2(puzzle_input):
    digits = puzzle_input[0]
    diff, result = len(digits) // 2, 0

    for i, _ in enumerate(digits):
        if digits[i] == digits[(i + diff) % len(digits)]:
            result += int(digits[i])

    return result
