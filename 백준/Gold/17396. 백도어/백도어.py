# 백준 17396

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1e12


def dijkstra(V, graph, start, DP):
    DP = [INF for _ in range(V+1)]
    PriorityQueue = []

    DP[start] = 0
    heapq.heappush(PriorityQueue, (0, start))
    
    while PriorityQueue:
        cur_w, cur_v = heapq.heappop(PriorityQueue)

        if DP[cur_v] < cur_w:
            continue

        for next_v, add_w in graph[cur_v]:
            next_w = cur_w + add_w

            if next_w < DP[next_v]:
                DP[next_v] = next_w
                heapq.heappush(PriorityQueue, (next_w, next_v))

    return DP


def solve():
    # 다익스트라를 여러 번 돌려 갱신되지 않은 경로 처리
    DP = [INF for _ in range(N+1)]
    DP = dijkstra(N, graph, 0, DP)
    DP = dijkstra(N, graph, 0, DP)

    return -1 if DP[N-1] == INF else DP[N-1]


# main 함수 ----------
N, M = map(int, input().split())
cantMove = list(map(int, input().split()))
cantMove[N-1] = 0

graph = [[] for _ in range(N)]
for i in range(M):
    start, end, distance = map(int, input().split())
    if cantMove[start] == 0 and cantMove[end] == 0:
        graph[start].append([end, distance])
        graph[end].append([start, distance])

print(solve())
