# 백준 17412

'''
1번 도시에서 2번 도시로 가는 경로의 개수를 구해야 한다.
따라서 1번 정점 -> 2번 정점으로 가는 최대 유량 문제로 볼 수 있다.
이 때, 모든 간선의 유량은 1로 보면 된다.
'''

import sys
from collections import deque
INF = 10e5

input = sys.stdin.readline


def BFS(capacity, source, sink, parent):
    visited = [False for _ in range(len(capacity))]
    
    q = deque([source])
    visited[source] = True
    
    while q:
        curV = q.popleft()
        
        for nextV in range(len(capacity)):
            # 용량이 남은 간선이 있는 경우
            if visited[nextV] == False and capacity[curV][nextV] > 0:
                q.append(nextV)
                visited[nextV] = True
                parent[nextV] = curV
                
                # sink에 도착할 경우
                if nextV == sink:
                    return True
    
    return False


def NetworkFlow(capacity, source, sink):
    parent = [-1 for _ in range(len(capacity))]
    max_flow = 0
    
    # BFS로 증가 경로 탐색
    while BFS(capacity, source, sink, parent):
        # 증가 경로의 최소 용량 탐색
        path_flow = INF
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        # 경로에 따라 용량 업데이트
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow

    return max_flow


def solve():
    capacity = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for start, end in road:
        capacity[start][end] = 1
    
    return NetworkFlow(capacity, 1, 2)


# main 함수 ----------
N, P = map(int, input().split())

road = []
for _ in range(P):
    road.append(map(int, input().split()))
    

print(solve())