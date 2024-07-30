# 백준 4179

'''
불이 번질 때까지 걸리는 시간과 사람이 탈출할 때까지 걸리는 시간을 따로 계산한다
출구 즉, 가장자리에 사람 > 불인 값이 존재한다면 탈출할 수 있다
'''

import sys
from collections import deque
import copy

input = sys.stdin.readline


def BFS(N: int, M: int, graph: list, start: list, target: list) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    q = deque()
    for i in start:
        q.append(i)
        graph[i[0]][i[1]] = 0


    # 큐가 빌 때까지 반복
    while q:
        temp = q.popleft()

        # 상하좌우 탐색 가능한지 확인
        for i in range(4):
            nextY = temp[0] + pointY[i]
            nextX = temp[1] + pointX[i]

            # 탐색 가능한 경우 큐에 넣고 graph에 표시
            if 0 <= nextX < M and 0 <= nextY < N and graph[nextY][nextX] in target:
                graph[nextY][nextX] = graph[temp[0]][temp[1]] + 1
                q.append([nextY, nextX])
    
    return graph



def solve(R: int, C: int, graph: list) -> int:

    start = []
    fire = []
    
    # 사람과 불의 위치 확인
    for y in range(R):
        for x in range(C):
            if graph[y][x] == 'J':
                start.append([y, x])
            elif graph[y][x] == 'F':
                fire.append([y, x])

    # 사람이 탈출할 때 걸리는 시간
    human_result = BFS(R, C, copy.deepcopy(graph), start, ['.', 'F'])

    # 불이 번질 때 걸리는 시간
    fire_result = BFS(R, C, copy.deepcopy(graph), fire, ['.', 'J'])
    
    # 사람 또는 불이 모든 칸에 도달하지 못하는 경우
    for y in range(R):
        for x in range(C):
            if human_result[y][x] in ['.', '#', 'F']:
                human_result[y][x] = 10e5
            if fire_result[y][x] in ['.', '#', 'J']:
                fire_result[y][x] = 10e5 

        
    # 탈출까지 걸리는 시간 계산
    escape_count = 10e5
    for y in range(R):
        if graph[y][0] != '#' and fire_result[y][0] > human_result[y][0]:
                if escape_count > human_result[y][0]:
                    escape_count = human_result[y][0]
        if graph[y][C-1] != '#' and fire_result[y][C-1] > human_result[y][C-1]:
                if escape_count > human_result[y][C-1]:
                    escape_count = human_result[y][C-1]
    
    for x in range(C):
        if graph[0][x] != '#' and fire_result[0][x] > human_result[0][x]:
                if escape_count > human_result[0][x]:
                    escape_count = human_result[0][x]
        if graph[R-1][x] != '#' and fire_result[R-1][x] > human_result[R-1][x]:
            if escape_count > human_result[R-1][x]:
                escape_count = human_result[R-1][x]
                
    # 미로를 탈출해야 하므로 가장자리까지 걸리는 최소 시간에 +1을 해줌
    return "IMPOSSIBLE" if escape_count == 10e5 else escape_count+1


def main():
    R, C = map(int, input().split())
    
    graph = []
    for i in range(R):
        graph.append(list(input().rstrip()))
    
    print(solve(R, C, graph))

main()