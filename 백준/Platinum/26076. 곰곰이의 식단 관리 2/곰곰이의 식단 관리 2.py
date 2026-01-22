# 백준 26076

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]


def BFS(Y, X, grid, start, wallType):
    q = deque()
    q.append(start)
    grid[start[0]][start[1]] = wallType

    while q:
        curY, curX = q.popleft()

        for i in range(8):
            nextY = curY + dy[i]
            nextX = curX + dx[i]

            if 0 <= nextX < X and 0 <= nextY < Y and grid[nextY][nextX] == 1:
                q.append((nextY, nextX))
                grid[nextY][nextX] = wallType


def solve(Y, X, grid):
    grid[1][1] = 9
    grid[Y-2][X-2] = 9

    # 왼쪽, 아래쪽 벽과 이어진 장애물을 2로, 위쪽, 오른쪽 벽과 이어진 장애물을 3으로 체크
    leftType = 2
    rightType = 3
    BFS(Y, X, grid, [0, X-1], leftType)
    if grid[Y-1][0] == 1:
        BFS(Y, X, grid, [Y-1, 0], rightType)

    # 장애물을 설치하지 않아도 이어진 경우
    if grid[0][X-1] == grid[Y-1][0]:
        return 0

    # 장애물을 1칸만 설치해도 이어지는 경우 체크
    for y in range(1, Y-1):
        for x in range(1, X-1):
            # 0인 칸 8방향에 2와 3이 동시에 있는지 체크
            if grid[y][x] == 0:
                isTwo = 0
                isThree = 0
                for i in range(8):
                    nextT = grid[y+dy[i]][x+dx[i]]
                    if nextT == 2:
                        isTwo = 1
                    elif nextT == 3:
                        isThree = 1
                if isTwo + isThree == 2:
                    return 1

    # 그 외의 경우 전부 2
    return 2


def main():
    Y, X = map(int, input().split())
    grid = [[0, 0] + [1] * X]
    for _ in range(Y):
        grid.append([1] + list(map(int, input().split())) + [1])
    grid.append([1] * X + [0, 0])

    print(solve(Y+2, X+2, grid))


main()
