# 백준 2638

import sys
from collections import deque

input = sys.stdin.readline
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
                    result[nextY][nextX] += 1
    
    return result


def solve():
    count = 0

    while True:
        count += 1

        # 1. 공기와 두 면 이상 접한 치즈 체크
        delList = checkAir()
        
        # 2. 공기와 두 면 이상 접한 치즈 제거
        for y in range(N):
            for x in range(M):
                if delList[y][x] >= 2:
                    graph[y][x] = 0

        # 3. 남은 치즈 체크
        leftCheese = 0
        for y in range(N):
            for x in range(M):
                if graph[y][x] == 1:
                    leftCheese += 1
        
        if leftCheese == 0:
            break
    
    return count


# main 함수 ----------
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

print(solve())
