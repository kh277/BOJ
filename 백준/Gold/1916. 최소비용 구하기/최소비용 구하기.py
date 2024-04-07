# 백준 1916

'''
n개의 정점과 m개의 간선이 존재하는 그래프
맨 마지막 줄에 주어지는 A도시 -> B도시로 가는 최적시간 구하기
-> A도시를 시작점으로 다익스트라 진행
'''

import sys
import heapq as q

input = sys.stdin.readline
INF = 1e8


def dijkstra(V: int, graph: list, start: int, end: int) -> list:
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

    return DP[end]


def main():
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N+1)]

    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])

    A, B = map(int, input().split())

    print(dijkstra(N, graph, A, B))


main()