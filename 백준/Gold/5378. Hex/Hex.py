# 백준 5378

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [0, 1, -1, 1, -1, 0]
dy = [-1, -1, 0, 0, 1, 1]


def BFS(N, grid, visited, start, end, curT):
    q = deque()
    for i in start:
        q.append(i)
        visited[i[0]][i[1]] = 1
    
    while q:
        cur = q.popleft()
        curY, curX = cur

        if cur in end:
            return True
        
        for i in range(6):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < N and 0 <= nextY < N and visited[nextY][nextX] == 0 and grid[nextY][nextX] == curT:
                q.append((nextY, nextX))
                visited[nextY][nextX] = 1

    return False


def solve(N, grid):
    blackS = []
    blackE = set()
    whiteS = []
    whiteE = set()
    for i in range(N):
        if grid[0][i] == 'B':
            blackS.append((0, i))
        if grid[N-1][i] == 'B':
            blackE.add((N-1, i))
        if grid[i][N-1] == 'W':
            whiteS.append((i, N-1))
        if grid[i][0] == 'W':
            whiteE.add((i, 0))

    visited = [[0] * N for _ in range(N)]
    if BFS(N, grid, visited, blackS, blackE, 'B') == True:
        return "Black wins"
    elif BFS(N, grid, visited, whiteS, whiteE, 'W') == True:
        return "White wins"
    return "Not finished"


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = []
        for _ in range(N):
            grid.append(list(input().decode().rstrip()))
        print(solve(N, grid))


main()
