#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().strip().split(' '))
    nums = list(map(lambda i: int(i,16) & 0xffffffff, sys.stdin.readlines()))
    assert len(nums) == n
    for x in nums:
        print((x >> k) & 1)
