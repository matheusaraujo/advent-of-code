def solve(puzzle_input, equation):
    ans = 0

    for line in puzzle_input:
        dims = [int(i) for i in line.split("x")]
        dims.sort()
        [l, w, h] = dims

        ans = ans + equation(l, w, h)

    return ans
