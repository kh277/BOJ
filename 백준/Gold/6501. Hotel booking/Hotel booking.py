# 백준 6501

'''
체인점 호텔이 존재하는 정점들끼리 서로 600분 이내에 도달 가능한지를 다익스트라 H번으로 체크.
이 간선들을 바탕으로 그래프를 재구축하여 BFS로 최소시간 도출.
'''

import io
from collections import deque
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def Dijkstra(V, graph, start):
    distance = [INF for _ in range(V+1)]
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        curDist, curV = heapq.heappop(pq)
        if distance[curV] < curDist:
            continue

        for nextV, tempDist in graph[curV]:
            nextDist = curDist + tempDist
            if nextDist < distance[nextV]:
                distance[nextV] = nextDist
                heapq.heappush(pq, (nextDist, nextV))

    return distance


def BFS(N, graph, start):
    visited = [INF for i in range(N)]
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        curV = q.popleft()

        for nextV in graph[curV]:
            if visited[nextV] == INF:
                q.append(nextV)
                visited[nextV] = visited[curV]+1
    
    return 0 if visited[N-1] == INF else visited[N-1]


def solve(N, H, M, graph, chain):
    chain.sort()
    revChain = dict()
    for i in range(H):
        revChain[chain[i]] = i

    # 체인점 호텔을 시작점으로 잡고 다익스트라
    graph2 = [[] for _ in range(H)]
    for i in range(H):
        startV = chain[i]
        dist = Dijkstra(N, graph, startV)

        # 다른 체인점 호텔까지 600분 이내에 도달 가능한 경우 간선 추가
        for j in range(i+1, H):
            endV = chain[j]
            if dist[endV] <= 600:
                graph2[revChain[endV]].append(i)
                graph2[i].append(revChain[endV])

    # BFS로 재구축한 그래프에 대해 최단 거리 도출
    return BFS(H, graph2, 0) - 1


def main():
    while True:
        N = int(input())
        if N == 0:
            break
        H, *chain = map(int, input().split())
        chain.append(1)
        chain.append(N)
        M = int(input())
        graph = [[] for _ in range(N+1)]
        for _ in range(M):
            a, b, t = map(int, input().split())
            graph[a].append((b, t))
            graph[b].append((a, t))

        print(solve(N, H+2, M, graph, chain))


main()
