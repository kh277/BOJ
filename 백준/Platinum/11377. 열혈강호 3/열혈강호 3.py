# 백준 11377

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def EdmondKarp(graph, capacity, source, sink):
    totalFlow = 0
    while True:
        parent = [-1] * (sink+1)
        q = deque()
        q.append(source)

        isFound = False
        while q:
            curV = q.popleft()
            for nextV in graph[curV]:
                if parent[nextV] == -1 and capacity[curV][nextV] > 0:
                    parent[nextV] = curV
                    if nextV == sink:
                        isFound = True
                        break
                    q.append(nextV)
            if isFound == True:
                break
        if parent[sink] == -1:
            break

        totalFlow += 1
        curV = sink
        while curV != source:
            prevV = parent[curV]
            capacity[prevV][curV] -= 1
            capacity[curV][prevV] += 1
            curV = prevV

    return totalFlow


def main():
    N, M, K = map(int, input().split())
    sink = N+M+2
    graph = [[] for _ in range(sink+1)]
    capacity = [[0] * (sink+1) for _ in range(sink+1)]

    # 초기 그래프 세팅
    graph[0].append(1)
    graph[1].append(0)
    capacity[0][1] = K
    for i in range(2, N+2):
        graph[0].append(i)
        graph[i].append(0)
        graph[1].append(i)
        graph[i].append(1)
        capacity[0][i] = 1
        capacity[1][i] = 1
    for i in range(N+2, N+M+2):
        graph[sink].append(i)
        graph[i].append(sink)
        capacity[i][sink] = 1
    for s in range(2, N+2):
        _, *w = list(map(int, input().split()))
        for e in w:
            e = e+N+1
            graph[s].append(e)
            graph[e].append(s)
            capacity[s][e] = 1

    print(EdmondKarp(graph, capacity, 0, sink))


main()
