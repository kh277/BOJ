# 백준 17129

import io
from array import array
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def findPos(N, M, grid, strType):
    for y in range(N):
        for x in range(M):
            if grid[y][x] == strType:
                return [y, x]


def BFS(N, M, grid, start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [array('I', [0])*M for _ in range(N)]
    q = deque()
    q.append([start[0], start[1], 0])
    visited[start[0]][start[1]] = 1

    while q:
        curY, curX, move = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == 0:
                if grid[nextY][nextX] in [3, 4, 5]:
                    return ['TAK', move+1]
                elif grid[nextY][nextX] == 0:
                    q.append([nextY, nextX, move+1])
                    visited[nextY][nextX] = 1

    return ['NIE']


def solve(N, M, grid):
    start = findPos(N, M, grid, 2)
    return BFS(N, M, grid, start)


def main():
    N, M = map(int, input().split())
    A = [array('I', [0])*M for _ in range(N)]
    for y in range(N):
        x = 0
        for i in list(map(str, input().decode().strip())):
            A[y][x] = int(i)
            x += 1

    for i in solve(N, M, A):
        print(i)


main()
