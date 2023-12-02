def problem1(input):
    visited = {(0,0): True}
    ans, x, y = 1, 0, 0
    
    for move in input:
        if move == '>': x = x + 1
        elif move == '<': x = x - 1
        elif move == '^': y = y + 1
        elif move == 'v': y = y - 1
        
        if not (x, y) in visited:
            ans = ans + 1
            visited[(x, y)] = True

    return ans