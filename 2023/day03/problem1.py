import re

def problem1(input):
    N, symbols, ans = len(input), {}, 0
    
    for i in range(0, N):
        for match in re.finditer(r'[^\d|.|\n]', input[i]):
            s, e = match.start(), match.end()
            symbols[(i, s)] = input[i][s:e]

    for i in range(0, N):
        for match in re.finditer(r'\d+', input[i]):
            s, e = match.start(), match.end()
            n = int(input[i][s:e])

            if (i, s-1) in symbols or (i, e) in symbols:
                ans += n
            else:
                for k in range(s-1, e+1):
                    if (i-1, k) in symbols or (i+1, k) in symbols:
                        ans += n
                        break
    
    return ans