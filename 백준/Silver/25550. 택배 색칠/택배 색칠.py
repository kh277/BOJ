# 백준 25550

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def solve(N, M, grid):
    result = [[max(0, grid[y+1][x+1]-1) for x in range(M)] for y in range(N)]

    for y in range(N):
        for x in range(M):
            for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                result[y-1][x-1] = min(result[y-1][x-1], grid[y+dy][x+dx])
    
    return sum([sum(i) for i in result])


def main():
    N, M = map(int, input().split())
    grid = [[0 for _ in range(M+2)]]
    for _ in range(N):
        grid.append([0] + list(map(int, input().split())) + [0])
    grid.append([0 for _ in range(M+2)])
    print(solve(N, M, grid))


main()
