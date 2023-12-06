import re

def problem2(input):
    time = int(input[0].replace('Time: ', '').replace(' ', ''))
    distance = int(input[1].replace('Distance: ', '').replace(' ', ''))
    ans = 0
    
    for t in range(0, time):
        if t * (time - t) > distance:
            ans += 1
        elif ans > 0:
            break
            
    return ans
