from helpers import (
    default_define_hand_value,
    default_define_label_value,
    extract_labels,
    solve,
)


def define_label_value(label):
    if label == "J":
        return 1
    return default_define_label_value(label)


def define_hand_value_joker(j, labels):
    if j[1] == 5 or j[1] == 4:
        return 60
    if j[1] == 3:
        return 60 if labels[1][1] == 2 else 50
    if j[1] == 2:
        if labels[0][1] == 3:
            return 60
        if (labels[0][0] != "J" and labels[0][1] == 2) or (
            labels[1][0] != "J" and labels[1][1] == 2
        ):
            return 50
        return 30

    labels[0] = (labels[0][0], labels[0][1] + 1)
    return default_define_hand_value(labels)


def define_hand_value(hand):
    labels = extract_labels(hand)

    j = next(filter(lambda x: x[0] == "J", labels), None)

    if j[1] == 0:
        return default_define_hand_value(labels)

    return define_hand_value_joker(j, labels)


def part2(hands):
    return solve(hands, define_hand_value, define_label_value)
