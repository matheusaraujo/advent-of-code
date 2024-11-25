def part2(puzzle_input):
    result, seen = 0, {0}

    while True:
        for line in puzzle_input:
            result += int(line)
            if result in seen:
                return result
            seen.add(result)
