# 백준 1753

'''
한 정점에서 다른 모든 정점으로의 최단 경로를 구하려면 다익스트라 알고리즘을 사용하면 된다.
다만, 정점의 개수가 10000개 이상이므로 O(ElogN)인 개선된 다익스트라 알고리즘을 사용해야 한다.
'''

import sys
import heapq as q

input = sys.stdin.readline
INF = 1e8


def dijkstra(V: int, E: int, graph: list, start: int) -> list:
    DP = [INF for _ in range(V+1)]
    PriorityQueue = []

    # 우선순위 큐에 시작 정점을 (우선순위, 값) 형태로 집어넣음
    DP[start] = 0
    q.heappush(PriorityQueue, (0, start))
    
    # 우선순위 큐가 빌 때까지 반복
    while PriorityQueue:
        cur_w, cur_v = q.heappop(PriorityQueue)

        # 갱신할 필요가 없는 경우 (구한 거리 > 저장된 거리)
        if DP[cur_v] < cur_w:
            continue
        
        # 현재 탐색한 정점과 이어전 간선들에 대해서
        for next_v, add_w in graph[cur_v]:
            next_w = cur_w + add_w

            # 갱신이 가능한 경우 (구한 거리 < 저장된 거리)
            if next_w < DP[next_v]:
                DP[next_v] = next_w
                q.heappush(PriorityQueue, (next_w, next_v))

    return DP[1:]


def main():
    V, E = map(int, input().split())
    K = int(input())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    for i in dijkstra(V, E, graph, K):
        if i == INF:
            print("INF")
        else:
            print(i)


main()
