#!/usr/bin/env python3
import random
from Crypto.Util.number import *

def pad(data, block_size):
    padlen = block_size - len(data) - 2
    if padlen < 8:
        raise ValueError
    return b'\x00' + bytes([random.randint(1, 255) for _ in range(padlen)]) + b'\x00' + data

FLAG = open('./flag', 'rb').read()

m = bytes_to_long(pad(FLAG, 128))
e = 3
for i in range(3):
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    c = pow(m, e, n)
    print(f'n{i} = {n}')
    print(f'c{i} = {c}')
