from helpers import solve


def is_one_bit_difference(num1, num2):
    xor = num1 ^ num2
    return xor != 0 and (xor & (xor - 1)) == 0


def is_reflection(arr, x):
    dx, c = 0, 0

    while x + dx < len(arr) and x - dx > 0:
        if arr[x + dx] != arr[x - dx - 1]:
            if c > 0 or not is_one_bit_difference(arr[x + dx], arr[x - dx - 1]):
                return False
            c = 1
        dx += 1

    return c == 1


def part2(puzzle_input):
    return solve(puzzle_input, is_reflection)
