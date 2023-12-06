import re

def extract_numbers(s):
    return [int(n) for n in re.findall(r'\d+', s)]

def problem1(input):
    times, distances, ans = extract_numbers(input[0]), extract_numbers(input[1]), 1
    
    for i in range(0, len(times)):
        cnt = 0
        for t in range(0, times[i]):
            if t * (times[i] - t) > distances[i]: 
                cnt += 1
            elif cnt > 0: 
                break
        ans *= cnt
            
    return ans