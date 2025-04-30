# 백준 20002

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def solve(N, grid):
    # 1. 계산에 사용할 누적 합 계산
    accSum = [[0 for _ in range(N)] for _ in range(N)]
    accSum[0][0] = grid[0][0]

    for x in range(1, N):
        accSum[0][x] = accSum[0][x-1] + grid[0][x]
    for y in range(1, N):
        accSum[y][0] = accSum[y-1][0] + grid[y][0]
    for y in range(1, N):
        for x in range(1, N):
            accSum[y][x] = grid[y][x] + accSum[y-1][x] + accSum[y][x-1] - accSum[y-1][x-1]

    # 2. 누적 합을 이용해 최대값 탐색
    result = -INF
    for size in range(N+1):
        for endX in range(size, N):
            for endY in range(size, N):
                startX = endX-size
                startY = endY-size
                
                curSum = accSum[endY][endX]
                if startX >= 1 and startY >= 1:
                    curSum += accSum[startY-1][startX-1]
                if startX >= 1:
                    curSum -= accSum[endY][startX-1]
                if startY >= 1:
                    curSum -= accSum[startY-1][endX]

                result = max(result, curSum)
    
    return result


def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    print(solve(N, grid))


main()
