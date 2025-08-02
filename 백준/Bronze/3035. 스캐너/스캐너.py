# 백준 3035

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(R, C, ZR, ZC, grid):
    result = [[None for _ in range(C*ZC)] for _ in range(R*ZR)]
    for y in range(R*ZR):
        for x in range(C*ZC):
            result[y][x] = grid[y//ZR][x//ZC]

    return result


def main():
    R, C, ZR, ZC = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(input().decode().rstrip()))
    for i in solve(R, C, ZR, ZC, grid):
        print(''.join(i))


main()
