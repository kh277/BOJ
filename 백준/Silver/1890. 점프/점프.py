# 백준 1890

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, grid):
    DP = [[0 for _ in range(N)] for _ in range(N)]
    DP[0][0] = 1

    for y in range(N):
        for x in range(N):
            if y == N-1 and x == N-1:
                continue
            delta = grid[y][x]
            if y+delta < N:
                DP[y+delta][x] += DP[y][x]
            if x+delta < N:
                DP[y][x+delta] += DP[y][x]

    return DP[N-1][N-1]


def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    print(solve(N, grid))


main()
