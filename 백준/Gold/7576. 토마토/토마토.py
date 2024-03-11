# 백준 7576

'''
처음 토마토가 놓은 곳을 시작점으로 그래프 탐색을 하되,
토마토는 상하좌우 1칸씩 영향을 주므로 BFS를 사용하면 된다.

토마토가 여러 개 존재하는 경우 시작점을 여러 개 입력하면 된다.
'''

import sys
from collections import deque

input = sys.stdin.readline

pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


def solve(M: int, N: int, graph: list) -> int:
    tomato = []

    # 익은 토마토의 위치 판단
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                tomato.append([i, j, 0])

    # BFS의 시작점에 익은 토마토 위치 추가
    q = deque()
    for i in tomato:
        q.append(i)

    # 큐가 빌 때까지 반복
    day = 0
    while q:
        temp = q.popleft()
        day = temp[2]

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            X = temp[0] + pointX[i]
            Y = temp[1] + pointY[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= X < N and 0 <= Y < M and graph[X][Y] != 1 and graph[X][Y] != -1:
                graph[X][Y] = 1
                q.append([X, Y, temp[2]+1])

    # 탐색하지 않은 지점이 있는지 확인
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
    return day


def main():
    M, N = map(int, input().split())
    graph = [0 for _ in range(N)]

    for i in range(N):
        graph[i] = list(map(int, input().split()))

    print(solve(M, N, graph))


main()
