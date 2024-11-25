import re

LIMITS = "12 red, 13 green, 14 blue"


def extract_line(line):
    str_r = re.search(r"\d+(?= red)", line)
    str_g = re.search(r"\d+(?= green)", line)
    str_b = re.search(r"\d+(?= blue)", line)

    red = int(str_r.group()) if str_r is not None else 0
    green = int(str_g.group()) if str_g is not None else 0
    blue = int(str_b.group()) if str_b is not None else 0

    return [red, green, blue]


def extract_game(line):
    str_game = re.search(r"[Game ]\d+", line)
    game = int(str_game.group()) if str_game is not None else 0

    return game
