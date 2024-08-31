# 1271

import sys

input = sys.stdin.readline


def solve(N: int, M: int) -> int:
    return [N//M, N%M]


def main():
    N, M = map(int, input().split())
    for i in solve(N, M):
        print(i)


main()
