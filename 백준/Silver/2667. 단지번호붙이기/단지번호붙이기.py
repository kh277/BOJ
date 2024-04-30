# 백준 2667

'''
이 문제는 주어진 필드에서 섬의 개수를 구하는 것과 같다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(N: int, graph: list, x: int, y: int) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    count = 0
    q = deque()
    q.append([y, x])
    graph[y][x] = '0'

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()
        count += 1

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            nextY = temp[0] + pointY[i]
            nextX = temp[1] + pointX[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= nextX < N and 0 <= nextY < N and graph[nextY][nextX] == '1':
                graph[nextY][nextX] = '0'
                q.append([nextY, nextX])

    return graph, count


def solve(N: int, graph: list) -> int:
    result = []

    # 전체 그래프에 대해 탐색
    for i in range(N):
        for j in range(N):
            # 1이 존재할 경우 BFS 탐색
            if graph[j][i] == '1':
                graph, count = BFS(N, graph, i, j)
                result.append(count)

    return [len(result)] + sorted(result)


def main():
    N = int(input())
    graph = []

    for _ in range(N):
        graph.append(list(input().rstrip()))

    for i in solve(N, graph):
        print(i)


main()
