# 백준 1504

'''
N개의 정점과 E개의 간선으로 이루어진 그래프
1번 정점에서 N번 정점까지 최단 거리로 이동하는데, A정점과 B정점을 반드시 지나야 함.
-> min(1->A->B->N을 지나는 최단거리, 1->B->A->N을 지나는 최단거리)
-> 1에서 다익스트라 실행, N에서 다익스트라 실행, A에서 다익스트라 실행 후
    1에서 A로 가는 길이 + N에서 B로 가는 길이 + A에서 B로 가는 길이
    1에서 B로 가는 길이 + N에서 A로 가는 길이 + A에서 B로 가는 길이
    중 최소값이 정답이 된다.
'''

import sys
import heapq as q

input = sys.stdin.readline
INF = 1e8


def dijkstra(V: int, graph: list, start: int) -> list:
    DP = [INF for _ in range(V+1)]
    PriorityQueue = []

    # 우선순위 큐에 시작 정점을 (우선순위, 값) 형태로 집어넣음
    DP[start] = 0
    q.heappush(PriorityQueue, (0, start))
    
    # 우선순위 큐가 빌 때까지 반복
    while PriorityQueue:
        cur_w, cur_v = q.heappop(PriorityQueue)

        # 갱신할 필요가 없는 경우 (구한 비용 > 저장된 비용)
        if DP[cur_v] < cur_w:
            continue
        
        # 현재 탐색한 정점과 이어전 간선들에 대해서
        for next_v, add_w in graph[cur_v]:
            next_w = cur_w + add_w

            # 갱신이 가능한 경우 (구한 비용 < 저장된 비용)
            if next_w < DP[next_v]:
                DP[next_v] = next_w
                q.heappush(PriorityQueue, (next_w, next_v))

    return DP


def solve(N: int, E: int, graph: list, A: int, B: int) -> int:
    start_DP = dijkstra(N, graph, 1)
    end_DP = dijkstra(N, graph, N)
    A_DP = dijkstra(N, graph, A)

    temp = [start_DP[A], A_DP[B], end_DP[B], start_DP[B], end_DP[A]]

    # 예외 케이스 - 경로가 존재하지 않는 경우
    for i in temp:
        if i == INF:
            return -1

    return min(start_DP[A]+A_DP[B]+end_DP[B], start_DP[B]+A_DP[B]+end_DP[A])


def main():
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for i in range(E):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    A, B = map(int, input().split())

    print(solve(N, E, graph, A, B))


main()