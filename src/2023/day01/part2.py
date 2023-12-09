import re


def get_digit(value):
    numbers_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    return numbers_dict[value] if value in numbers_dict else int(value)


def part2(lines):
    ans = 0

    for line in lines:
        digits = re.findall(
            r"(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))",
            line,
        )
        ans = ans + 10 * int(get_digit(digits[0])) + int(get_digit(digits[-1]))

    return ans
