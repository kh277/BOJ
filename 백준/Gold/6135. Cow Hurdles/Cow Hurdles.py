# 백준 6135

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


# 플로이드-워셜 변형
def init(N, graph):
    for curV in range(1, N+1):
        graph[curV][curV] = 0

    for midV in range(1, N+1):
        for startV in range(1, N+1):
            for endV in range(1, N+1):
                graph[startV][endV] = min(graph[startV][endV], max(graph[startV][midV], graph[midV][endV]))

    for startV in range(N+1):
        for endV in range(N+1):
            if graph[startV][endV] == INF:
                graph[startV][endV] = -1

    return graph


def query(start, end, DP):
    return DP[start][end]


def main():
    N, M, T = map(int, input().split())
    graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        s, e, h = map(int, input().split())
        graph[s][e] = h

    DP = init(N, graph)
    for _ in range(T):
        a, b = map(int, input().split())
        print(query(a, b, DP))


main()