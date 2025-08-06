# 백준 14546

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(X, Y, grid, start, end):
    # 타입 자체가 다른 경우
    if grid[start[0]][start[1]] != grid[start[0]][start[1]]:
        return 'NO'

    # BFS 탐색
    curType = grid[start[0]][start[1]]
    q = deque()
    q.append(start)
    grid[start[0]][start[1]] = 0

    while q:
        curY, curX = q.popleft()

        if end == [curY, curX]:
            return 'YES'

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < X and 0 <= nextY < Y and grid[nextY][nextX] == curType:
                q.append([nextY, nextX])
                grid[nextY][nextX] = 0

    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        X, Y, Sx, Sy, Ex, Ey = map(int, input().split())
        grid = []
        for _ in range(Y):
            grid.append(list(input().decode().rstrip()))

        print(BFS(X, Y, grid, [Y-Sy, Sx-1], [Y-Ey, Ex-1]))


main()
