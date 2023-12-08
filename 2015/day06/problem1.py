import re

def problem1(input):
    m = [[0 for x in range(1000)] for y in range(1000)]

    for line in input:
        ma = re.findall(r'(.* )(\d+),(\d+) through (\d+),(\d+)', line)[0]
        op, x1, y1, x2, y2 = ma[0].strip(), int(ma[1]), int(ma[2]), int(ma[3]), int(ma[4])

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if op == 'turn on': m[i][j] = 1
                elif op == 'turn off': m[i][j] = 0
                else: m[i][j] = 1 if m[i][j] == 0 else 0

    return sum(map(sum,m))