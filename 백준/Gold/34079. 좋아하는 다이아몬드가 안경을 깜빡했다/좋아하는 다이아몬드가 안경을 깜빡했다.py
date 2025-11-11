# 백준 34079

import io
from array import array
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**6


def BFS(N, graph, start):
    q = deque()
    visited = array('i', [INF]) * (N+1)
    q.append((start, 0))
    visited[start] = 0

    while q:
        curV, move = q.popleft()

        nextM = move + 1
        for nextV in graph[curV]:
            if visited[nextV] > nextM:
                visited[nextV] = nextM
                q.append((nextV, nextM))

    return visited


def solve(N, graph):
    # 시작 정점을 1번, N번 정점으로 잡고 BFS 탐색
    dist1 = BFS(N, graph, 1)
    distN = BFS(N, graph, N)

    # 최단 거리에 포함되는 정점까지의 이동 거리 및 정점 번호 저장
    minD = dist1[N]
    count = array('i', [0]) * (minD+1)
    index = array('i', [0]) * (minD+1)
    for i in range(1, N+1):
        if dist1[i] <= minD and dist1[i]+distN[i] == minD:
            count[dist1[i]] += 1
            index[dist1[i]] = i

    # 이동 거리가 유일한 정점 반환
    for i in range(minD-1, -1, -1):
        if count[i] == 1:
            return index[i]
    return 1


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    print(solve(N, graph))


main()
