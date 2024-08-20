# 백준 1240

'''
N개의 노드로 이루어진 트리가 존재할 때,
N <= 1000이므로 다익스트라 알고리즘을 이용하자.
'''

import sys
import heapq

input = sys.stdin.readline
INF = 1e8


def dijkstra(V: int,  graph: list, start: int) -> list:
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


def solve(N: int, graph: list, query: list) -> list:
    # 다익스트라를 통해 거리 도출 및 쿼리 결과 저장
    result = []
    for start, end in query:
        temp = dijkstra(N, graph, start)
        result.append(temp[end])
    
    return result


def main():
    N, M = map(int, input().split())

    # 입력 처리 및 인접 행렬 생성
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    query = []
    for _ in range(M):
        query.append(list(map(int, input().split())))
    
    # 결과 출력
    for i in solve(N, graph, query):
        print(i)


main()