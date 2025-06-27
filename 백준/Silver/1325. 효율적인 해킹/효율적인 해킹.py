# 백준 1325

import io
from array import array
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, start, edge):
    q = deque()
    q.append(start)
    visited = bytearray(N+1)
    visited[start] ^= 1

    while q:
        curV = q.popleft()

        for nextV in edge[curV]:
            if visited[nextV] == 0:
                q.append(nextV)
                visited[nextV] ^= 1
    
    return sum(visited)


def main():
    N, M = map(int, input().split())
    edge = [array('h') for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[b].append(a)

    result = []
    maxResult = 0
    for i in range(1, N+1):
        temp = BFS(N, i, edge)
        if temp > maxResult:
            result = [i]
            maxResult = temp
        elif temp == maxResult:
            result.append(i)
    print(*sorted(result))


main()
