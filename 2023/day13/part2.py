from helpers import solve


# https://www.geeksforgeeks.org/check-whether-two-numbers-differ-one-bit-position/
def is_one_bit_difference(n1, n2):
    xor = n1 ^ n2
    return xor != 0 and (xor & (xor - 1)) == 0


def is_reflection(arr, x):
    dx, flag = 0, 0

    while x + dx < len(arr) and x - dx > 0:
        if arr[x + dx] != arr[x - dx - 1]:
            if flag > 0 or not is_one_bit_difference(arr[x + dx], arr[x - dx - 1]):
                return False
            flag = 1
        dx += 1

    return flag == 1


def part2(puzzle_input):
    return solve(puzzle_input, is_reflection)
