from heapq import heappop, heappush


# pylint: disable=too-few-public-methods
class Player:
    def __init__(self, hit_points, mana):
        self.hit_points = hit_points
        self.mana = mana


# pylint: disable=too-few-public-methods
class Boss:
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage

    @staticmethod
    def parse(puzzle_input: str):
        hit_points, damage = (
            puzzle_input[0].split(": ")[1],
            puzzle_input[1].split(": ")[1],
        )
        return Boss(int(hit_points), int(damage))


class Effect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __lt__(self, other):
        return self.duration < other.duration


class Spell:
    # pylint: disable=too-many-arguments
    def __init__(self, name, cost, damage, heal, effect_duration, mana_gain):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.effect_duration = effect_duration
        self.mana_gain = mana_gain


SPELLS = [
    Spell("Magic Missile", 53, 4, 0, 0, 0),
    Spell("Drain", 73, 2, 2, 0, 0),
    Spell("Shield", 113, 0, 0, 6, 0),
    Spell("Poison", 173, 0, 0, 6, 0),
    Spell("Recharge", 229, 0, 0, 5, 101),
]


class State:
    # pylint: disable=too-many-arguments
    def __init__(
        self, mana_spent, player_hp, mana, boss_hp, armor, effects, player_turn
    ):
        self.mana_spent = mana_spent
        self.player_hp = player_hp
        self.mana = mana
        self.boss_hp = boss_hp
        self.armor = armor
        self.effects = effects
        self.player_turn = player_turn

    def apply_effects(self):
        new_effects = []
        new_mana = self.mana
        new_armor = 0
        new_boss_hp = self.boss_hp

        for effect in self.effects:
            if effect.name == "Shield":
                new_armor = 7
            elif effect.name == "Poison":
                new_boss_hp -= 3
            elif effect.name == "Recharge":
                new_mana += 101

            if effect.duration > 1:
                new_effects.append(Effect(effect.name, effect.duration - 1))

        self.mana = new_mana
        self.armor = new_armor
        self.boss_hp = new_boss_hp
        self.effects = new_effects

    def next_state_boss_turn(self, damage):
        return State(
            self.mana_spent,
            self.player_hp - damage,
            self.mana,
            self.boss_hp,
            self.armor,
            self.effects,
            True,
        )

    def next_state_player_turn(self, spell, next_effects):
        return State(
            self.mana_spent + spell.cost,
            self.player_hp + spell.heal,
            self.mana - spell.cost,
            self.boss_hp - spell.damage,
            self.armor,
            next_effects,
            False,
        )

    def is_win(self):
        return self.boss_hp <= 0

    def is_loss(self):
        return self.player_hp <= 0

    def __lt__(self, other):
        return self.mana_spent < other.mana_spent


def min_mana_to_win(player, boss, hard_mode=False):
    initial_state = State(
        0, player.hit_points, player.mana, boss.hit_points, 0, [], True
    )
    queue = [initial_state]

    while queue:
        state = heappop(queue)

        if state.player_turn and hard_mode:
            state.player_hp -= 1
            if state.is_loss():
                continue

        state.apply_effects()

        if state.is_win():
            return state.mana_spent
        if state.is_loss():
            continue

        if not state.player_turn:
            damage = max(1, boss.damage - state.armor)
            heappush(queue, state.next_state_boss_turn(damage))
            continue

        for spell in SPELLS:
            if spell.cost > state.mana:
                continue

            if any(e.name == spell.name and e.duration > 0 for e in state.effects):
                continue

            next_effects = state.effects[:]
            if spell.effect_duration:
                next_effects.append(Effect(spell.name, spell.effect_duration))

            heappush(queue, state.next_state_player_turn(spell, next_effects))
    return float("inf")
