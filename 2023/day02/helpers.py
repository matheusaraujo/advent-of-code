import re


def extract_line(line):
    sr = re.search(r"\d+(?= red)", line)
    sg = re.search(r"\d+(?= green)", line)
    sb = re.search(r"\d+(?= blue)", line)

    r = int(sr.group()) if sr is not None else 0
    g = int(sg.group()) if sg is not None else 0
    b = int(sb.group()) if sb is not None else 0

    return [r, g, b]


def extract_game(line):
    sg = re.search(r"[Game ]\d+", line)
    g = int(sg.group()) if sg is not None else 0

    return g
