# 백준 5048

import sys
from collections import deque

input = sys.stdin.readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


# Player의 위치 체크
def findPlayer():
    for y in range(1, H-1):
        for x in range(1, W-1):
            if grid[y][x] == 'P':
                return [y, x]


# curPos 상하좌우에 Trap이 존재하는지 체크
def checkTrap(curPos):
    for i in range(4):
        nextX = curPos[1] + pointX[i]
        nextY = curPos[0] + pointY[i]
        if grid[nextY][nextX] == 'T':
            return True
    
    return False


def BFS(start):
    visited = [[False for _ in range(W)] for _ in range(H)]
    goldCount = 0

    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        curY, curX = q.popleft()

        # 현재 위치에 금이 존재한다면
        if grid[curY][curX] == 'G':
            goldCount += 1

        # 주변에 Trap이 존재한다면
        if checkTrap([curY, curX]) == True:
            continue

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if grid[nextY][nextX] != '#' and visited[nextY][nextX] == False:
                q.append([nextY, nextX])
                visited[nextY][nextX] = True
    
    return goldCount


# main 함수 ----------
W, H = map(int, input().split())
grid = []
for _ in range(H):
    grid.append(list(input().rstrip()))

print(BFS(findPlayer()))
