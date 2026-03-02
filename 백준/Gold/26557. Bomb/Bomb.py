# 백준 26557

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1000000000
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]


def solve(Z, Y, X, grid, start, end):
    visited = [[[INF] * X for _ in range(Y)] for _ in range(Z)]
    dq = deque()
    dq.append((0, start[0], start[1], start[2]))
    visited[start[0]][start[1]][start[2]] = 0

    while dq:
        breakCount, curZ, curY, curX = dq.popleft()
        
        if curZ == end[0] and curY == end[1] and curX == end[2]:
            return breakCount
    
        for i in range(6):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            nextZ = curZ + dz[i]

            if 0 <= nextX < X and 0 <= nextY < Y and 0 <= nextZ < Z and visited[nextZ][nextY][nextX] > breakCount:
                if grid[nextZ][nextY][nextX] == '#':
                    dq.append((breakCount+1, nextZ, nextY, nextX))
                    visited[nextZ][nextY][nextX] = breakCount+1
                else:
                    dq.appendleft((breakCount, nextZ, nextY, nextX))
                    visited[nextZ][nextY][nextX] = breakCount


def main():
    T = int(input())
    for _ in range(T):
        Z, Y, X = map(int, input().split())
        grid = [[] for _ in range(Z)]
        for z in range(Z):
            for _ in range(Y):
                grid[z].append(list(input().decode().strip()))
        start = [0, 0, 0]
        end = [0, 0, 0]
        for z in range(Z):
            for y in range(Y):
                for x in range(X):
                    if grid[z][y][x] == 'S':
                        start = (z, y, x)
                    elif grid[z][y][x] == 'E':
                        end = (z, y, x)

        print(solve(Z, Y, X, grid, start, end))


main()
