#!/usr/bin/env python
import random
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

e1 = 257
d1 = inverse(e1, (p - 1) * (q - 1))
print(f'n = {n}')
print(f'd1 = {d1}')

e2 = 65537
m = bytes_to_long(pad(FLAG, 128))
c = pow(m, e2, n)
print(f'c = {c}')
