# 백준 26549

'''
그래프에서 섬의 개수와 넓이를 구하는 문제이다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def BFS(start):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    curArea = 0

    q = deque()
    q.append(start)
    graph[start[0]][start[1]] = '#'
    curArea += 1

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            if 0 <= nextX < M and 0 <= nextY < N and graph[nextY][nextX] == '.':
                q.append([nextY, nextX])
                graph[nextY][nextX] = '#'
                curArea += 1
    
    return curArea


def solve():
    count = 0
    area = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == '.':
                area += BFS([y, x])
                count += 1

    section = 'sections'
    space = 'spaces'
    if count == 1:
        section = 'section'
    if area == 1:
        space = 'space'
    return "{a} {b}, {c} {d}".format(a=count, b=section, c=area, d=space)


# main 함수 ----------
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(input().rstrip()))

    print(solve())