# 백준 1707

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(start, graph, visited):
    q = deque()
    q.append([start, 0])
    visited[start] = 0
    typeNum = [1, 0]

    while q:
        curV, curType = q.popleft()
        for nextV in graph[curV]:
            if visited[nextV] == -1:
                q.append([nextV, curType^1])
                visited[nextV] = curType^1
                typeNum[curType^1] += 1
            else:
                if visited[nextV] == curType:
                    return [-1, -1]

    return typeNum


def solve(V, graph):
    visited = [-1 for _ in range(V+1)]
    for i in range(V):
        if visited[i] == -1:
            a, b = BFS(i, graph, visited)
            if a == -1:
                return 'NO'
    
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V+1)]
        for _ in range(E):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        print(solve(V, graph))


main()
