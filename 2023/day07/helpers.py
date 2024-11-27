import functools


def default_define_label_value(label):
    labels = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    return labels[label]


def default_define_hand_value(labels):
    if labels[0][1] == 1:
        return 0
    if labels[0][1] == 2:
        return 20 if labels[1][1] == 2 else 10
    if labels[0][1] == 3:
        return 40 if labels[1][1] == 2 else 30
    if labels[0][1] == 4:
        return 50

    return 60


def extract_labels(hand):
    labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    labels = [(l, hand.count(l)) for l in labels]
    labels.sort(key=lambda x: -x[1])

    return labels


def compare(hand_a, hand_b, define_label_value):
    if hand_a[2] == hand_b[2]:
        for i in range(0, 5):
            if hand_a[0][i] != hand_b[0][i]:
                return define_label_value(hand_a[0][i]) - define_label_value(
                    hand_b[0][i]
                )
    return hand_a[2] - hand_b[2]


def solve(hands, define_hand_value, define_label_value):
    hands = [h.split(" ") for h in hands]
    hands = [(h[0], h[1], define_hand_value(h[0])) for h in hands]

    def compare_wrapper(hand_a, hand_b):
        return compare(hand_a, hand_b, define_label_value)

    hands.sort(key=functools.cmp_to_key(compare_wrapper))

    ans, idx = 0, 1
    for h in hands:
        ans += idx * int(h[1])
        idx += 1
    return ans
