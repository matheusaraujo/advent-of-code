import hashlib

def problem2(secret_key):

    ans = 1

    while True:
        str2hash = secret_key + str(ans)
        result = hashlib.md5(str2hash.encode())

        if str(result.hexdigest()).startswith("000000"):
            return ans
        
        ans = ans + 1 
    