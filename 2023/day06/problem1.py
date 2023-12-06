import re

from helpers import get_integer_roots

def extract_numbers(s):
    return [int(n) for n in re.findall(r'\d+', s)]

def problem1(input):
    times, distances, ans = extract_numbers(input[0]), extract_numbers(input[1]), 1
    
    for i in range(0, len(times)):
        # Tt - t^2 > D
        # - t^2 + Tt - D > 0
        x1, x2 = get_integer_roots(-1, times[i], -distances[i])
        ans *= (x2 - x1 - 1)
            
    return ans