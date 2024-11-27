from helpers import solve


def is_reflection(arr, x):
    dx = 0
    while x + dx < len(arr) and x - dx > 0:
        if arr[x + dx] != arr[x - dx - 1]:
            return False
        dx += 1
    return True


def part1(puzzle_input):
    return solve(puzzle_input, is_reflection)
