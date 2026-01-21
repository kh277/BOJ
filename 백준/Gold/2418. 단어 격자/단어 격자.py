# 백준 2418

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def solve(Y, X, L, grid, string):
    DP = [[[0] * L for _ in range(X)] for _ in range(Y)]

    for y in range(Y):
        for x in range(X):
            if grid[y][x] == string[0]:
                DP[y][x][0] = 1

    for l in range(1, L):
        prevC = string[l-1]
        curC = string[l]
        for curY in range(Y):
            for curX in range(X):
                if grid[curY][curX] == curC:
                    for i in range(8):
                        prevY = curY + dy[i]
                        prevX = curX + dx[i]
                        if 0 <= prevY < Y and 0 <= prevX < X and grid[prevY][prevX] == prevC:
                            DP[curY][curX][l] += DP[prevY][prevX][l-1]

    result = 0
    for y in range(Y):
        for x in range(X):
            result += DP[y][x][l]

    return result


def main():
    Y, X, L = map(int, input().split())
    grid = []
    for i in range(Y):
        grid.append(list(input().decode().strip()))
    string = input().decode().strip()
    print(solve(Y, X, L, grid, string))


main()
