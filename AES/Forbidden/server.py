#!/usr/bin/env python3
import os
from Crypto.Cipher import AES

KEY = os.urandom(16)
NONCE = os.urandom(12)
FLAG = open('./flag').read()

def main():
    for _ in range(2):
        aes = AES.new(KEY, AES.MODE_GCM, nonce=NONCE)
        user = input('user = ').strip()
        if 'admin' in user:
            raise ValueError
        cipher, tag = aes.encrypt_and_digest(f'user:{user}'.encode())
        print(f'cipher = {cipher.hex()}')
        print(f'tag = {tag.hex()}')

    aes = AES.new(KEY, AES.MODE_GCM, nonce=NONCE)
    cipher = bytes.fromhex(input('cipher = ').strip())
    tag = bytes.fromhex(input('tag = ').strip())
    plain = aes.decrypt_and_verify(cipher, tag)
    if b'admin' in plain:
        print(FLAG)
    else:
        print('YOU ARE NOT ADMIN!!!')

try:
    main()
except:
    ...
