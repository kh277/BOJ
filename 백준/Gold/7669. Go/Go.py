# 백준 7669

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


def BFS(grid, start, otherStoneType):
    visited = set()

    q = deque()
    q.append(start)
    visited.add((start[0], start[1]))

    result = 1
    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if grid[nextY][nextX] == 0 and (nextY, nextX) not in visited:
                q.append([nextY, nextX])
                visited.add((nextY, nextX))
                result += 1
            elif grid[nextY][nextX] == otherStoneType:
                return set(), 0

    return visited, result


def solve(N, blackPos, whitePos):
    # 0(빈칸), 1(검은 돌), 2(흰 돌), 3(중립 돌)로 표시
    grid = [[0 for _ in range(N+2)] for _ in range(N+2)]

    # 가장 외곽에 중립 돌 추가
    for i in range(N+2):
        grid[0][i] = 3
        grid[N+1][i] = 3
        grid[i][0] = 3
        grid[i][N+1] = 3
    
    # 검은 돌과 흰 돌의 위치 표시
    for y, x in blackPos:
        grid[y][x] = 1
    for y, x in whitePos:
        grid[y][x] = 2

    # 검은 돌 계산
    visited = set()
    blackResult = 0
    for y in range(1, N+2):
        for x in range(1, N+2):
            if grid[y][x] == 0 and (y, x) not in visited:
                curVisited, curBlackResult = BFS(grid, [y, x], 2)
                visited = visited | curVisited
                blackResult += curBlackResult

    # 흰 돌 계산
    visited = set()
    whiteResult = 0
    for y in range(1, N+2):
        for x in range(1, N+2):
            if grid[y][x] == 0 and (y, x) not in visited:
                curVisited, curWhiteResult = BFS(grid, [y, x], 1)
                visited = visited | curVisited
                whiteResult += curWhiteResult

    if blackResult < whiteResult:
        return 'White wins by {}'.format(whiteResult-blackResult)
    elif blackResult > whiteResult:
        return 'Black wins by {}'.format(blackResult-whiteResult)
    else:
        return 'Draw'


# main 함수 ----------
while True:
    while True:
        line = input().strip()
        if line:
            break
    temp = list(map(int, line.split()))
    if temp[0] == 0:
        break
    N, B, W = temp

    if B > 0:
        while True:
            line = input().strip()
            if line:
                break
        blackInput = list(map(int, line.split()))
        blackPos = [[blackInput[i], blackInput[i+1]] for i in range(0, B*2, 2)]
    else:
        input()
        blackPos = []

    if W > 0:
        while True:
            line = input().strip()
            if line:
                break
        whiteInput = list(map(int, line.split()))
        whitePos = [[whiteInput[i], whiteInput[i+1]] for i in range(0, W*2, 2)]
    else:
        input()
        whitePos = []

    print(solve(N, blackPos, whitePos))