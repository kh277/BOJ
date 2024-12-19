# 백준 3184

import sys
from collections import deque

input = sys.stdin.readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


def BFS(startY, startX, visited):
    sheep = 0
    wolf = 0

    q = deque()

    if grid[startY][startX] == '#':
        return 0, 0
    elif grid[startY][startX] == 'v':
        wolf += 1
    elif grid[startY][startX] == 'o':
        sheep += 1
    q.append([startY, startX])
    visited[startY][startX] = True
    
    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                if grid[nextY][nextX] != '#':
                    if grid[nextY][nextX] == 'v':
                        wolf += 1
                    elif grid[nextY][nextX] == 'o':
                        sheep += 1
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True

    return [sheep, wolf]


def solve():
    leftSheep = 0
    leftWolf = 0

    visited = [[False for _ in range(M)] for _ in range(N)]

    # 상하 모서리 visited 처리
    for y in range(N):
        if visited[y][0] == False:
            BFS(y, 0, visited)
        if visited[y][M-1] == False:
            BFS(y, M-1, visited)

    # 좌우 모서리 visited 처리
    for x in range(M):
        if visited[0][x] == False:
            BFS(0, x, visited)
        if visited[N-1][x] == False:
            BFS(N-1, x, visited)

    # 모서리가 아닌 내부 영역에서 양과 늑대의 수 체크
    for y in range(1, N-1):
        for x in range(1, M-1):
            if visited[y][x] == False:
                a, b = BFS(y, x, visited)
                if a > b:
                    leftSheep += a
                else:
                    leftWolf += b
    
    return [leftSheep, leftWolf]


# main 함수 ----------
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

print(*solve())