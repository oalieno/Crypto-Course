#!/usr/bin/env python3
from sage.matrix.berlekamp_massey import berlekamp_massey

class LFSR:
    def __init__(self, init, feedback):
        self.state = init
        self.feedback = feedback
    @classmethod
    def random(cls, size):
        init = [random.choice([0, 1]) for i in range(size)]
        feedback = [random.choice([0, 1]) for i in range(size)]
        return cls(init, feedback)
    def getbit(self):
        nextbit = reduce(lambda x, y: x ^^ y, [int(i) & int(j) for i, j in zip(self.state, self.feedback)])
        self.state = self.state[1:] + [nextbit]
        return nextbit
    def getbyte(self):
        b = 0
        for i in range(8):
            b = (b << 1) + self.getbit()
        return bytes([b])

def xor(a, b):
    return bytes([i ^^ j for i, j in zip(a, b)])

def bytes2bits(x):
    return [int(i) for i in f'{int.from_bytes(x, "big"):0{len(x) * 8}b}']

# recover feedback coefficients
enc = bytes.fromhex('d0aa72cef8dab5baac')
stream = xor(enc[:4], b'CTF{')
s = [GF(2)(i) for i in bytes2bits(stream)]
feedback = ([0] * 16 + berlekamp_massey(s).list()[:-1])[-16:]

# generate xor key to decrypt
lfsr = LFSR(bytes2bits(stream)[16:], feedback)
key = b''.join([lfsr.getbyte() for _ in range(5)])
plain = xor(enc[4:], key)
print(b'CTF{' + plain)
