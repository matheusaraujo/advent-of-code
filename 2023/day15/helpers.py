from functools import reduce


def hashing(s):
    return reduce(lambda curr, char: (curr + ord(char)) * 17 % 256, s, 0)
