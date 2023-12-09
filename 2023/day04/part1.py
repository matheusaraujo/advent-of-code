def part1(puzzle_input):
    ans = 0
    for card in puzzle_input:
        numbers = card.split(":")[1].split("|")

        winning_numbers = [int(n) for n in numbers[0].split(" ") if len(n) > 0]
        my_numbers = [int(n) for n in numbers[1].split(" ") if len(n) > 0]

        cnt = sum(1 for n in my_numbers if n in winning_numbers)

        ans += 2 ** (cnt - 1) if cnt > 0 else 0

    return ans
