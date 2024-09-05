# 백준 2660

'''
다른 모든 회원이 친구 -> 다른 모든 정점까지의 거리가 1
다른 모든 회원이 친구이거나 친구의 친구 -> 다른 모든 정점까지의 거리가 1~2

따라서 한 정점에서 다른 모든 정점까지의 거리를 구하고 가장 먼 거리가 점수가 된다.
이것을 모든 사람에 대해 반복해야 하므로 플로이드-워셜 알고리즘을 사용하자.
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
    return [graph[i][1:] for i in range(1, N+1)]


def solve(N: int, graph: list) -> list:
    # 인접 리스트 -> 인접 행렬
    temp_list = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for start, end in graph:
        temp_list[start][end] = 1
        temp_list[end][start] = 1

    # 플로이드-워셜 알고리즘으로 각 정점 간 최단거리 도출
    DP = Floyd_Warshall(N, temp_list)

    # 회장 후보 추출
    score = [INF, []]
    for start in range(N):
        temp = max(DP[start])
        if temp < score[0]:
            score = [temp, [start+1]]
        elif temp == score[0]:
            score[1].append(start+1)
            
    return [[score[0], len(score[1])], score[1]]


def main():
    N = int(input())
    
    graph = []
    while True:
        temp = list(map(int, input().split()))
        if temp == [-1, -1]:
            break
        else:
            graph.append(temp)
    
    for i in solve(N, graph):
        print(*i)


main()