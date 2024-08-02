# 백준 2745

import sys

input = sys.stdin.readline


def solve(N: str, B: int):
    return int(N, B)


def main():
    N, B = map(str, input().split())

    print(solve(N, int(B)))


main()