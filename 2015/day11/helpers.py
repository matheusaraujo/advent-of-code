def find_next_password(password: str) -> str:
    password = next_password(password)
    while not is_valid_password(password):
        password = next_password(password)
    return password


def next_password(password: str) -> str:
    password = list(password)
    i = len(password) - 1
    while i >= 0:
        if password[i] == "z":
            password[i] = "a"
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return "".join(password)


def is_valid_password(password: str) -> bool:
    return (
        contains_increasing_straight(password)
        and not contains_forbidden_characters(password)
        and contains_at_least_two_non_overlapping_pairs(password)
    )


def contains_forbidden_characters(password: str) -> bool:
    return "i" in password or "o" in password or "l" in password


def contains_increasing_straight(password: str) -> bool:
    for i in range(len(password) - 2):
        if (ord(password[i]) + 1 == ord(password[i + 1])) and (
            ord(password[i + 1]) + 1 == ord(password[i + 2])
        ):
            return True
    return False


def contains_at_least_two_non_overlapping_pairs(password: str) -> bool:
    pairs, i = set(), 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2
