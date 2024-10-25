# 백준 5986

import sys
from collections import deque

input = sys.stdin.readline


def BFS(start, visited):
    pointX = [-1, 1, 0, 0, 0, 0]
    pointY = [0, 0, -1, 1, 0, 0]
    pointZ = [0, 0, 0, 0, -1, 1]

    q = deque()
    q.append(start)
    visited[start[0]][start[1]][start[2]] = True

    while q:
        curZ, curY, curX = q.popleft()

        for i in range(6):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            nextZ = curZ + pointZ[i]

            if 0 <= nextX < N and 0 <= nextY < N and 0 <= nextZ < N:
                if data[nextZ][nextY][nextX] == '*' and visited[nextZ][nextY][nextX] == False:
                    q.append([nextZ, nextY, nextX])
                    visited[nextZ][nextY][nextX] = True


def solve():
    visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(N)]
    result = 0

    for z in range(N):
        for y in range(N):
            for x in range(N):
                if data[z][y][x] == '*' and visited[z][y][x] == False:
                    BFS([z, y, x], visited)
                    result += 1
    
    return result


# main 함수 ----------
N = int(input())

data = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        data[i].append(list(input().rstrip()))

print(solve())