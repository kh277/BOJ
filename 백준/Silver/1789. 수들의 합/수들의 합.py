# 백준 1789

import sys

input = sys.stdin.readline


def solve(N: int) -> int:
    if N == 1:
        return 1
    
    for i in range(N+1):
        if i*(i+1)/2 > N:
            return i-1


def main():
    N = int(input())

    print(solve(N))


main()
