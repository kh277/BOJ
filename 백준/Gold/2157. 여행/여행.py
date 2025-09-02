# 백준 2157

'''
DP[count][end] = 이동 횟수가 count이고 도착한 정점이 end인 경우, 먹은 기내식 점수의 최대값
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, cost):
    DP = [[-1 for _ in range(N)] for _ in range(M+1)]
    DP[1][0] = 0

    for move in range(1, M):
        for start in range(N-1):
            for end in range(start+1, N):
                curCost = cost[start][end]
                if curCost >= 0 and DP[move][start] >= 0:
                    DP[move+1][end] = max(DP[move+1][end], DP[move][start] + curCost)

    return max([DP[i][N-1] for i in range(1, M+1)])


def main():
    N, M, K = map(int, input().split())
    cost = [[-1 for _ in range(N)] for _ in range(N)]

    for _ in range(K):
        a, b, c = map(int, input().split())
        if a < b:
            cost[a-1][b-1] = max(cost[a-1][b-1], c)

    print(solve(N, M, cost))


main()
