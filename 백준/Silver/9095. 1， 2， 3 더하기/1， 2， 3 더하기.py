# 백준 11726

import sys

input = sys.stdin.readline


def solve(N: int) -> int:
    DP = [None for _ in range(1001)]
    # 미사용
    DP[0] = 0

    # 1
    DP[1] = 1

    # 1+1, 2
    DP[2] = 2

    # 1+1+1, 2+1, 1+2, 3
    DP[3] = 4

    for i in range(4, N+1):
        DP[i] = DP[i-3] + DP[i-2] + DP[i-1]
    
    return DP[N]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())

        print(solve(N))


main()
