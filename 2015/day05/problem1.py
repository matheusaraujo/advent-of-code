def problem1_solve(input):
    v, r = 0, 0

    vowels = {'a', 'e', 'i', 'o', 'u'}
    forbidden = {'ab', 'cd', 'pq', 'xy'}
    
    for idx, ch in enumerate(input):
        if ch in vowels: v += 1
        
        if idx < len(input) - 1:
            pair = input[idx:idx+2]
            
            if pair in forbidden: return False
            if ch == input[idx + 1]: r += 1

    return v > 2 and r > 0

def problem1(input):
    ans = 0
    for line in input:
        if problem1_solve(line): ans += 1
    return ans