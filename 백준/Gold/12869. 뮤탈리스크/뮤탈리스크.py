# 백준 16270

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-9, -9, -3, -3, -1, -1]
dy = [-3, -1, -9, -1, -3, -9]
dz = [-1, -3, -1, -9, -9, -3]


def BFS(N, A):
    visited = [[[0] * (61) for _ in range(61)] for _ in range(61)]
    q = deque()

    # 초기값 큐에 추가
    start = [0, 0, 0, 0]
    for i in range(N):
        start[i] = A[i]
    q.append(start)
    visited[start[0]][start[1]][start[2]] = 1

    while q:
        curX, curY, curZ, count = q.popleft()

        # 종료조건
        if curX == 0 and curY == 0 and curZ == 0:
            return count

        for i in range(6):
            nextX = max(0, curX + dx[i])
            nextY = max(0, curY + dy[i])
            nextZ = max(0, curZ + dz[i])

            if visited[nextX][nextY][nextZ] == 0:
                q.append((nextX, nextY, nextZ, count+1))
                visited[nextX][nextY][nextZ] = 1


def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    print(BFS(N, A))


main()
