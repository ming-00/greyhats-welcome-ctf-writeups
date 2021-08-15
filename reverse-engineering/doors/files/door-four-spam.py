import hashlib
import binascii

def brute_key():
    key = 10 ** (6 - 1) * 6
    limit = 10 ** (7 - 1)
    while key < limit: # we work altenating style
        if check(key):
            return key
        if check(limit):
            return limit
        limit -= 1
        key += 1
    print("UNABLE TO FIND KEY")
    exit(1)

def check(key):
    hhs = [
        b'919c5ab6d04ee9d1c81335692d2ed68e',
        b'9f7e8841c1d64dfde51953fccecde2cf',
        b'bcb34c837111773983f4860ee51cb1b6',
        b'e48b14700f10e3d8f3ad25b73a0d20db',
        b'835f2ff9473cfc787d4f1c08ad5037c9',
        b'c3e3b06937f539a2e52b834a4f1d27fc',
    ]
    for i in range(6):
        dg = key % 10
        key //= 10
        hh = binascii.hexlify(hashlib.md5(f"{i}_{dg}_{key}".encode()).digest())
        if hhs[i] != hh:
            return False
    return (key == 0)

if __name__ == "__main__":
    key_4 = brute_key()
    print(key_4)
    exit(0)