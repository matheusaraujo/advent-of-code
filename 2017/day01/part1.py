def part1(puzzle_input):
    result, digits = 0, puzzle_input[0]
    for i in range(len(digits)):
        if digits[i] == digits[i - 1]:
            result += int(digits[i])

    return result
