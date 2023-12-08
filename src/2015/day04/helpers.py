import hashlib


def get_santa_hash(secret_key, hash_starting_with, looking_range=(100000, 9999999)):
    for ans in range(looking_range[0], looking_range[1]):
        str2hash = secret_key + str(ans)
        result = hashlib.md5(str2hash.encode())

        if str(result.hexdigest()).startswith(hash_starting_with):
            return ans

        ans = ans + 1
    return -1
