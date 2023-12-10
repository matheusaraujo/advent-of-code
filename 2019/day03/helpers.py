MOVES = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}


def move(w, f):
    x, y, k = 0, 0, 0
    for m in w:
        for _ in range(int(m[1:])):
            x += MOVES[m[0]][0]
            y += MOVES[m[0]][1]
            k += 1
            f(x, y, k)
