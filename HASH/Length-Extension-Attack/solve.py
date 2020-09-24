#!/usr/bin/env python3
import hashpumpy
from base64 import b64encode, b64decode
from pwn import *

r = remote('127.0.0.1', 20000)

r.recvuntil('your token: ')
token = b64decode(r.recvline().strip())
r.recvuntil('your authentication code: ')
auth = r.recvline().strip()

new_auth, new_token = hashpumpy.hashpump(auth, token, 'user=admin', 28)

r.sendlineafter("input your token: ", b64encode(new_token))
r.sendlineafter("input your authentication code: ", new_auth)

print(r.recvline().decode())
