# 백준 14716

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def BFS(X, Y, start, grid, visited):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        curY, curX = q.popleft()

        for i in range(8):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < X and 0 <= nextY < Y and visited[nextY][nextX] == False and grid[nextY][nextX] == 1:
                q.append([nextY, nextX])
                visited[nextY][nextX] = True


def solve(X, Y, grid):
    visited = [[False for _ in range(X)] for _ in range(Y)]

    count = 0
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 1 and visited[y][x] == False:
                BFS(X, Y, [y, x], grid, visited)
                count += 1

    return count


def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))

    print(solve(W, H, grid))


main()
