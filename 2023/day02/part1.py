from helpers import LIMITS, extract_game, extract_line


def part1(lines):
    r_max, g_max, b_max = extract_line(LIMITS)

    ans = 0

    for line in lines:
        game_id = extract_game(line)
        games = line.split(";")

        valid = True

        for game in games:
            red, green, blue = extract_line(game)

            if red > r_max or green > g_max or blue > b_max:
                valid = False
                break

        if valid:
            ans = ans + game_id

    return ans
