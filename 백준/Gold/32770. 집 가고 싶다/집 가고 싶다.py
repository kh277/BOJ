# 백준 32770

'''
(sasa -> home -> sasa의 최단거리) = (sasa -> home의 최단거리) + (home -> sasa의 최단거리)
'''

import sys
import heapq

input = sys.stdin.readline
INF = 10e17


# 다익스트라 : 우선순위 큐를 이용해 start에서 end까지 최단거리 도출
def dijkstra(V, graph, start, end):
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

    return DP[end]


def solve():
    # 딕셔너리에 시작점과 끝점의 번호 미리 할당
    dic = dict()
    dic['sasa'] = 0
    dic['home'] = 1
    count = 2

    # 다른 정류장들에 대해 번호 부여 및 딕셔너리에 저장
    for i in range(N):
        if E[i][0] not in dic:
            dic[E[i][0]] = count
            count += 1
        if E[i][1] not in dic:
            dic[E[i][1]] = count
            count += 1

    # 정류장 이름으로 이루어진 간선 정보를 숫자로 이루어진 간선으로 변환
    V = count
    graph = [[] for _ in range(V)]
    for i in range(N):
        graph[dic[E[i][0]]].append([dic[E[i][1]], int(E[i][2])])

    # sasa -> home -> sasa 최단거리 도출
    result = dijkstra(V, graph, 0, 1) + dijkstra(V, graph, 1, 0)
    if result >= INF:
        return -1

    return result


# main 함수 ----------
N = int(input())
E = []
for _ in range(N):
    E.append(list(map(str, input().split())))
print(solve())