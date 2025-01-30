# brute force solution


def part1(puzzle_input):
    house = 1
    while sum_of_presents(house) < int(puzzle_input[0]):
        house += 1
    return house


def sum_of_presents(house):
    total = sum(d * 10 for d in range(1, int(house ** 0.5) + 1) if house % d == 0)
    for d in range(1, int(house ** 0.5) + 1):
        if house % d == 0:
            other = house // d
            if other != d:
                total += other * 10
    return total
