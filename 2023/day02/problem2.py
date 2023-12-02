from fixtures import extract_line

def problem2(lines):
    ans = 0
    for line in lines:
        games = line.split(';')
        r, g, b = 0, 0, 0

        for game in games:
            k = extract_line(game)
            r = max(r, k[0])
            g = max(g, k[1])
            b = max(b, k[2])

        o = r * g * b

        ans = ans + o

    return ans