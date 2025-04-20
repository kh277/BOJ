# 백준 14248

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, A, start):
    visited = [0 for _ in range(N)]
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        curI = q.popleft()

        for i in [-1, 1]:
            nextI = curI + A[curI]*i
            if 0 <= nextI < N and visited[nextI] == 0:
                q.append(nextI)
                visited[nextI] = 1
    
    return sum(visited)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = int(input())
    print(BFS(N, A, S-1))


main()
