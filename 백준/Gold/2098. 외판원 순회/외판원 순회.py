# 백준 2098

'''
방문 처리를 비트마스킹으로 하고, 재귀 DP를 통해 정점 순회를 하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8
START = 0


def TSP(N, graph, status, curV, DP):
    # 도시를 다 방문했고, START로의 경로가 존재한다면 curV -> START로 가는 값 반환
    if status == (1 << N) - 1:
        return graph[curV][START] if graph[curV][START] != 0 else INF

    # 이전에 계산한 값일 경우
    if not DP[curV][status] == 0:
        return DP[curV][status]

    DP[curV][status] = INF

    # 방문하지 않은 도시들에 대해 반복
    for nextV in range(N):
        if (status & (1 << nextV)) == 0 and graph[curV][nextV] != 0:
            # (curV에서 nextV 가는 비용) + (nextV에서 나머지 도시를 거쳐 START로 가는 비용) 계산 및 nextV 방문처리
            temp = graph[curV][nextV] + TSP(N, graph, status | (1 << nextV), nextV, DP)

            # 최소값 갱신이 가능하다면 갱신
            if temp < DP[curV][status]:
                DP[curV][status] = temp
    
    return DP[curV][status]


def main():
    N = int(input())
    graph = []

    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    print(TSP(N, graph, 1<<START, 0, [[0 for _ in range(2**N)] for _ in range(N)]))


main()
