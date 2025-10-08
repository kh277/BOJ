# 백준 2447

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    grid = [['*' for _ in range(N)] for _ in range(N)]

    cur = N
    while cur > 1:
        for y in range(N):
            for x in range(N):
                if grid[y][x] == '*' and (y % cur == 1 and x % cur == 1) or ((y // cur) % 3 == 1 and (x // cur) % 3 == 1):
                    grid[y][x] = ' '
        cur //= 3
    
    return grid


def main():
    N = int(input())
    for i in solve(N):
        print(''.join(i))


main()
