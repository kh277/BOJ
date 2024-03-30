# 백준 1238

'''
1, 2, 3, ..., N개의 정점에서 X로 모이고 돌아가는데 가장 오래 걸리는 시간?
-> 시작점을 기준으로 다익스트라 진행
-> 간선의 시작점과 끝점을 뒤집은 뒤 다익스트라 진행.
그 뒤 두 값을 합친 최소값 반환.
'''

import sys
import heapq as q

input = sys.stdin.readline
INF = 10e8


def dijkstra(V: int, E: int, graph: list, start: int) -> list:
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

    return DP[1:]

def solve(V: int, E: int, graph: list, graph_rev: list, start: int) -> int:
    result_1 = dijkstra(V, E, graph, start)
    result_2 = dijkstra(V, E, graph_rev, start)

    maximum = 0
    for i in range(V):
        if maximum < result_1[i] + result_2[i]:
            maximum = result_1[i] + result_2[i]
    
    return maximum


def main():
    # 정점, 간선, 목적지
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(M+1)]
    graph_rev = [[] for _ in range(M+1)]
    
    # rev에는 간선의 출발지와 도착지를 뒤집어서 저장
    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph_rev[b].append([a, c])

    print(solve(N, M, graph, graph_rev, X))

main()
