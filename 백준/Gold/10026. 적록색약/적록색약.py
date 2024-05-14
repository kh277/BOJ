# 백준 10026

'''
적록색약인 사람은 빨간색 = 초록색으로 봄
따라서 초록색을 빨간색으로 바꾸고 구역의 개수를 세자
'''

import sys
from collections import deque
import copy

input = sys.stdin.readline


def BFS(N: int, graph: list, x: int, y: int, target: str) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    q = deque()
    q.append([y, x])
    graph[y][x] = 0

    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            nextY = temp[0] + pointY[i]
            nextX = temp[1] + pointX[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= nextX < N and 0 <= nextY < N and graph[nextY][nextX] == target:
                graph[nextY][nextX] = 0
                q.append([nextY, nextX])
    
    return graph



def solve(N: int, graph: list) -> int:

    # 정상인 사람이 보는 구역의 수
    graph1 = copy.deepcopy(graph)
    normal = 0
    for y in range(N):
        for x in range(N):
            if graph1[y][x] != 0:
                normal += 1
                if graph1[y][x] == 'R':
                    graph1 = BFS(N, graph1, x, y, 'R')
                elif graph1[y][x] == 'G':
                    graph1 = BFS(N, graph1, x, y, 'G')
                elif graph1[y][x] == 'B':
                    graph1 = BFS(N, graph1, x, y, 'B')

    # 색약인 사람이 보는 구역의 수
    graph2 = copy.deepcopy(graph)
    
    # G를 R로 바꿈 
    for y in range(N):
        for x in range(N):
            if graph2[y][x] == 'G':
                graph2[y][x] = 'R'
    
    color_blind = 0
    for y in range(N):
        for x in range(N):
            if graph2[y][x] != 0:
                color_blind += 1
                if graph2[y][x] == 'R':
                    graph2 = BFS(N, graph2, x, y, 'R')
                elif graph2[y][x] == 'B':
                    graph2 = BFS(N, graph2, x, y, 'B')

    return normal, color_blind


def main():
    N = int(input())
    
    graph = []
    for i in range(N):
        graph.append(list(input().rstrip()))
    
    print(*solve(N, graph))

main()