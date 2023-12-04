import re

def problem2(input):
    cards = [1] * len(input)
    for card_number in range(0, len(input)):
        numbers = input[card_number].split(':')[1].split('|')
        winning_numbers = [int(n) for n in numbers[0].split(' ') if len(n) > 0]
        my_numbers = [int(n) for n in numbers[1].split(' ') if len(n) > 0]
        
        cnt = sum(1 for n in my_numbers if (n in winning_numbers))

        for i in range(0, cnt):
            cards[card_number+i+1] += cards[card_number]

    return sum(cards)