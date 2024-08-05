# 백준 23817

'''
1~20개의 식당 중 5개의 식당을 방문하는 최소 시간을 구해야 한다.

1. 그래프에서 시작 위치와 식당의 위치를 파악한다.
2. 시작 위치를 포함하여 각 식당끼리 거리를 간선으로 작성한다.
3. 시작 위치에서 식당 5개를 지나는 데 걸리는 최소시간을 구한다.
'''

import sys


input = sys.stdin.readline
INF = 10e7

def Floyd_Warshall(N: int, graph: list) -> list:
    # 자기에게로의 간선은 0으로 초기화
    for i in range(1, N+1):
        graph[i][i] = 0

    # a->b로의 비용에서 k를 거쳐 가는 것이 더 효율적인지 판단
    for k in range(1, N+1):             # 거치는 점
        for a in range(1, N+1):         # 시작점
            for b in range(1, N+1):     # 끝점
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 간선 정보가 INF인 값은 0로 변환
    for a in range(N+1):
        for b in range(N+1):
            if graph[a][b] == INF:
                graph[a][b] = 0
    
    # 0번 정점은 제외하고 출력
    return [graph[i][1:] for i in range(1, N+1)]


def main():
    N = int(input())
    M = int(input())

    graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a][b] = min(c, graph[a][b])
    
    for i in Floyd_Warshall(N, graph):
        print(*i)


main()
