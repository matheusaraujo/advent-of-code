import functools


def define_label_value(label):
    labels = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,
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


def define_hand_value(hand):
    labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    labels = [(l, hand.count(l)) for l in labels]
    labels.sort(key=lambda x: -x[1])

    j = next(filter(lambda x: x[0] == "J", labels), None)

    def no_j():
        if labels[0][1] == 1:
            return 0
        elif labels[0][1] == 2:
            return 20 if labels[1][1] == 2 else 10
        elif labels[0][1] == 3:
            return 40 if labels[1][1] == 2 else 30
        elif labels[0][1] == 4:
            return 50
        elif labels[0][1] == 5:
            return 60

    if j[1] == 0:
        return no_j()

    if j[1] == 5 or j[1] == 4:
        return 60
    elif j[1] == 3:
        return 60 if labels[1][1] == 2 else 50
    elif j[1] == 2:
        if labels[0][1] == 3:
            return 60
        elif labels[0][0] != "J" and labels[0][1] == 2:
            return 50
        elif labels[1][0] != "J" and labels[1][1] == 2:
            return 50
        return 30
    else:
        labels[0] = (labels[0][0], labels[0][1] + 1)
        return no_j()
    return 0


def compare(hand_a, hand_b):
    if hand_a[2] == hand_b[2]:
        for i in range(0, 5):
            if hand_a[0][i] != hand_b[0][i]:
                return define_label_value(hand_a[0][i]) - define_label_value(
                    hand_b[0][i]
                )
    return hand_a[2] - hand_b[2]


def part2(hands):
    hands = [h.replace("\n", "").split(" ") for h in hands]
    hands = [(h[0], h[1], define_hand_value(h[0])) for h in hands]
    hands.sort(key=functools.cmp_to_key(compare))
    ans, idx = 0, 1
    for h in hands:
        ans += idx * int(h[1])
        idx += 1
    return ans
