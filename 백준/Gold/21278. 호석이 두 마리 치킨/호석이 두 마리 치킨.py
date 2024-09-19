# 백준 21278

'''
플로이드-워셜 알고리즘으로 모든 정점간 거리를 구한다.
그 뒤, 시작점을 두 개 잡고 각 정점에 대한 최단거리를 구한다.
이 합이 최소가 되는 두 점이 정답이 된다.
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

    # 간선 정보가 INF인 값은 -1로 변환
    for a in range(N+1):
        for b in range(N+1):
            if graph[a][b] == INF:
                graph[a][b] = -1
    
    # 0번 정점은 제외하고 출력
    # return graph
    return [graph[i][1:] for i in range(1, N+1)]


def solve(N: int, M: int, V: list) -> list:
    graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
    
    # 인접 그래프 -> 인접 행렬
    for i in V:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1

    # 플로이드-워셜 진행
    graph = Floyd_Warshall(N, graph)
    
    # 정점 2개 선택 후 최단거리 도출
    result = [None, None, INF]
    for i in range(N-1):
        for j in range(i+1, N):
            cur_sum = 0
            for k in range(N):
                cur_sum += min(graph[i][k], graph[j][k])
            if cur_sum < result[2]:
                result = [i+1, j+1, cur_sum]
    
    return [result[0], result[1], result[2]*2]


def main():
    N, M = map(int, input().split())
    
    V = []
    for _ in range(M):
        V.append(list(map(int, input().split())))
    
    print(*solve(N, M, V))


main()