from helpers import extract_line


def part2(lines):
    ans = 0
    for line in lines:
        games = line.split(";")
        r_max, g_max, b_max = 0, 0, 0

        for game in games:
            red, green, blue = extract_line(game)
            r_max = max(red, r_max)
            g_max = max(green, g_max)
            b_max = max(blue, b_max)

        ans = ans + (r_max * g_max * b_max)

    return ans
