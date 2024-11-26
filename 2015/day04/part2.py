from helpers import get_santa_hash


def part2(secret_key):
    return get_santa_hash(secret_key[0], "000000")
