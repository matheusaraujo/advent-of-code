def solve(puzzle_input, equation):
    ans = 0

    for line in puzzle_input:
        dims = [int(i) for i in line.split("x")]
        dims.sort()
        [length, width, height] = dims

        ans = ans + equation(length, width, height)

    return ans
