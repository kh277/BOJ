# 백준 2169

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(Y, X, grid):
    DP = [[0] * X for _ in range(Y)]

    # Y=0 처리
    DP[0][0] = grid[0][0]
    for x in range(1, X):
        DP[0][x] = DP[0][x-1] + grid[0][x]

    # 1<=Y<N 처리
    for y in range(1, Y):
        # 왼쪽 -> 오른쪽 처리
        left = [0] * X
        left[0] = DP[y-1][0] + grid[y][0]
        for x in range(1, X):
            left[x] = max(DP[y-1][x]+grid[y][x], left[x-1]+grid[y][x])

        # 오른쪽 -> 왼쪽 처리
        right = [0] * X
        right[X-1] = DP[y-1][X-1] + grid[y][X-1]
        for x in range(X-2, -1, -1):
            right[x] = max(DP[y-1][x]+grid[y][x], right[x+1]+grid[y][x])

        # DP에 반영
        for x in range(X):
            DP[y][x] = max(left[x], right[x])

    return DP[Y-1][X-1]


def main():
    Y, X = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(map(int, input().split())))
    print(solve(Y, X, grid))


main()
