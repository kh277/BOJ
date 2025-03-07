# 백준 14719

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 방문한 위치는 1로 표시
def BFS(X, start, grid):
    pointX = [-1, 1]
    q = deque()
    q.append(start)
    grid[start[0]][start[1]] = 2
    
    cantAcc = False
    result = 1
    while q:
        curY, curX = q.popleft()

        for i in range(2):
            nextX = curX + pointX[i]

            # 고일 수 있는 경우
            if 0 < nextX < X-1 and grid[curY][nextX] == 0:
                q.append([curY, nextX])
                grid[curY][nextX] = 2
                result += 1
            # 모서리가 0일 경우
            elif nextX == 0 or nextX == X-1:
                if grid[curY][nextX] == 0:
                    grid[curY][nextX] = 2
                    cantAcc = True

    return 0 if cantAcc == True else result


def solve(Y, X, block):
    grid = [[0 for _ in range(X)] for _ in range(Y)]

    for x in range(X):
        for y in range(block[x]):
            grid[y][x] = 1

    result = 0
    for y in range(Y):
        for x in range(1, X-1):
            if grid[y][x] == 0:
                result += BFS(X, [y, x], grid)

    return result


def main():
    H, W = map(int, input().split())
    block = list(map(int, input().split()))
    print(solve(H, W, block))


main()