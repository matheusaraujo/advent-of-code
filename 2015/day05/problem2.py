def problem2_solve(input):
    r1, r2, n = 0, 0, len(input)

    for idx in range(n - 2):
        if input[idx] == input[idx + 2]: r1 += 1
        
        tmp = input[idx:idx + 2]
        if input.find(tmp, idx + 2) != -1: r2 += 1

    return r1 > 0 and r2 > 0

def problem2(input):
    ans = 0
    for line in input:
        if problem2_solve(line): ans += 1
    return ans