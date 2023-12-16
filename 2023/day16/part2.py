from helpers import solve


def part2(contraption):
    ans, rows, cols = 0, len(contraption), len(contraption[0])

    for x in range(rows):
        ans = max(
            ans, solve(contraption, x, 0, "R"), solve(contraption, x, cols - 1, "L")
        )

    for y in range(cols):
        ans = max(
            ans, solve(contraption, 0, y, "D"), solve(contraption, rows - 1, y, "U")
        )

    return ans
