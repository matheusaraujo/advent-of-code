# brute force solution


def part2(puzzle_input):
    house = 1
    while sum_of_presents(house) < int(puzzle_input[0]):
        house += 1
    return house


def sum_of_presents(house):
    total = 0
    for d in range(1, int(house ** 0.5) + 1):
        if house % d == 0:
            if d * 50 >= house:
                total += d * 11
            other = house // d
            if other != d and other * 50 >= house:
                total += other * 11
    return total
