# 백준 1000

import sys

input = sys.stdin.readline


def solve(A: int, B: int) -> int:
    return A+B


def main():
    A, B = map(int, input().split())
    print(solve(A, B))


main()