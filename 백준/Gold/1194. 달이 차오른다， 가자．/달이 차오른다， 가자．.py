# 백준 1194

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 1000000


def BFS(Y, X, grid, start):
    q = deque()
    visited = [[[INF] * (64) for _ in range(X)] for _ in range(Y)]
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]][0] = 0

    while q:
        curY, curX, curS = q.popleft()
        nextT = visited[curY][curX][curS] + 1

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if not (0 <= nextX < X and 0 <= nextY < Y):
                continue

            nextData = grid[nextY][nextX]

            # 다음 칸이 출구라면
            if nextData == 49:
                return nextT

            # 다음 칸이 빈 칸이라면
            elif (nextData == 46 or nextData == 48) and visited[nextY][nextX][curS] > nextT:
                q.append((nextY, nextX, curS))
                visited[nextY][nextX][curS] = nextT
            
            # 다음 칸이 열쇠라면
            elif 97 <= nextData <= 102:
                nextS = curS | (1<<(nextData-97))
                if visited[nextY][nextX][nextS] > nextT:
                    q.append((nextY, nextX, nextS))
                    visited[nextY][nextX][nextS] = nextT
            
            # 다음 칸이 접근 가능한 문이라면
            elif 65 <= nextData <= 70 and curS & (1<<(nextData-65)):
                if visited[nextY][nextX][curS] > nextT:

                    q.append((nextY, nextX, curS))
                    visited[nextY][nextX][curS] = nextT

    return -1


def solve(Y, X, grid):
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 48:
                return BFS(Y, X, grid, (y, x))


def main():
    Y, X = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(input().strip()))
    print(solve(Y, X, grid))


main()
