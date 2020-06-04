#!/usr/bin/env python3
from Crypto.Util.number import *

def pad(data, block_size):
    if len(data) > block_size - 2:
        raise ValueError("message too big")
    return b'\x00' + b'\xff' * (block_size - 2 - len(data)) + b'\x00' + data

FLAG = open('./flag', 'rb').read()

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 3

m = bytes_to_long(pad(FLAG, 128))
c = pow(m, e, n)
print(f'n = {n}')
print(f'c = {c}')
