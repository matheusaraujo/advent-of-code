from helpers import extract_line


def part2(lines):
    ans = 0
    for line in lines:
        games = line.split(";")
        r_max, g_max, b_max = 0, 0, 0

        for game in games:
            r, g, b = extract_line(game)
            r_max = max(r, r_max)
            g_max = max(g, g_max)
            b_max = max(b, b_max)

        ans = ans + (r_max * g_max * b_max)

    return ans
