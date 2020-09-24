#!/usr/bin/env python3
import os
from Crypto.Cipher import AES

KEY = os.urandom(16)
FLAG = open('./flag').read()

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    aes = AES.new(KEY, AES.MODE_ECB)
    
    # encrypt token
    user = input('user = ').strip()
    if ':;' in user:
        raise ValueError
    token = f'user:{user};money:10;'.encode()
    token = aes.encrypt(pad(token))
    print(f'token = {token.hex()}')
    
    # decrypt token
    token = bytes.fromhex(input('token = ').strip())
    token = aes.decrypt(token)
    user, money, _ = token.split(b';')
    if int(money.split(b':')[1]) > 666666:
        print(FLAG)
    else:
        print('SHOW ME THE MONEY!!!')

try:
    main()
except:
    ...
