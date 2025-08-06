# 백준 2823

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(X, Y, grid):
    for curY in range(Y):
        for curX in range(X):
            if grid[curY][curX] == '.':
                canMove = 0
                for i in range(4):
                    nextX = curX + dx[i]
                    nextY = curY + dy[i]
                    if grid[nextY][nextX] == '.':
                        canMove += 1
                if canMove < 2:
                    return 1

    return 0


def main():
    Y, X = map(int, input().split())
    grid = []
    grid.append(['X'] * (X+2))
    for _ in range(Y):
        grid.append(['X'] + list(input().decode().rstrip()) + ['X'])
    grid.append(['X'] * (X+2))
    print(solve(X+2, Y+2, grid))



main()
