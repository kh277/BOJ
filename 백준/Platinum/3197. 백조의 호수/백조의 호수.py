# 백준 3197

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(Y, X, grid):
    # 백조의 초기 위치 저장
    swan = []
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 'L':
                swan.append((y, x))

    visited = [[0] * X for _ in range(Y)]
    swanQ = deque()
    swanNextQ = deque()
    waterQ = deque()
    waterNextQ = deque()

    # 백조와 물의 초기 위치 큐에 추가
    swanQ.append(swan[0])
    visited[swan[0][0]][swan[0][1]] = 1
    for y in range(Y):
        for x in range(X):
            if grid[y][x] != 'X':
                waterQ.append((y, x))

    day = 0
    while True:
        # 백조 이동 BFS
        while swanQ:
            curY, curX = swanQ.popleft()

            for i in range(4):
                nextX = curX + dx[i]
                nextY = curY + dy[i]
                if 0 <= nextX < X and 0 <= nextY < Y and visited[nextY][nextX] == 0:
                    visited[nextY][nextX] = 1

                    # 백조를 만난 경우
                    if nextX == swan[1][1] and nextY == swan[1][0]:
                        return day
                    # 다음날 이동 가능한 칸인 경우
                    if grid[nextY][nextX] == 'X':
                        swanNextQ.append((nextY, nextX))
                    # 지금 이동 가능한 칸인 경우
                    else:
                        swanQ.append((nextY, nextX))

        # 얼음 녹이기 BFS
        while waterQ:
            curY, curX = waterQ.popleft()

            for i in range(4):
                nextX = curX + dx[i]
                nextY = curY + dy[i]
                if 0 <= nextX < X and 0 <= nextY < Y and grid[nextY][nextX] == 'X':
                    grid[nextY][nextX] = '.'
                    waterNextQ.append((nextY, nextX))

        # 다음날 처리
        swanQ = swanNextQ
        swanNextQ = deque()
        waterQ = waterNextQ
        waterNextQ = deque()
        day += 1


def main():
    Y, X = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(input().decode().strip()))

    print(solve(Y, X, grid))


main()
