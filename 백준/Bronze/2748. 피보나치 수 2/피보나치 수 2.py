# 백준 2748

import sys

input = sys.stdin.readline


def solve(N: int) -> int:
    DP = [0 for _ in range(N+1)]

    DP[0] = 0
    DP[1] = 1
    for i in range(2, N+1):
        DP[i] = DP[i-1] + DP[i-2]
    
    return DP[N]


def main():
    N = int(input())
    
    print(solve(N))


main()
