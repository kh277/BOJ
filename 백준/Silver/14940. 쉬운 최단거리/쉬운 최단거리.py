# 백준 14940

import io
from array import array
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(H, W, start, grid):
    visited = [[0 for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append([start[0], start[1], 0])

    while q:
        curY, curX, count = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < W and 0 <= nextY < H and grid[nextY][nextX] == 1 and visited[nextY][nextX] == 0:
                q.append([nextY, nextX, count+1])
                visited[nextY][nextX] = count+1
    
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = -1

    return visited


def solve(H, W, grid):
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 2:
                return BFS(H, W, [y, x], grid)


def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))
    
    for i in solve(H, W, grid):
        print(*i)


main()
