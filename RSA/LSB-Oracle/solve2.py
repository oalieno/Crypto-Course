#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import *

r = remote('127.0.0.1', 20000)

n = int(r.recvline().split(b' = ')[1])
c = int(r.recvline().split(b' = ')[1])
e = 65537

inv  = inverse(2, n)
inve = pow(inv, e, n)

flag, x = 0, 0
for i in range(1024):
    r.sendline(str(c))
    m = int(r.recvline().split(b' = ')[1])
    bit = (m - x) % 2
    x = inv * (x + bit) % n
    flag += bit * (1 << i)
    c = (c * inve) % n

print(long_to_bytes(flag))
