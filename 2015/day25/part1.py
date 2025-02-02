def part1(puzzle_input):
    puzzle_input = puzzle_input[0].replace(",", "").replace(".", "").split(" ")
    row, column = int(puzzle_input[-3]), int(puzzle_input[-1])
    return solve(row, column)


def solve(row, column):
    first_code = 20151125
    code_count = sum(range(row + column - 1)) + column
    cur_code = first_code
    for _ in range(code_count - 1):
        cur_code = (cur_code * 252533) % 33554393
    return cur_code
