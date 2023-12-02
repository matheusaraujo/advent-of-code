def problem2(input):
    ans = 0
    
    for line in input:
        dims =  [int(i) for i in line.split('x')]
        dims.sort()
        [l, w, h] = dims

        ans = ans + l * w * h + 2 * (l + w)

    return ans