def problem2(input):
    floor = 0
    for f in range(0, len(input)):
        if input[f] == '(':
            floor = floor + 1
        if input[f] == ')':
            floor = floor - 1
        
        if floor == -1:
            return f + 1
    return 0