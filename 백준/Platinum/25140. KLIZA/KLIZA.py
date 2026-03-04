# 백준 25140

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
delta = [(1, 3), (0, 2, 4), (1, 5), (0, 4, 6), (1, 3, 5, 7), (2, 4, 8), (3, 7), (4, 6, 8), (5, 7)]


def solve(grid, curX):
    initStatus = ''.join(grid)
    end = "123456789"
    q = deque()
    visited = set()
    q.append((initStatus, curX, 0, ""))
    visited.add(initStatus)

    while q:
        status, curX, count, move = q.popleft()

        # 종료조건
        if status == end:
            return count, move

        # 위치 이동
        for nextX in delta[curX]:
            temp = list(status)
            temp[curX], temp[nextX] = temp[nextX], temp[curX]
            nextS = ''.join(temp)

            if nextS not in visited:
                q.append((nextS, nextX, count+1, move+nextS[curX]))
                visited.add(nextS)


def main():
    grid = []
    for _ in range(3):
        grid.extend(list(input().decode().split()))
    curX = 0
    for i in range(9):
        if grid[i] == 'X':
            grid[i] = '9'
            curX = i

    c, s = solve(grid, curX)
    print(c)
    if c != 0:
        print(*list(s))


main()
