# 백준 27866

import sys

input = sys.stdin.readline


def solve(S: str, i: int) -> int:
    return S[i-1]


def main():
    S = input().rstrip()
    i = int(input())
    print(solve(S, i))


main()
