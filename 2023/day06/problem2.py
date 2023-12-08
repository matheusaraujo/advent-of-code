import re

from helpers import get_integer_roots

def problem2(input):
    time = int(input[0].replace('Time: ', '').replace(' ', ''))
    distance = int(input[1].replace('Distance: ', '').replace(' ', ''))
    
    # Tt - t^2 > D
    # - t^2 + Tt - D > 0
    x1, x2 = get_integer_roots(-1, time, -distance)
        
    return x2 - x1 - 1
