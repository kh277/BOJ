# 백준 15730

'''
1113번 코드에서 입력과 제한 높이만 바꾸었다.
'''

import sys
from collections import deque

input = sys.stdin.readline
INF = 10002


def BFS(N: int, M: int, graph: list, start: list, height: int) -> list:
    visited = set()
    min_height = INF
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    
    q = deque()
    q.append(start)
    visited.add(start)
    
    while q:
        curY, curX = q.popleft()
        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < M and 0 <= nextY < N:
                if int(graph[nextY][nextX]) == height and (nextY, nextX) not in visited:
                    q.append((nextY, nextX))
                    visited.add((nextY, nextX))
                elif int(graph[nextY][nextX]) != height:
                    min_height = min(min_height, int(graph[nextY][nextX]))
            else:
                min_height = -1
    
    result = 0
    for y, x in visited:
        if min_height == -1:
            graph[y][x] = min_height
        elif min_height < height:
            continue
        else:
            result += min_height - height
            graph[y][x] = min_height

    return [result, graph]


def solve(N: int, M: int, graph: list) -> int:
    # 그래프에서 최대 높이 추출
    max_height = -1
    for y in range(N):
        for x in range(M):
            max_height = max(max_height, graph[y][x])
    
    # 높이를 1씩 증가시켜가며 BFS 탐색
    result = 0
    for height in range(0, max_height+1):
        for y in range(N):
            for x in range(M):
                if graph[y][x] == height:
                    temp, graph = BFS(N, M, graph, (y, x), height)
                    result += temp
    
    return result
    

def main():
    N, M = map(int, input().split())
    
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    print(solve(N, M, graph))


main()