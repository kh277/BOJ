# 백준 33754

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, grid):
    result = 2
    for x in range(1, N):
        if grid[0][x] == 0:
            result = 1
            if grid[1][x-1] == 0 or grid[1][x] == 0:
                return 0
        if grid[1][x] == 0:
            result = 1
            if grid[0][x-1] == 0:
                return 0

    return result


def main():
    N = int(input())
    grid = []
    for i in range(2):
        grid.append(list(map(int, input().split())))
    print(solve(N, grid))


main()
