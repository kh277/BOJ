# 백준 11658

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def init(N, grid, accSum):
    for y in range(N):
        accSum[y][0] = grid[y][0]
        for x in range(1, N):
            accSum[y][x] = accSum[y][x-1] + grid[y][x]


def update(N, grid, accSum, x1, y1, value):
    gap = value - grid[y1][x1]
    grid[y1][x1] += gap
    for x in range(x1, N):
        accSum[y1][x] += gap


def query(N, accSum, x1, y1, x2, y2):
    result = 0
    for y in range(y1, y2+1):
        result += accSum[y][x2]
        if x1 != 0:
            result -= accSum[y][x1-1]

    return result


def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    # 누적 합 배열 전처리
    accSum = [[0] * N for _ in range(N)]
    init(N, grid, accSum)

    # 쿼리 처리
    for _ in range(M):
        w, *q = map(int, input().split())
        if w == 0:
            update(N, grid, accSum, q[1]-1, q[0]-1, q[2])
        else:
            print(query(N, accSum, q[1]-1, q[0]-1, q[3]-1, q[2]-1))


main()
