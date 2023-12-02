from fixtures import extract_line, extract_game

def problem1(lines, limits_line):
    rmax, gmax, bmax = extract_line(limits_line)

    ans = 0

    for line in lines:
        game_id = extract_game(line)
        games = line.split(';')

        valid = True

        for game in games:
            r, g, b = extract_line(game)
            
            if r > rmax or g > gmax or b > bmax:
                valid = False
                break

        if valid:
            ans = ans + game_id

    return ans
