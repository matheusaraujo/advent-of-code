import re

def problem1(input):
    d, m = input[0].replace('\n', ''), {}
    
    for i in range(2, len(input)):
        f, l, r = re.findall(r'(.*) = \((.*),\s(.*)\)', input[i])[0]
        m[f] = [l, r]

    c, i, ans = 'AAA', 0, 0

    while(c != 'ZZZ'):
        c = m[c][0] if d[i] == 'L' else m[c][1]
        i = i + 1 if i < len(d) - 1 else 0
        ans += 1
        
    return ans