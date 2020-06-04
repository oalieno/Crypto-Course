#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import *

r = remote('127.0.0.1', 20000)

n = int(r.recvline().split(b' = ')[1])
c = int(r.recvline().split(b' = ')[1])
e = 65537

_2e = pow(2, e, n)

L, R = 0, 1
for i in range(1024):
    c = (c * _2e) % n
    r.sendline(str(c))
    m = int(r.recvline().split(b' = ')[1])
    L, R = L * 2, R * 2
    L += m == 1
    R -= m == 0

print(long_to_bytes(L * n // (1 << 1024)))
print(long_to_bytes(R * n // (1 << 1024)))
