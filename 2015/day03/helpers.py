def move(x, y, m, v):
    if m == ">":
        x += 1
    elif m == "<":
        x -= 1
    elif m == "^":
        y += 1
    elif m == "v":
        y -= 1

    if (x, y) not in v:
        v[(x, y)] = True

    return x, y
