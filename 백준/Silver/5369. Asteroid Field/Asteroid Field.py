# 백준 5369

'''
좌상단의 s에서 우하단의 d까지 소행성 *를 피해서 도착할 때, 이동 거리의 최소값을 구하는 문제이다.
'''

import sys
from collections import deque

input = sys.stdin.readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


def BFS():
    visited = [[False for _ in range(N)] for _ in range(N)]

    q = deque()
    q.append([0, 0, 0])
    visited[0][0] = True

    while q:
        curY, curX, curCount = q.popleft()

        if curX == N-1 and curY == N-1:
            return curCount

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < N and 0 <= nextY < N and visited[nextY][nextX] == False:
                if grid[nextY][nextX] != '*':
                    q.append([nextY, nextX, curCount+1])
                    visited[nextY][nextX] = True
    
    return -1


# main 함수 ----------
T = int(input())
for _ in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(input().rstrip()))
    print(BFS())