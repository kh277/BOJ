# 백준 1113

'''
(0, 0)부터 (N-1, M-1)까지의 좌표를 땅의 높이 순서대로 BFS 탐색한다.
시작 지점의 높이가 1이라고 가정해보자.
시작 지점과 이어져 있으면서 높이가 같은 점을 탐색하여 저장해둔다.
동시에 그 점들 주변 땅의 높이 중 가장 낮은 값을 저장한다.
이어진 점들에 대해 그 차이값만큼 물을 채운다.
만약 주변 땅 중 경계값이 포함된다면, 그 땅은 물을 채울 수 없게 된다.

높이가 1인 모든 땅에 대해 반복하고, 2인 땅, ...
9인 땅까지 반복한 뒤 물을 채울 수 있는 총 결과값을 더해서 출력하면 된다.
'''

import sys
from collections import deque

input = sys.stdin.readline
INF = 10


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
            
            # 수영장 내부인 경우
            if 0 <= nextX < M and 0 <= nextY < N:
                # 높이가 같고 방문하지 않은 경우 -> visited에 추가
                if int(graph[nextY][nextX]) == height and (nextY, nextX) not in visited:
                    q.append((nextY, nextX))
                    visited.add((nextY, nextX))
                # 높이가 다른 경우
                elif int(graph[nextY][nextX]) != height:
                    min_height = min(min_height, int(graph[nextY][nextX]))
            # 수영장 외부인 경우
            else:
                min_height = -1
    
    result = 0
    for y, x in visited:
        # 현재 땅이 수영장 외부와 접한 경우 -> 물 추가 X
        if min_height == -1:
            graph[y][x] = str(min_height)
        # 현재 땅이 주변보다 높은 경우 -> 물 추가 X
        elif min_height < height:
            continue
        # 주변이 현재 땅보다 높은 경우 -> 차이만큼 저장
        else:
            result += min_height - height
            graph[y][x] = str(min_height)

    return [result, graph]


def solve(N: int, M: int, graph: list) -> int:
    result = 0
    for height in range(1, 10):
        # graph에서 높이가 height인 좌표에 대해 반복
        for y in range(N):
            for x in range(M):
                if graph[y][x] == str(height):
                    temp, graph = BFS(N, M, graph, (y, x), height)
                    result += temp
    
    return result
    

def main():
    N, M = map(int, input().split())
    
    graph = []
    for _ in range(N):
        graph.append(list(input().rstrip()))
    
    print(solve(N, M, graph))


main()