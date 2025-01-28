# 백준 7562

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    grid = [[0 for _ in range(l)] for _ in range(l)]
    pointX = [2, 2, 1, 1, -1, -1, -2, -2]
    pointY = [1, -1, 2, -2, 2, -2, 1, -1]

    q = deque()
    q.append([start[0], start[1], 0])
    
    while q:
        curY, curX, curCount = q.popleft()

        if end[0] == curY and end[1] == curX:
            return curCount

        for i in range(8):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < l and 0 <= nextY < l and grid[nextY][nextX] == 0:
                q.append([nextY, nextX, curCount+1])
                grid[nextY][nextX] = curCount+1


# main 함수 ----------
T = int(input())
for _ in range(T):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    print(solve())