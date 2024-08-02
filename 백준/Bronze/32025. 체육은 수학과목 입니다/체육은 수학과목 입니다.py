# 백준 32025

import sys

input = sys.stdin.readline


def solve(H: int, W: int) -> list:
    return min(H, W) * 50


def main():
    H = int(input())
    W = int(input())

    print(solve(H, W))


main()