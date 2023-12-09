def part1(puzzle_input):
    ans = 0

    for line in puzzle_input:
        dims = [int(i) for i in line.split("x")]
        dims.sort()
        [l, w, h] = dims

        ans = ans + 2 * l * w + 2 * l * h + 2 * w * h + l * w

    return ans
