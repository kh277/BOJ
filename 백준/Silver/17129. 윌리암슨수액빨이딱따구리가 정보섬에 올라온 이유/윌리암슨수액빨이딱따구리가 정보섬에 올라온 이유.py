# 백준 17129

import io
from collections import deque
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def findPos(N, M, grid):
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 2:
                return [y, x]


def BFS(N, M, grid, start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((start[0], start[1], 0))
    grid[start[0]][start[1]] = 1

    while q:
        curY, curX, move = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < M and 0 <= nextY < N and grid[nextY][nextX] != 1:
                if grid[nextY][nextX] in {3, 4, 5}:
                    return ['TAK', move+1]
                q.append((nextY, nextX, move+1))
                grid[nextY][nextX] = 1

    return ['NIE']


def solve(N, M, A):
    start = findPos(N, M, A)
    return BFS(N, M, A, start)


def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().decode().strip())) for _ in range(N)]

    for i in solve(N, M, A):
        print(i)


main()
