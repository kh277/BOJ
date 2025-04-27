# 백준 2589

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, M, start, grid, visited):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    q = deque()
    q.append([start[0], start[1], 0])
    visited[start[0]][start[1]] = True
    maxD = 0

    while q:
        curY, curX, curD = q.popleft()
        maxD = max(maxD, curD)
        
        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                if grid[nextY][nextX] == 'L':
                    q.append([nextY, nextX, curD+1])
                    visited[nextY][nextX] = True

    return maxD


def solve(N, M, grid):
    result = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 'L':
                temp = BFS(N, M, [y, x], grid, [[False for _ in range(M)] for _ in range(N)])
                result = max(result, temp)

    return result


def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(input().decode().strip()))

    print(solve(N, M, grid))


main()
