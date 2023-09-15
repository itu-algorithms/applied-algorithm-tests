#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(n):
        x = int(sys.stdin.readline(),16) & 0xffffffffffffffff
        pc = 0
        while x != 0:
            pc += x & 1
            x >>= 1
        print(pc)
