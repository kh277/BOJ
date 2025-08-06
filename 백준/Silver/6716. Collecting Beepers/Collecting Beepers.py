# 백준 6716

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8
START = 0


def TSP(N, graph, status, curV, DP):
    if status == (1<<N) - 1:
        return graph[curV][START]

    if not DP[curV][status] == 0:
        return DP[curV][status]

    DP[curV][status] = INF

    for nextV in range(N):
        if (status & (1<<nextV)) == 0:
            temp = graph[curV][nextV] + TSP(N, graph, status | (1<<nextV), nextV, DP)

            if temp < DP[curV][status]:
                DP[curV][status] = temp

    return DP[curV][status]


def solve(N, point):
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            temp = abs(point[i][0]-point[j][0]) + abs(point[i][1]-point[j][1])
            graph[i][j] = temp
            graph[j][i] = temp

    return TSP(N, graph, 1<<START, 0, [[0 for _ in range(1<<N)] for _ in range(N)])


def main():
    T = int(input())
    for _ in range(T):
        X, Y = map(int, input().split())
        Sx, Sy = map(int, input().split())
        point = [[Sx, Sy]]
        N = int(input())
        for _ in range(N):
            point.append(list(map(int, input().split())))
        print(f"The shortest path has length {solve(N+1, point)}")


main()
