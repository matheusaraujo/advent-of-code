from helpers import Boss, Player, min_mana_to_win


def part2(puzzle_input):
    return min_mana_to_win(Player(50, 500), Boss.parse(puzzle_input), hard_mode=True)
