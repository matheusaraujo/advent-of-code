from fixtures import extract_line

def problem2(lines):
    ans = 0
    for line in lines:
        games = line.split(';')
        rmax, gmax, bmax = 0, 0, 0

        for game in games:
            r, g, b = extract_line(game)
            rmax = max(r, rmax)
            gmax = max(g, gmax)
            bmax = max(b, bmax)

        ans = ans + (rmax * gmax * bmax)

    return ans