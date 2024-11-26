from helpers import get_santa_hash


def part1(secret_key):
    return get_santa_hash(secret_key[0], "00000")
