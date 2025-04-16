# 백준 29718

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, grid, A):
    sumClap = [0 for _ in range(M)]
    for x in range(M):
        for y in range(N):
            sumClap[x] += grid[y][x]

    window = sum(sumClap[:A])
    result = window
    for x in range(M-A):
        window = window - sumClap[x] + sumClap[x+A]
        result = max(result, window)

    return result


def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    A = int(input())

    print(solve(N, M, grid, A))


main()
