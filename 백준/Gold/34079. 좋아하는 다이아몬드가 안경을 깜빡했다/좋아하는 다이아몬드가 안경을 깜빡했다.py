# 백준 34079

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**6


def BFS(N, graph, start, visited):
    q = deque()
    traceback = [[] for _ in range(N+1)]
    q.append((start, 0))
    visited[start] = 0

    while q:
        curV, move = q.popleft()

        nextM = move + 1
        for nextV in graph[curV]:
            if visited[nextV] > nextM:
                visited[nextV] = nextM
                traceback[nextV] = [curV]
                q.append((nextV, nextM))
            elif visited[nextV] == nextM:
                traceback[nextV].append(curV)

    return traceback


def solve(N, graph):
    # 학교 -> 집으로 가는 최단 거리 탐색
    visited = [INF for _ in range(N+1)]
    traceback = BFS(N, graph, 1, visited)

    # 역추적 경로를 그래프로 잡고 다시 BFS 탐색
    visited2 = [INF for _ in range(N+1)]
    BFS(N, traceback, N, visited2)

    # 최단 경로에 포함된 정점 중 이동 거리가 동일한 정점끼리 모으기
    count = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        if visited2[i] != INF:
            count[visited2[i]].append(i)

    # 이동 거리가 동일한 정점이 1개뿐인 경우 탐색
    for i in range(1, N+1):
        if len(count[i]) == 1:
            return count[i]
    return 1


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    print(*solve(N, graph))


main()
