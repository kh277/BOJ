# 백준 7569

'''
백준 7576의 3차원 버전이다.
'''

import sys
from collections import deque

input = sys.stdin.readline

pointX = [-1, 1, 0, 0, 0, 0]
pointY = [0, 0, -1, 1, 0, 0]
pointZ = [0, 0, 0, 0, -1, 1]


def solve(M: int, N: int, H: int, graph: list) -> list:
    pointX = [-1, 1, 0, 0, 0, 0]
    pointY = [0, 0, -1, 1, 0, 0]
    pointZ = [0, 0, 0, 0, -1, 1]

    q = deque()

    # 익은 토마토의 위치 판단
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    q.append([i, j, k, 0])

    # 큐가 빌 때까지 반복
    day = 0
    while q:
        temp = q.popleft()
        if temp[3] > day:
            day = temp[3]

        # 상하좌우 탐색 가능한지 확인
        for i in range(6):
            nextZ = temp[0] + pointZ[i]
            nextY = temp[1] + pointY[i]
            nextX = temp[2] + pointX[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= nextX < M and 0 <= nextY < N and 0 <= nextZ < H and graph[nextZ][nextY][nextX] == 0:
                graph[nextZ][nextY][nextX] = 1
                q.append([nextZ, nextY, nextX, temp[3]+1])
    
    # 익은 토마토의 위치 판단
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    return -1

    return day


def main():
    M, N, H = map(int, input().split())
    graph = [[[] for i in range(N)] for _ in range(H)]

    for i in range(H):
        for j in range(N):
            graph[i][j] = list(map(int, input().split()))

    print(solve(M, N, H, graph))


main()
