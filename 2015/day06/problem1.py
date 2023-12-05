import re

from node import Node

def extract_input(line):
    match = re.findall(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line)[0]
    return match[0], int(match[1]), int(match[2]), int(match[3]), int(match[4]) 


def solve(a1):
    print('input', a1)
    
    if len(a1) == 1: return a1
    
    a2 = []

    for i in range(1, len(a1)):
        if a1[i][0] < a1[i-1][1]:
            a2.append((a1[i-1][0], a1[i][0]-1, a1[i-1][2]))
            a2.append(a1[i])
            a2.append((a1[i][1]+1,a1[i-1][1], a1[i-1][2]))

    return a2

def problem1(input, N):

    print('result', solve([(0, 7, 0)]))
    print('result', solve([(0, 7, 0), (4, 5, 1)]))
    print('result', solve([(0, 7, 0), (1, 2, 1), (3, 4, 1)]))
    

    return 3

                
                
                