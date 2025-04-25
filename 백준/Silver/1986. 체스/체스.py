# 백준 1986

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def checkQueen(N, M, start, grid):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    curY, curX = start

    for dy, dx in move:
        nextX = curX + dx
        nextY = curY + dy
        while 0 <= nextX < M and 0 <= nextY < N and grid[nextY][nextX] not in {1, 2, 3}:
            grid[nextY][nextX] = -1
            nextX += dx
            nextY += dy


def checkKnight(N, M, start, grid):
    move = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    curY, curX = start

    for dy, dx in move:
        nextX = curX + dx
        nextY = curY + dy
        if 0 <= nextX < M and 0 <= nextY < N and grid[nextY][nextX] not in {1, 2, 3}:
            grid[nextY][nextX] = -1


def solve(N, M, grid):
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1:
                checkQueen(N, M, [y, x], grid)
            elif grid[y][x] == 2:
                checkKnight(N, M, [y, x], grid)

    count = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 0:
                count += 1

    return count


def main():
    N, M = map(int, input().split())
    # 퀸 = 1, 나이트 = 2, 폰 = 3으로 저장
    grid = [[0 for _ in range(M)] for _ in range(N)]

    Q = list(map(int, input().split()))
    for i in range(1, len(Q), 2):
        grid[Q[i]-1][Q[i+1]-1] = 1

    K = list(map(int, input().split()))
    for i in range(1, len(K), 2):
        grid[K[i]-1][K[i+1]-1] = 2

    P = list(map(int, input().split()))
    for i in range(1, len(P), 2):
        grid[P[i]-1][P[i+1]-1] = 3

    print(solve(N, M, grid))


main()
