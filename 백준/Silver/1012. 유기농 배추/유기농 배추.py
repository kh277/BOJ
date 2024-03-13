# 백준 1012

'''
이 문제는 주어진 필드에서 섬의 개수를 구하는 것과 같다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(M: int, N: int, graph: list, x: int, y: int) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    q = deque()
    q.append([y, x])

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            nextY = temp[0] + pointY[i]
            nextX = temp[1] + pointX[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= nextX < M and 0 <= nextY < N and graph[nextY][nextX] == 1:
                graph[nextY][nextX] = 0
                q.append([nextY, nextX])

    return graph


def solve(M: int, N: int, K: int, graph: list) -> int:
    count = 0

    # 전체 그래프에 대해 탐색
    for i in range(M):
        for j in range(N):
            # 양배추가 존재할 경우 BFS 탐색
            if graph[j][i] == 1:
                graph = BFS(M, N, graph, i, j)
                count += 1

    return count


def main():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [[0 for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            x, y = map(int, input().split())
            graph[y][x] = 1

        print(solve(M, N, K, graph))

main()
