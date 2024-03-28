# 백준 2178

'''
가로 N, 세로 M 크기의 격자에서 BFS 실행
좌상단 모서리 -> 우하단 모서리로 가는데 몇번의 사이클이 필요한지 구하기
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(M: int, N: int, graph: list, x: int, y: int) -> int:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    q = deque()
    q.append([y, x, 1])

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()

        if temp[0] == N-1 and temp[1] == M-1:
            return temp[2]

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            nextY = temp[0] + pointY[i]
            nextX = temp[1] + pointX[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= nextX < M and 0 <= nextY < N and graph[nextY][nextX] == 1:
                graph[nextY][nextX] = 0
                q.append([nextY, nextX, temp[2]+1])


def main():
    N, M = map(int, input().split())
    graph = [None for _ in range(N)]

    for i in range(N):
        graph[i] = list(map(int, input().rstrip()))

    print(BFS(M, N, graph, 0, 0))

main()
