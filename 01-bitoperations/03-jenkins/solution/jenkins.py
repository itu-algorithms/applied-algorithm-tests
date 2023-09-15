#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    h = 0
    for c in sys.stdin.read():
        h += ord(c)
        h &= 0xffffffff
        h += h << 10
        h &= 0xffffffff
        h ^= h >> 6
    h += h << 3
    h &= 0xffffffff
    h ^= h >> 11
    h += h << 15
    h &= 0xffffffff
    print(f'{h:08x}')
