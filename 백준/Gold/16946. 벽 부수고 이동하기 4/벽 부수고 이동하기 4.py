# 백준 16946

'''
벽을 한 칸 부수고 이동할 수 있는 곳의 넓이를 구해야 한다.
반대로 생각해서 섬의 넓이를 가장자리에 있는 벽에 더해준다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(start):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    wall = set()    # 현재 섬을 둘러싸고 있는 벽 저장
    
    q = deque()
    q.append(start)
    graph[start[0]][start[1]] = -1
    area = 1    # 현재 섬의 넓이 저장

    while q:
        curY, curX = q.popleft()
        
        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < M and 0 <= nextY < N:
                # 다음 탐색 지역이 미방문일 경우
                if graph[nextY][nextX] == 0:
                    q.append([nextY, nextX])
                    graph[nextY][nextX] = -1
                    area += 1
                
                # 다음 탐색 지역이 벽일 경우 
                elif graph[nextY][nextX] > 0:
                    wall.add((nextY, nextX))
    
    # 벽에 섬의 넓이 더하기
    for wallY, wallX in wall:
        graph[wallY][wallX] += area


def solve():
    # graph의 자료형 int로 변환
    for y in range(N):
        for x in range(M):
            graph[y][x] = int(graph[y][x])
    
    # 각 섬에 대해 BFS 탐색
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                BFS([y, x])
    
    # graph의 자료형 str로 변환 및 -1인 지점 0으로 변환
    for y in range(N):
        for x in range(M):
            if graph[y][x] == -1:
                graph[y][x] = str(0)
            else:
                graph[y][x] = str(graph[y][x] % 10)

    return graph


# main 함수 ----------
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))

for i in solve():
    print(''.join(i))
