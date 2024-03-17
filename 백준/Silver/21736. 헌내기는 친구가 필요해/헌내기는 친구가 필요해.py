# 백준 21736

'''
N행 M열 크기의 격자에서 I를 시작점으로 할 때,
도달할 수 있는 P의 개수를 구하는 문제이다.
BFS를 사용하여 격자를 탐색하면 된다.
'''

import sys
from collections import deque

input = sys.stdin.readline

pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


def BFS(N: int, M: int, x: int, y: int, graph: list):
    q = deque()
    q.append([x, y])

    count = 0
    while q:
        temp = q.popleft()

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            X = temp[0] + pointX[i]
            Y = temp[1] + pointY[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= X < N and 0 <= Y < M and graph[X][Y] != '.':
                if graph[X][Y] == 'X':
                    continue

                if graph[X][Y] == 'P':
                    count += 1

                graph[X][Y] = '.'
                q.append([X, Y])
    
    # 만난 사람의 수에 따라 결과 리턴
    if count == 0:
        return "TT"
    else:
        return count


def solve(N: int, M: int, graph: list) -> str:
    # 시작점 파악
    for i in range(N):
        for j in range(M):
            # 시작점을 확인한 경우 그 점에서부터 BFS 실행
            if graph[i][j] == 'I':
                return BFS(N, M, i, j, graph)


def main():
    N, M = map(int, input().split())
    graph = [0 for _ in range(N)]
    for i in range(N):
        graph[i] = list(input().rstrip())

    print(solve(N, M, graph))


main()
