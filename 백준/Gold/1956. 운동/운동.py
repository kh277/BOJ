# 백준 1956

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'i'
INF = 10**8


def FloydWarshall(V, graph):
    for curV in range(V):
        graph[curV][curV] = 0

    for midV in range(V):
        for startV in range(V):
            for endV in range(V):
                graph[startV][endV] = min(graph[startV][endV], graph[startV][midV] + graph[midV][endV])

    return graph


def solve(V, graph):
    minD = INF
    dist = FloydWarshall(V, graph)

    for i in range(V-1):
        for j in range(i+1, V):
            minD = min(minD, dist[i][j]+dist[j][i])

    return -1 if minD >= INF else minD 


def main():
    V, E = map(int, input().split())
    graph = [array(ARRAY_TYPE, [INF]) * V for _ in range(V)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = c

    print(solve(V, graph))


main()
