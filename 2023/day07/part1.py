from helpers import (
    default_define_hand_value,
    default_define_label_value,
    extract_labels,
    solve,
)


def define_hand_value(hand):
    labels = extract_labels(hand)

    return default_define_hand_value(labels)


def part1(hands):
    return solve(hands, define_hand_value, default_define_label_value)
