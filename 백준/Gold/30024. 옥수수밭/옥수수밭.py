# 백준 30024

'''
일단, 옥수수밭의 가장자리에 있는 옥수수들을 전부 우선순위 큐에 넣는다.
우선순위 큐에서 원소 꺼내기 및 방문처리 -> 상하좌우 우선순위 큐에 넣기 -> 반복...

위 과정을 K번 반복하면 된다.
'''

import sys
from collections import deque
import heapq

input = sys.stdin.readline


# 그래프의 가장자리 점만 반환
def edge_BFS(N: int, M: int) -> list:
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    result = []
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    
    while q:
        curY, curX = q.popleft()
        
        isEdge = False
        for i in range(4):
            nextY = curY + pointY[i]
            nextX = curX + pointX[i]
            
            # 인접 점이 가장자리라면
            if nextX in [-1, M] or nextY in [-1, N]:
                isEdge = True
                
            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
                q.append([nextY, nextX])
                visited[nextY][nextX] = True
        
        if isEdge == True:
            result.append([curY, curX])

    return result


# start와 인접한 상하좌우 점 중 탐색 가능한 점만 반환
def BFS(N: int, M: int, start: list, visited: list) -> list:
    result = []
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    
    for i in range(4):
        nextY = start[0] + pointY[i]
        nextX = start[1] + pointX[i]
        
        if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == False:
            result.append([nextY, nextX])
    
    return result
    

def solve(N: int, M: int, graph: list, K: int) -> list:
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    # 가장자리 점 우선순위 큐에 삽입
    pq = []
    edgePoint = edge_BFS(N, M)
    for i in edgePoint:
        heapq.heappush(pq, [-graph[i[0]][i[1]], i[0], i[1]])
        visited[i[0]][i[1]] = True
    
    # 쿼리 K번 진행
    result = []
    for i in range(K):
        curValue, curY, curX = heapq.heappop(pq)
        result.append([curY+1, curX+1])
        
        # 상하좌우 중 탐색 가능한 좌표만 우선순위 큐에 추가
        nextPoint = BFS(N, M, [curY, curX], visited)
        for j in nextPoint:
            heapq.heappush(pq, [-graph[j[0]][j[1]], j[0], j[1]])
            visited[j[0]][j[1]] = True

    return result


def main():
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    K = int(input())
    
    for i in solve(N, M, graph, K):
        print(*i)


main()