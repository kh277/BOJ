# 백준 11724

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        curV = q.popleft()
        
        for nextV in graph[curV]:
            if visited[nextV] == False:
                q.append(nextV)
                visited[nextV] = True


def solve(N, graph):
    visited = [False for _ in range(N+1)]
    count = 0

    for i in range(1, N+1):
        if visited[i] == False:
            BFS(i, graph, visited)
            count += 1

    return count


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    print(solve(N, graph))


main()