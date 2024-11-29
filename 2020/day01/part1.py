def part1(puzzle_input):
    puzzle_input, hist = map(int, puzzle_input), set()
    for i in puzzle_input:
        hist.add(i)
        if 2020 - i in hist:
            return i * (2020 - i)
    return None
