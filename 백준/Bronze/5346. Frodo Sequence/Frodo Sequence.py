# 백준 5346

import sys

input = sys.stdin.readline


def solve(N):
    return (N+1)//2


# main 함수 ----------
while True:
    N = int(input())
    if N == 0:
        break
    print(solve(N))