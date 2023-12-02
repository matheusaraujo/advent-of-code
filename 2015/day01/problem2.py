def problem2(input):
    floor = 0
    for i, c in enumerate(input, start = 1):
        if c == '(': floor = floor + 1
        if c == ')': floor = floor - 1
        
        if floor == -1: return i
    return 0