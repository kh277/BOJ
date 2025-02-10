# 백준 2350

'''
경로를 많이 지난다고 해서 비용이 추가되지는 않으므로
그래프에 대해 최대 폭만 가지도록 MST를 도출하고 정점 간 폭의 최소값을 구하자.
'''

from collections import deque
import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 201


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    parent[max(a, b)] = min(a, b)


# kruskal 알고리즘을 통해 MST를 구성하는 그래프 반환
def kruskal():
    parent = [i for i in range(N+1)]
    graph = [[] for _ in range(N+1)]

    # [start, end, gap] 순서에서 gap 내림차순 기준으로 정렬
    road.sort(key= lambda x: -x[2])

    # 간선 비교
    for i in road:
        a, b, gap = i
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            graph[a].append([b, gap])
            graph[b].append([a, gap])
    
    return graph


# BFS로 start에서 다른 모든 정점까지 배가 지나갈 수 있는 최대 폭 구하기
def BFS(start, graph, maxGap):
    visited = [False for _ in range(N+1)]

    q = deque()
    q.append([start, INF])
    visited[start] = True

    while q:
        curV, curGap = q.popleft()

        for nextV, nextGap in graph[curV]:
            if visited[nextV] == False:
                visited[nextV] = True
                gap = min(curGap, nextGap)
                maxGap[start][nextV] = gap
                maxGap[nextV][start] = gap
                q.append([nextV, gap])


def preprocess():
    # kruskal로 MST를 구성하는 그래프 구하기
    graph = kruskal()

    # BFS로 모든 정점 간 통과할 수 있는 배의 최대 폭 구하기
    maxGap = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        BFS(i, graph, maxGap)

    return maxGap


# main 함수 ----------
N, M, K = map(int, input().split())
road = []
for _ in range(M):
    road.append(list(map(int, input().split())))
maxGap = preprocess()

for _ in range(K):
    s, e = map(int, input().split())
    print(maxGap[s][e])