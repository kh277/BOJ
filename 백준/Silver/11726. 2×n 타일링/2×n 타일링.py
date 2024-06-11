# 백준 11726

import sys

input = sys.stdin.readline


def solve(N: int) -> int:
    DP = [None for _ in range(1001)]
    DP[0] = 0
    DP[1] = 1
    DP[2] = 2

    for i in range(3, N+1):
        DP[i] = (DP[i-2] + DP[i-1]) % 10007
    
    return DP[N]


def main():
    N = int(input())

    print(solve(N))


main()
