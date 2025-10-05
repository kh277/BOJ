# 백준 17073

'''
고인 물의 기대값은 W / (리프 노드의 개수)이다.
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, graph):
    result = 0
    q = deque()
    visited = bytearray(N+1)
    q.append(1)
    visited[1] = 1

    while q:
        curV = q.popleft()
        
        count = 0
        for nextV in graph[curV]:
            if visited[nextV] == 0:
                count += 1
                q.append(nextV)
                visited[nextV] = 1
        if count == 0:
            result += 1
    
    return result


def main():
    N, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(W/BFS(N, graph))


main()
