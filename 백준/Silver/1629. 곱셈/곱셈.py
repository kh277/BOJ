# 백준 1629


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def recur(A: int, B: int, C: int) -> int:
    return pow(A, B, mod=C)


# main() ----------
A, B, C = map(int, input().split())

print(recur(A, B, C))
