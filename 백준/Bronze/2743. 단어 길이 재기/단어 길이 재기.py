# 백준 2743

import sys

input = sys.stdin.readline


def solve(S: str) -> int:
    return len(S)


def main():
    S = input().rstrip()
    print(solve(S))


main()
