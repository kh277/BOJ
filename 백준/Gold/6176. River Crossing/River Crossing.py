# 백준 6176

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def solve(N, M, cost):
    # DP[i] = 지금까지 옮긴 소가 i마리일 때, 걸린 최소 시간
    DP = [INF for _ in range(N+1)]
    DP[0] = 0

    for moveCount in range(N):
        for curCow in range(min(1, moveCount+1), N+1):
            if moveCount+curCow <= N:
                # moveCount마리의 소를 이미 옮겼고, 이번에 John이 curCow마리의 소를 옮기고 돌아올 때 걸리는 시간
                DP[moveCount+curCow] = min(DP[moveCount+curCow], DP[moveCount]+cost[curCow]+M)

    # 마지막에 John이 돌아온 시간 제거
    return DP[N]-M


def main():
    N, M = map(int, input().split())

    # cost[i] = John이 소 i마리를 태우고 넘어갈 때 걸리는 시간
    cost = [M]
    for i in range(1, N+1):
        cost.append(cost[i-1] + int(input()))

    print(solve(N, M, cost))


main()