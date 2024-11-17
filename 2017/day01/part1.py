def part1(puzzle_input):
    result, input = 0, puzzle_input[0]
    for i in range(len(input)):
        if input[i] == input[i - 1]:
            result += int(input[i])

    return result
