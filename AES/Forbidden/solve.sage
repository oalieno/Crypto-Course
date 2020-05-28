#!/usr/bin/env python3
import socket

class remote:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.buffer = b''
    def recvuntil(self, text):
        text = self._convert_to_bytes(text)
        while text not in self.buffer:
            self.buffer += self.s.recv(1024)
        index = self.buffer.find(text) + len(text)
        result, self.buffer = self.buffer[:index], self.buffer[index:]
        return result
    def recvline(self):
        return self.recvuntil(b'\n')
    def recvlines(self, n):
        lines = []
        for _ in range(n):
            lines.append(self.recvline())
        return lines
    def _convert_to_bytes(self, text):
        if type(text) is not bytes:
            text = str(text)
        if type(text) is str:
            text = text.encode()
        return text
    def send(self, text):
        text = self._convert_to_bytes(text)
        self.s.sendall(text)
    def sendline(self, text):
        text = self._convert_to_bytes(text)
        self.send(text + b'\n')
    def sendafter(self, prefix, text):
        self.recvuntil(prefix)
        self.send(text)
    def sendlineafter(self, prefix, text):
        self.recvuntil(prefix)
        self.sendline(text)

G.<a> = GF(2 ^ 128, modulus=x^128+x^7+x^2+x+1)
R.<x> = PolynomialRing(G)

def b2g(n):
    n = int.from_bytes(n, 'big')
    n = G((Integer(n).bits() + [0] * 128)[:128][::-1])
    return n

def g2b(n):
    n = (Integer(n.integer_representation()).bits() + [0] * 128)[:128]
    n = int(''.join(map(str, n)), 2)
    return n.to_bytes(16, 'big')

def xor(a, b):
    return bytes([x ^^ y for x, y in zip(a, b)])

r = remote('127.0.0.1', 20000)

r.sendlineafter('user = ', 'AAAAA')
C1 = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())
T1 = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())
r.sendlineafter('user = ', 'BBBBB')
C2 = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())
T2 = bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())

L1 = b2g(b'\x00' * 15 + bytes([len(C1) * 8]))
C1 = b2g(C1)
C2 = b2g(C2)
T1 = b2g(T1)
T2 = b2g(T2)

f = (C1 - C2) * x ^ 2 - (T1 - T2)
H, _ = f.roots()[0]
EJ = T1 - C1 * H ^ 2 - L1 * H

C1_ = xor(g2b(C1)[6:], xor(b'user:AAAAA', b'user:admin'))
C1_ = b2g(C1_)
T1_ = C1_ * H ^ 2 + L1 * H + EJ

r.sendlineafter('cipher = ', g2b(C1_)[6:].hex())
r.sendlineafter('tag = ', g2b(T1_).hex())
print(r.recvline())
