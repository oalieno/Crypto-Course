#!/usr/bin/env python3
import random
from functools import reduce

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
        nextbit = reduce(lambda x, y: x ^ y, [i & j for i, j in zip(self.state, self.feedback)])
        self.state = self.state[1:] + [nextbit]
        return nextbit
    def getbyte(self):
        b = 0
        for i in range(8):
            b = (b << 1) + self.getbit()
        return bytes([b])

def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])

FLAG = open('./flag', 'rb').read()
assert FLAG.startswith(b'CTF{')

lfsr = LFSR.random(16)
key = b''.join([lfsr.getbyte() for i in range(len(FLAG))])
print(f'enc = {xor(FLAG, key).hex()}')
