# 백준 2636

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


def checkAir():
    result = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = True

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                if graph[nextY][nextX] == 0:
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True
                else:
                    result[nextY][nextX] = True
    
    return result


def solve():
    count = 0
    beforeCount = sum([sum(x) for x in graph])

    while True:
        count += 1

        # 1. 공기와 한 면 이상 접한 치즈 체크
        delList = checkAir()
        
        # 2. 공기와 한 면 이상 접한 치즈 제거
        for y in range(N):
            for x in range(M):
                if delList[y][x] == True:
                    graph[y][x] = 0

        # 3. 남은 치즈 체크
        leftCheese = 0
        for y in range(N):
            for x in range(M):
                if graph[y][x] == 1:
                    leftCheese += 1
        
        if leftCheese == 0:
            break
        beforeCount = leftCheese
    
    return [count, beforeCount]


# main 함수 ----------
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in solve():
    print(i)
