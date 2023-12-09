from helpers import extract_game, extract_line


def part1(lines, limits_line):
    r_max, g_max, b_max = extract_line(limits_line)

    ans = 0

    for line in lines:
        game_id = extract_game(line)
        games = line.split(";")

        valid = True

        for game in games:
            r, g, b = extract_line(game)

            if r > r_max or g > g_max or b > b_max:
                valid = False
                break

        if valid:
            ans = ans + game_id

    return ans
