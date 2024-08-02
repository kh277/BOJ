# 백준 1743

import sys
from collections import deque

input = sys.stdin.readline


def BFS(N: int, M: int, graph: list, x: int, y: int) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    q = deque()
    count = 0

    q.append([y, x])
    graph[y][x] = 0
    count += 1

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
                count += 1
                q.append([nextY, nextX])

    return count


def solve(N: int, M: int, K: int, data: list) -> list:
    # 쓰레기의 위치를 graph에 1로 표시
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for y, x in data:
        graph[y-1][x-1] = 1
    
    # 각 쓰레기에 대해 BFS 탐색. 쓰레기가 없거나 탐색을 마친 점은 0으로 표시
    max_size = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                temp = BFS(N, M, graph, x, y)
                if temp > max_size:
                    max_size = temp

    return max_size


def main():
    N, M, K = map(int, input().split())

    data = []
    for _ in range(K):
        data.append(list(map(int, input().split())))
    
    print(solve(N, M, K, data))


main()