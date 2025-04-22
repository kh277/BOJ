# 백준 12515

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    count = 1

    while q:
        curV = q.popleft()

        for nextV in graph[curV]:
            if visited[nextV] == False:
                q.append(nextV)
                visited[nextV] = True
                count += 1

    if count == 1:
        return 0
    return count


def solve(N, A):
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        graph[i].append(A[i-1])
    
    visited = [False for _ in range(N+1)]
    result = 0
    for i in range(N):
        if visited[i] == False:
            result += BFS(i, graph, visited)
    
    return result


def main():
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        A = list(map(int, input().split()))
    
        print(f"Case #{i}: {solve(N, A)}.000000")


main()
