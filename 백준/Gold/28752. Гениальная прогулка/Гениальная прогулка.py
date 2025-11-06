# 백준 28752

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**20


def Dijkstra(V, graph, start, end):
    dist = [INF for _ in range(V+1)]

    pq = []
    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        curT, curV = heapq.heappop(pq)

        if dist[curV] < curT:
            continue

        for nextV, a, p, nextD in graph[curV]:
            remain = curT % p
            # 도착하자마자 기다리지 않고 바로 이동할 수 있는 경우
            if remain + nextD <= a:
                nextT = curT + nextD
                if nextT < dist[nextV]:
                    dist[nextV] = nextT
                    heapq.heappush(pq, (nextT, nextV))

            # 도착한 뒤 기다렸다 이동해야 하는 경우
            else:
                nextT = curT + p - remain + nextD
                if nextT < dist[nextV]:
                    dist[nextV] = nextT
                    heapq.heappush(pq, (nextT, nextV))

    return -1 if dist[end] == INF else dist[end]


def main():
    N, M, S, T = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, a, b, d = map(int, input().split())
        if a != 0 and a >= d:
            graph[v].append((u, a, a+b, d))
        if d <= a:
            graph[u].append((v, a, a+b, d))

    print(Dijkstra(N, graph, S, T))


main()
