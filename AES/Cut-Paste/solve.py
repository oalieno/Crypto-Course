#!/usr/bin/env python3
from pwn import *

r = remote('127.0.0.1', 20000)

# user:AAAAAAAAAAA 9999999999999999 AAAAAAAAA;money: 10;...
r.sendlineafter('user = ', 'A' * 11 + '9' * 16 + 'A' * 9)
token = r.recvline().strip().partition(b' = ')[2].decode()
token = bytes.fromhex(token)
token = token[:16] + token[32:48] + token[16:32] + token[48:]
r.sendlineafter('token = ', token.hex())

r.interactive()
