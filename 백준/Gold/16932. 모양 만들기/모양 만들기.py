# 백준 16932

'''
BFS를 통해 섬의 넓이를 구하고 그 섬의 가장자리에 있는 0에 넓이를 더해준다
모든 섬에 대해 반복한 다음 가장 큰 값을 리턴하면 된다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(start, visited):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    area = 1
    edge = set()

    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    
    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                if graph[nextY][nextX] == 0:
                    edge.add((nextY, nextX))
                else:
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True
                    area += 1
    
    return [area, edge]


def solve():
    visited = [[False for _ in range(M)] for _ in range(N)]
    result = [[False for _ in range(M)] for _ in range(N)]

    # 모든 섬에 대해 반복
    for y in range(N):
        for x in range(M):
            if visited[y][x] == False and graph[y][x] == 1:
                area, edge = BFS([y, x], visited)
                for edgeY, edgeX in edge:
                    result[edgeY][edgeX] += area
    
    # 최대값 리턴
    return max([max(result[i]) for i in range(N)])+1


# main 함수 ----------
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

print(solve())