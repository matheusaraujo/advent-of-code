def part1(puzzle_input):
    return puzzle_input.count("(") - puzzle_input.count(")")


if __name__ == "__main__":
    puzzle_input = input()
    answer = part1(puzzle_input)
    print(answer)
