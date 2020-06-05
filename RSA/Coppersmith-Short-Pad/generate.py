#!/usr/bin/env python3
import os
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
e = 3

m = pad(FLAG, 120)
m1 = bytes_to_long(m + os.urandom(8))
m2 = bytes_to_long(m + os.urandom(8))
c1 = pow(m1, e, n)
c2 = pow(m2, e, n)
print(f'n = {n}')
print(f'c1 = {c1}')
print(f'c2 = {c2}')
