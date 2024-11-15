# 백준 32655

'''
다익스트라 알고리즘으로 각 출구까지 걸리는 최단 시간을 구하고,
문이 열리는 주기를 이용해 각 출구마다 탈출 시각을 구한다.
그 뒤 탈출 시각의 최소값을 출력한다. 

주의 반례
5 4 13
1 2 5
2 3 10
3 4 11
4 5 22
2    
4 5
-> 26
'''

import sys
import heapq

input = sys.stdin.readline
INF = 10e16


def dijkstra(V: int, graph: list, start: int) -> list:
    DP = [INF for _ in range(V+1)]
    pq = []

    DP[start] = 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_w, cur_v = heapq.heappop(pq)

        if DP[cur_v] < cur_w:
            continue

        for next_v, add_w in graph[cur_v]:
            next_w = cur_w + add_w
            if next_w < DP[next_v]:
                DP[next_v] = next_w
                heapq.heappush(pq, (next_w, next_v))

    return DP


def solve():
    # 다익스트라로 1번 정점에서 각 정점까지의 최단거리 도출
    time = dijkstra(N, graph, 1)

    # 각 출구에 대해 탈출까지 걸리는 계산
    result = INF
    for i in range(X):
        curExit = escape[i]     # 나가고자 하는 출구
        index = time[curExit]//(K*X)    # curExit에 도착했을 때 회차 계산

        while True:
            # 문이 열렸지만, 아직 도착하지 못한 경우
            if K*X*index + K*(i+1) - 1 < time[curExit]:
                index += 1
                continue

            # 문이 열려 있는 상태에서 도착한 경우 -> 도착한 시간에 탈출
            if K*X*index + K*i <= time[curExit] < K*X*index + K*(i+1):
                result = min(result, time[curExit])

            # 문이 닫힌 상태에서 도착한 경우 -> 다음 문이 열리는 시각에 탈출
            elif time[curExit] <= K*X*index + K*i:
                result = min(result, K*X*index + K*i)

            break

    return result


# main 함수 ----------
N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
X = int(input())
escape = list(map(int, input().split()))

print(solve())
