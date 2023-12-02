def move(x, y, move, visited):
    if move == '>': x += 1
    elif move == '<': x -= 1
    elif move == '^': y += 1
    elif move == 'v': y -= 1

    if (x, y) not in visited:
        visited[(x, y)] = True

    return x, y

def problem2(input):
    visited = {(0,0): True}
    x1, y1, x2, y2 = 0, 0, 0, 0

    for i in range(0, len(input), 2):
        m1, m2 = input[i], input[i+1]

        x1, y1 = move(x1, y1, m1, visited)
        x2, y2 = move(x2, y2, m2, visited)

    return len(visited)