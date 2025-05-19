# 백준 25513

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(startP, grid, target):
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append([startP[0], startP[1], 0])
    visited[startP[0]][startP[1]] = True

    while q:
        curY, curX, moveCount = q.popleft()

        if curY == target[0] and curX == target[1]:
            return moveCount

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < 5 and 0 <= nextY < 5 and visited[nextY][nextX] == False and grid[nextY][nextX] != -1:
                q.append([nextY, nextX, moveCount+1])
                visited[nextY][nextX] = True
    
    return -1


def solve(grid, r, c):
    dic = dict()
    # 시작 위치 파악
    for y in range(5):
        for x in range(5):
            if grid[y][x] in {1, 2, 3, 4, 5, 6}:
                dic[grid[y][x]] = [y, x]

    # BFS 6번 반복
    result = 0
    startP = [r, c]
    for i in range(1, 7):
        moveCount = BFS(startP, grid, dic[i])
        if moveCount == -1:
            return -1
        startP = dic[i]
        result += moveCount
    
    return result


def main():
    grid = []
    for _ in range(5):
        grid.append(list(map(int, input().split())))
    r, c = map(int, input().split())
    print(solve(grid, r, c))

main()
