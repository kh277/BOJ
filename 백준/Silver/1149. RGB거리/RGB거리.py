# 백준 1149

import sys

input = sys.stdin.readline


def solve(N: int, cost: list) -> int:
    DP = [[0, 0, 0] for _ in range(N)]

    DP[0] = [cost[0][0], cost[0][1], cost[0][2]]

    for i in range(1, N):
        DP[i][0] = cost[i][0] + min(DP[i-1][1], DP[i-1][2])
        DP[i][1] = cost[i][1] + min(DP[i-1][0], DP[i-1][2])
        DP[i][2] = cost[i][2] + min(DP[i-1][0], DP[i-1][1])
    
    return min(DP[N-1])


def main():
    N = int(input())
    cost = []
    for i in range(N):
        cost.append(list(map(int, input().split())))

    print(solve(N, cost))


main()
