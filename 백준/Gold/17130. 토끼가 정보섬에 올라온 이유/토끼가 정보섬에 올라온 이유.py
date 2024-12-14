# 백준 17130

'''
DP[y][x] = grid[y][x]까지 도착했을 때, 얻을 수 있는 당근의 최대 개수
'''

import sys
from collections import deque

input = sys.stdin.readline
pointX = [1, 1, 1]
pointY = [-1, 0, 1]


# 토끼가 방문 가능한 지점을 체크
def canVisit(startY, startX, visited):
    q = deque()
    q.append([startY, startX])
    visited[startY][startX] = True

    while q:
        curY, curX = q.popleft()
        for i in range(3):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                if grid[nextY][nextX] != '#':
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True
    
    return visited


# 토끼가 얻을 수 있는 당근 수 체크
def checkDP(startX, DP, visited):
    for curX in range(startX+1, M):
        for curY in range(N):
            if grid[curY][curX] == '#' and visited[curY][curX] == False:
                continue
            for i in range(3):
                beforeX = curX - pointX[i]
                beforeY = curY - pointY[i]
                if 0 <= beforeX < M and 0 <= beforeY < N and visited[beforeY][beforeX] == True:
                    if grid[beforeY][beforeX] == '#':
                        continue
                    elif grid[curY][curX] == 'C':
                        DP[curY][curX] = max(DP[curY][curX], DP[beforeY][beforeX]+1)
                    else:
                        DP[curY][curX] = max(DP[curY][curX], DP[beforeY][beforeX])

    return DP


def solve():
    DP = [[-1 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    # 토끼의 위치 파악 후 BFS 탐색
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 'R':
                DP[y][x] = 0
                visited = canVisit(y, x, visited)
                DP = checkDP(x, DP, visited)

    result = -1
    # 쪽문의 위치 파악 후 최대값 저장
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 'O' and visited[y][x] == True:
                result = max(result, DP[y][x])

    return result


# main 함수 ----------
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

print(solve())