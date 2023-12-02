from fixtures import extract_line, extract_game

def problem1(lines, limits_line):
    limits = extract_line(limits_line)

    ans = 0

    for line in lines:
        r, g, b = 0, 0, 0
        game_id = extract_game(line)
        games = line.split(';')

        flag = True

        for game in games:
            k = extract_line(game)
            r, g, b = k[0], k[1], k[2]
        
            if r > limits[0] or g > limits[1] or b > limits[2]:
                flag = False

        if flag:
            ans = ans + game_id

    return ans
