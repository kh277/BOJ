# 백준 6840

import sys

input = sys.stdin.readline


def solve(L):
    return sorted(L)[1]


# main 함수 ----------
L = []
for _ in range(3):
    L.append(int(input()))

print(solve(L))