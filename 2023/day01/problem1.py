import re
import sys

ans = 0

for line in sys.stdin:
    digits = re.findall(r'\d', line)
    ans = ans + 10 * int(digits[0]) + int(digits[-1])

print(ans)
