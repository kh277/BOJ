# 백준 34661

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

def solve(N, M, grid):
    result = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == '.':
                result += 1

    if result % 2 == 1:
        return 'sewon'
    return 'pizza'


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        grid = []
        for _ in range(N):
            grid.append(list(input().decode().strip()))
        print(solve(N, M, grid))


main()
