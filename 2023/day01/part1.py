import re


def part1(lines):
    ans = 0

    for line in lines:
        digits = re.findall(r"\d", line)
        ans = ans + 10 * int(digits[0]) + int(digits[-1])

    return ans
