# 백준 24516

import sys

input = sys.stdin.readline


def solve():
    return [i for i in range(1, 1+2*N, 2)]


# main 함수 ----------
N = int(input())
print(*solve())