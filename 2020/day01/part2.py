def part2(puzzle_input):
    puzzle_input, n = sorted(list(map(int, puzzle_input))), len(puzzle_input)

    for i in range(n):
        target = 2020 - puzzle_input[i]
        left, right = i + 1, n - 1

        while left < right:
            current_sum = puzzle_input[left] + puzzle_input[right]
            if current_sum == target:
                return puzzle_input[i] * puzzle_input[left] * puzzle_input[right]
            if current_sum < target:
                left += 1
            else:
                right -= 1

    return None
