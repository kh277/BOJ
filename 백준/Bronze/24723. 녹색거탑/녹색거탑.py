# 백준 24723


import sys

input = sys.stdin.readline


def solve(N: int) -> int:
    return 2**N


def main():
    N = int(input())
    print(solve(N))


main()
