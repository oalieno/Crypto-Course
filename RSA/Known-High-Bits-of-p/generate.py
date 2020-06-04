#!/usr/bin/env python3
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
e = 65537

if q > p:
    p, q = q, p
p = hex(p)[2:].rjust(128, '0')
p = p[:81] + '0' * (128 - 81)
print(f'p = {p}')

m = bytes_to_long(pad(FLAG))
c = pow(m, e, n)
print(f'n = {n}')
print(f'c = {c}')
