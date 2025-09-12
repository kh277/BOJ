# 백준 1956

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'i'
INF = 10**8


def FloydWarshall(V, graph):
    for curV in range(1, V+1):
        graph[curV][curV] = 0

    for midV in range(1, V+1):
        for startV in range(1, V+1):
            for endV in range(1, V+1):
                graph[startV][endV] = min(graph[startV][endV], graph[startV][midV] + graph[midV][endV])

    return graph


def solve(V, graph):
    minD = INF
    dist = FloydWarshall(V, graph)

    for i in range(1, V):
        for j in range(i+1, V+1):
            minD = min(minD, dist[i][j]+dist[j][i])

    return -1 if minD >= INF else minD 


def main():
    V, E = map(int, input().split())
    graph = [array(ARRAY_TYPE, [INF]) * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    print(solve(V, graph))


main()
