# 백준 34295

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def BFS(Y, X, grid, start, end):
    visited = [[[0, 0] for _ in range(X)] for _ in range(Y)]
    q = deque()
    q.append((start[0], start[1], 0, 0))
    q.append((start[0], start[1], 1, 0))
    visited[start[0]][start[1]][0] = 1
    visited[start[0]][start[1]][1] = 1

    while q:
        curY, curX, curW, moveC = q.popleft()

        # 종료지점 체크
        if curY == end[0] and curX == end[1]:
            return moveC
        
        for i in range(8):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < X and 0 <= nextY < Y:
                # 이전 방향 체크
                nextW = -1
                if grid[curY][curX] < grid[nextY][nextX] and curW == 0:
                    nextW = 1
                elif grid[curY][curX] > grid[nextY][nextX] and curW == 1:
                    nextW = 0

                if nextW != -1 and visited[nextY][nextX][nextW] == 0:
                    visited[nextY][nextX][nextW] = 1
                    q.append((nextY, nextX, nextW, moveC+1))

    return -1


def main():
    Y, X = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(map(int, input().split())))
    a, b, c, d = map(int, input().split())

    print(BFS(Y, X, grid, (a-1, b-1), (c-1, d-1)))


main()
