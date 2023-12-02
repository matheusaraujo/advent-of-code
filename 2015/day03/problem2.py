def problem2(input):
    visited = {(0,0): True}
    ans, x1, y1, x2, y2 = 1, 0, 0, 0, 0

    for i in range(0, len(input), 2):
        m1, m2 = input[i], input[i+1]

        if m1 == '>': x1 = x1 + 1
        elif m1 == '<': x1 = x1 - 1
        elif m1 == '^': y1 = y1 + 1
        elif m1 == 'v': y1 = y1 - 1

        if not (x1, y1) in visited:
            ans = ans + 1
            visited[(x1, y1)] = True

        if m2 == '>': x2 = x2 + 1
        elif m2 == '<': x2 = x2 - 1
        elif m2 == '^': y2 = y2 + 1
        elif m2 == 'v': y2 = y2 - 1

        if not (x2, y2) in visited:
            ans = ans + 1
            visited[(x2, y2)] = True

    return ans