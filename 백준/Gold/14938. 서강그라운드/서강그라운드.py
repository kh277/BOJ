# 백준 14938

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def FloydWarshall(V, graph):
    for curV in range(V):
        graph[curV][curV] = 0

    for midV in range(V):
        for startV in range(V):
            for endV in range(V):
                graph[startV][endV] = min(graph[startV][endV], graph[startV][midV] + graph[midV][endV])

    return graph


def solve(V, E, M, items, graph):
    maxItem = 0
    dist = FloydWarshall(V, graph)
    for startV in range(V):
        getItem = 0
        for endV in range(V):
            if dist[startV][endV] <= M:
                getItem += items[endV]
        maxItem = max(maxItem, getItem)

    return maxItem


def main():
    V, M, E = map(int, input().split())
    items = list(map(int, input().split()))
    graph = [[INF for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        a, b, l = map(int, input().split())
        graph[a-1][b-1] = l
        graph[b-1][a-1] = l
    print(solve(V, E, M, items, graph))


main()
