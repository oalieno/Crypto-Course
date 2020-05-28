#!/usr/bin/env python3
from pwn import *

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

r = remote("127.0.0.1", 20000)

enc = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())

def oracle(c):
    r.sendlineafter('cipher = ', c.hex())
    if b'CORRECT' in r.recvline():
        return True
    else:
        return False

flag = b''
for i in range(16, len(enc), 16):
    ans = b''
    iv, block = enc[i-16:i], enc[i:i+16]
    for j in range(16):
        for k in range(256):
            if oracle(iv[:16 - 1 - j] + bytes([k]) + xor(bytes([j + 1] * j), xor(iv[-j:], ans)) + block):
                ans = bytes([iv[16 - 1 - j] ^ k ^ (j + 1)]) + ans
                print(ans)
                break
    flag += ans

print(flag)
