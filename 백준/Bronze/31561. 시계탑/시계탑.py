# 백준 31561

import sys

input = sys.stdin.readline


def solve(M: int) -> int:
    if 0 <= M <= 30:
        return M/2
    else:
        return 15 + (M-30)*3/2


def main():
    M = int(input())

    print(solve(M))


main()