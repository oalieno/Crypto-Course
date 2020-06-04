#!/usr/bin/env python3
import random
from Crypto.Util.number import *

def pad(data, block_size):
    padlen = block_size - len(data) - 2
    if padlen < 8:
        raise ValueError
    return b'\x00' + bytes([random.randint(1, 255) for _ in range(padlen)]) + b'\x00' + data

FLAG = open('./flag', 'rb').read()

p  = getPrime(512)
q1 = getPrime(512)
q2 = getPrime(512)
n1 = p * q1
n2 = p * q2
e = 65537

m = bytes_to_long(pad(FLAG, 128))
c = pow(m, e, n1)
print(f'n1 = {n1}')
print(f'n2 = {n2}')
print(f'c = {c}')
