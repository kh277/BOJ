# 백준 1260

import sys
from collections import deque

input = sys.stdin.readline


def DFS(V: int, graph: list, visited: list) -> list:
    visited_point = []
    q = deque()
    q.append(V)

    while q:
        temp = q.pop()

        if visited[temp]:
            continue

        visited_point.append(temp)
        visited[temp] = True

        for i in sorted(graph[temp], reverse=True):
            q.append(i)

    return visited_point


def BFS(V: int, graph: list, visited: list) -> list:
    visited_point = []
    q = deque()
    q.append(V)

    while q:
        temp = q.popleft()

        if visited[temp]:
            continue

        visited_point.append(temp)
        visited[temp] = True

        for i in sorted(graph[temp]):
            q.append(i)

    return visited_point


def main():
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    # graph의 i번째 인덱스에는 i번째 점과 연결된 간선이 저장됨
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(*DFS(V, graph, [False for _ in range(N+1)]))
    print(*BFS(V, graph, [False for _ in range(N+1)]))


main()
