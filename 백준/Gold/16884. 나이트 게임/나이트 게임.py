# 백준 16884

import sys

input = sys.stdin.readline


def solve():
    return 'cubelover' if N % 2 == 0 else 'koosaga'


# main 함수 ----------
T = int(input())
for _ in range(T):
    N = int(input())
    print(solve())