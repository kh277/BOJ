# 백준 10156

import sys

input = sys.stdin.readline


def solve():
    return max(K*N - M, 0)


# main 함수 ----------
K, N, M = map(int, input().split())
print(solve())