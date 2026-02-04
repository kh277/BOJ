# 백준 34951

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1e15


def DFS(N, graph, visited, S):
    maxT = 0
    q = []
    q.append((0, 0))
    visited[0] = 0

    while q:
        curV, curD = q.pop()

        for nextV, _ in graph[curV]:
            nextD = curD
            if nextV >= N:
                nextD += S[nextV-N]
            if visited[nextV] < nextD:
                q.append((nextV, nextD))
                visited[nextV] = nextD
                if nextD > maxT:
                    maxT = nextD

    return maxT


def solve(N, M, graph, S, G):
    # G와 이웃한 천체와의 최단거리 도출
    minD = INF
    for curV in range(N+M):
        for nextV, dist in graph[curV]:
            if nextV == G or curV == G:
                minD = min(minD, dist)

    # BFS로 지나게 할 수 있는 최대의 우주 시간 저장
    visited = [-1 for _ in range(N+M)]
    maxT = DFS(N, graph, visited, S)

    if maxT >= minD:
        return 'HAPPY'
    return 'SAD'


def main():
    N, M, E = map(int, input().split())
    add = N+M
    graph = [[] for _ in range(N+M)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        if s < 0:
            s += add
        else:
            s -= 1
        if e < 0:
            e += add
        else:
            e -= 1
        graph[s].append((e, w))

    S = list(map(int, input().split()))
    G = int(input())

    print(solve(N, M, graph, S[::-1], G-1))


main()
