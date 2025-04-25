# 백준 22352

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, M, start, grid):
    startNum = grid[start[0]][start[1]]
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    changeGrid = [start]

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                if grid[nextY][nextX] == startNum:
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True
                    changeGrid.append([nextY, nextX])

    return changeGrid


def solve(N, M, before, after):
    count = 0
    for y in range(N):
        for x in range(M):
            if before[y][x] != -1 and before[y][x] != after[y][x]:
                # 두 번째 바뀐 구간이 발견된 경우
                if count == 1:
                    return 'NO'
                # 바뀐 구간 반영
                for cY, cX in BFS(N, M, [y, x], before):
                    before[cY][cX] = after[y][x]
                count += 1

    # 하나도 안 바뀐 경우
    if count == 0:
        return 'YES'

    # 바뀐 전후로 차이가 있는지 체크
    for y in range(N):
        for x in range(M):
            if before[y][x] != after[y][x]:
                return 'NO'

    return 'YES'


def main():
    N, M = map(int, input().split())
    before = []
    for _ in range(N):
        before.append(list(map(int, input().split())))
    
    after = []
    for _ in range(N):
        after.append(list(map(int, input().split())))
    
    print(solve(N, M, before, after))


main()