# 백준 16469

'''
세 명이 동시에 만나는 최단 시간이므로,
각각에 대해 BFS 탐색을 하여 걸린 시간을 각각 저장한다.
그 뒤, 모든 좌표에 저장된 세 값을 비교해서 최대인 값을 저장한다.
이 값들 중 최소값을 출력하면 된다.
'''

import sys
from collections import deque

input = sys.stdin.readline
INF = 10e6


def BFS(R: int, C: int, graph: list, start: list, DP: list, people: int) -> list:
    visited = set()
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    
    q = deque()
    q.append([start[0], start[1], 0])
    DP[start[0]][start[1]][people] = 0
    visited.add(start)
    
    while q:
        curY, curX, time = q.popleft()
        
        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]
            
            if 0 <= nextX < C and 0 <= nextY < R and (nextY, nextX) not in visited and graph[nextY][nextX] == '0':
                q.append((nextY, nextX, time+1))
                DP[nextY][nextX][people] = time+1
                visited.add((nextY, nextX))
            
    return DP


def solve(R: int, C: int, graph: list, start_pos: list) -> list:
    DP = [[[INF, INF, INF] for _ in range(C)] for _ in range(R)]
    
    for i in range(3):
        DP = BFS(R, C, graph, (start_pos[i][0]-1, start_pos[i][1]-1), DP, i)
    
    result = [INF, 0]
    for y in range(R):
        for x in range(C):
            if result[0] > max(DP[y][x]):
                result = [max(DP[y][x]), 1]
            elif result[0] == max(DP[y][x]):
                result = [max(DP[y][x]), result[1]+1]
    
    return result if result[0] != INF else [-1]


def main():
    R, C = map(int, input().split())
    
    graph = []
    for _ in range(R):
        graph.append(list(input().rstrip()))
    
    start_pos = []
    for _ in range(3):
        start_pos.append(list(map(int, input().split())))
    
    for i in solve(R, C, graph, start_pos):
        print(i)
    

main()