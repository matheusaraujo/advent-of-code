from itertools import combinations

inventory = {
    "weapons": [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0),
    ],
    "armor": [
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5),
    ],
    "rings": [
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ],
}

ring_combinations = (
    [()]
    + [(r,) for r in inventory["rings"][1:]]
    + list(combinations(inventory["rings"][1:], 2))
)


# pylint: disable=too-few-public-methods
class Character:
    def __init__(self, damage=0, armor=0, hit_points=0, puzzle_input=None):
        self.damage = damage
        self.armor = armor
        self.hit_points = hit_points

        if puzzle_input:
            self.damage = int(puzzle_input[1].split(": ")[1])
            self.armor = int(puzzle_input[2].split(": ")[1])
            self.hit_points = int(puzzle_input[0].split(": ")[1])


def player_wins(player: Character, boss: Character) -> bool:
    player_attack = max(1, player.damage - boss.armor)
    boss_attack = max(1, boss.damage - player.armor)

    turns_to_defeat_boss = (boss.hit_points + player_attack - 1) // player_attack
    turns_to_defeat_player = (player.hit_points + boss_attack - 1) // boss_attack

    return turns_to_defeat_boss <= turns_to_defeat_player


def solve(puzzle_input, player_should_win, func):
    costs = []
    for weapon in inventory["weapons"]:
        for armor_choice in inventory["armor"]:
            for ring_set in ring_combinations:
                total_cost = weapon[0] + armor_choice[0] + sum(r[0] for r in ring_set)
                total_damage = weapon[1] + armor_choice[1] + sum(r[1] for r in ring_set)
                total_armor = weapon[2] + armor_choice[2] + sum(r[2] for r in ring_set)

                if (
                    player_wins(
                        Character(total_damage, total_armor, 100),
                        Character(puzzle_input=puzzle_input),
                    )
                    == player_should_win
                ):
                    costs.append(total_cost)
    return func(costs)
