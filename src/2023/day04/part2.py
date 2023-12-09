def part2(puzzle_input):
    cards = [1] * len(puzzle_input)

    for card_number, card in enumerate(puzzle_input):
        numbers = card.split(":")[1].split("|")
        winning_numbers = [int(n) for n in numbers[0].split(" ") if len(n) > 0]
        my_numbers = [int(n) for n in numbers[1].split(" ") if len(n) > 0]

        cnt = sum(1 for n in my_numbers if n in winning_numbers)

        for i in range(0, cnt):
            cards[card_number + i + 1] += cards[card_number]

    return sum(cards)
