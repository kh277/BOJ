# 백준 2573

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


# cur칸이 몇 칸이나 녹을 수 있는지 체크
def checkMelt(N, M, cur, grid):
    count = 0
    for i in range(4):
        nextX = cur[1] + pointX[i]
        nextY = cur[0] + pointY[i]
        if 0 <= nextX < M and 0 <= nextY < N and grid[nextY][nextX] == 0:
            count += 1

    return count


# 연결된 빙하 탐색
def BFS(N, M, start, grid, visited):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        curY, curX = q.popleft()
        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                if grid[nextY][nextX] > 0:
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True


def solve(N, M, grid):
    year = 0
    while True:
        # 섬의 개수 세기
        count = 0
        visited = [[False for _ in range(M)] for _ in range(N)]
        for y in range(N):
            for x in range(M):
                if visited[y][x] == False and grid[y][x] != 0:
                    BFS(N, M, [y, x], grid, visited)
                    count += 1

        # 섬의 개수 체크
        if count == 0:
            return 0
        if count > 1:
            return year

        # 녹을 수 있는 칸 체크
        melt = []
        for y in range(N):
            for x in range(M):
                if grid[y][x] > 0:
                    temp = checkMelt(N, M, [y, x], grid)
                    if temp != 0:
                        melt.append([y, x, temp])

        # 녹이기
        for curY, curX, meltCount in melt:
            grid[curY][curX] = max(0, grid[curY][curX] - meltCount)
        
        year += 1


def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    print(solve(N, M, grid))


main()
