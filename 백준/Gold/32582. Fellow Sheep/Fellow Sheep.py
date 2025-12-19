# 백준 32582

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def BFS(capacity, source, sink, parent):
    visited = [False for _ in range(len(capacity))]
    q = deque([source])
    visited[source] = True

    while q:
        curV = q.popleft()
        for nextV in range(len(capacity)):
            # 용량이 남은 간선이 있는 경우
            if visited[nextV] == False and capacity[curV][nextV] > 0:
                q.append(nextV)
                visited[nextV] = True
                parent[nextV] = curV

                # sink에 도착할 경우
                if nextV == sink:
                    return True

    return False


def NetworkFlow(capacity, source, sink):
    parent = [-1 for _ in range(len(capacity))]
    maxFlow = 0
    
    # BFS로 증가 경로 탐색
    while BFS(capacity, source, sink, parent):
        # 증가 경로의 최소 용량 탐색
        pathFlow = INF
        s = sink
        while s != source:
            pathFlow = min(pathFlow, capacity[parent[s]][s])
            s = parent[s]

        # 경로에 따라 용량 업데이트
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= pathFlow
            capacity[v][u] += pathFlow
            v = parent[v]
        
        maxFlow += pathFlow

    return maxFlow


def main():
    N = int(input())
    maxSheep = INF
    for _ in range(N):
        capacity = [[0] * 4 for _ in range(4)]
        A, B, C, D, E = map(int, input().split())
        capacity[0][1] = A
        capacity[1][0] = A
        capacity[1][3] = B
        capacity[3][1] = B
        capacity[1][2] = C
        capacity[2][1] = C
        capacity[0][2] = D
        capacity[2][0] = D
        capacity[2][3] = E
        capacity[3][2] = E
        maxSheep = min(maxSheep, NetworkFlow(capacity, 0, 3))

    print(maxSheep)


main()
