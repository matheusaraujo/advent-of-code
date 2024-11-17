def part2(puzzle_input):
    input = puzzle_input[0]
    diff, result = len(input) // 2, 0

    for i in range(len(input)):
        if input[i] == input[(i + diff) % len(input)]:
            result += int(input[i])

    return result

