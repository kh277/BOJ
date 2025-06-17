# 백준 28015

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(M, grid):
    count = 0
    result = [0 for _ in range(M)]

    # 0이 아닐 경우 0이 나오기 전까지 칠하기
    curI = 0
    while curI < M:
        if grid[curI] == 0:
            curI += 1
            continue

        count += 1
        curColor = grid[curI]
        for nextI in range(curI, M):
            if grid[nextI] == 0:
                break 
            result[nextI] = curColor
        curI = nextI+1

    # result에서 다른 부분이 있을 경우 최소 횟수로 칠하기
    curI = 0
    while curI < M:
        if grid[curI] == result[curI]:
            curI += 1
            continue

        result[curI] = grid[curI]
        count += 1
        for nextI in range(curI+1, M):
            if grid[nextI] == result[nextI]:
                break
            result[nextI] = grid[curI]
        curI = nextI+1

    return count


def main():
    N, M = map(int, input().split())
    count = 0
    for _ in range(N):
        count += solve(M, list(map(int, input().split())))
    print(count)


main()
