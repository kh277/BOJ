# 백준 11657

'''
시작 정점에서 다른 모든 정점까지 최단 거리를 구해야 한다.
또한 가중치에 음수가 섞여 있으므로 벨만-포드 알고리즘을 사용하면 된다.
'''

import sys
import math

input = sys.stdin.readline
INF = 10e8


def bellman_ford(V: int, E: int, graph: list, start: int) -> list:
    DP = [INF for _ in range(V+1)]
    DP[start] = 0
    
    # 모든 정점에 대해 반복
    for i in range(V):
        # 모든 간선에 대해 반복
        for j in range(E):
            # [출발 정점, 도착 정점, 거리] 순으로 담겨있는 리스트 
            cur = graph[j]
            
            # 현재 정점을 거쳐서 다음 정점으로 이동하는 거리가 더 짧은 경우 
            if DP[cur[0]] != INF and DP[cur[1]] > DP[cur[0]] + cur[2]:
                DP[cur[1]] = DP[cur[0]] + cur[2]

                # 마지막 정점에 대해서도 갱신 -> 음수 순환이 존재하는 그래프
                if i == V-1:
                    return [-1]
    
    # 거리가 INF인 점 -1로 변환
    for i in range(V+1):
        if DP[i] == INF:
            DP[i] = -1

    return DP[2:]


def main():
    N, M = map(int, input().split())
    graph = []

    for i in range(M):
        A, B, C = map(int, input().split())
        graph.append((A, B, C))

    for i in bellman_ford(N, M, graph, 1):
        print(i)

main()