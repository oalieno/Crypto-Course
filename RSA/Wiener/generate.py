#!/usr/bin/env python
import random
from math import gcd
from Crypto.Util.number import *

def pad(data, block_size):
    padlen = block_size - len(data) - 2
    if padlen < 8:
        raise ValueError
    return b'\x00' + bytes([random.randint(1, 255) for _ in range(padlen)]) + b'\x00' + data

FLAG = open('./flag', 'rb').read()

p = getPrime(512)
q = getPrime(512)
n = p * q

d = None
while d is None or gcd(d, (p - 1) * (q - 1)) != 1:
    d = random.randint(1, int((1 / 3) * n ** (1 / 4)))
e = inverse(d, (p - 1) * (q - 1))

m = bytes_to_long(pad(FLAG, 128))
c = pow(m, e, n)
print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
