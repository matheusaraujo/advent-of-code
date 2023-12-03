import re

def problem2(input):
    N, numbers, ans, nid = len(input), {}, 0, 0

    for i in range(0, N):
        for match in re.finditer(r'\d+', input[i]):
            s, e = match.start(), match.end()
            for j in range(s, e):
                numbers[(i, j)] = (nid, int(input[i][s:e]))
            nid += 1

    for i in range(0, N):
        for match in re.finditer(r'\*', input[i]):
            s = match.start()

            positions = {
                (i, s-1), (i, s+1),
                (i-1, s-1), (i-1, s), (i-1, s+1),
                (i+1, s-1), (i+1, s), (i+1, s+1),
            }
            
            ns = []
            
            for p in positions:
                if p in numbers and not numbers[p] in ns: 
                    ns.append(numbers[p])

            if len(ns) == 2:
                ans += ns[0][1] * ns[1][1]

    return ans
    