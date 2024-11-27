# D번

import sys
import heapq

input = sys.stdin.readline
INF = 10e18


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
    dic = dict()
    dic['sasa'] = 0
    dic['home'] = 1
    count = 3

    for i in range(N):
        if E[i][0] not in dic:
            dic[E[i][0]] = count
            count += 1

        if E[i][1] == 'sasa':
            dic['end'] = 2
        elif E[i][1] not in dic:
            dic[E[i][1]] = count
            count += 1

    V = len(dic)
    graph = [[] for _ in range(V)]
    for i in range(N):
        if E[i][1] == 'sasa':
            graph[dic[E[i][0]]].append([2, int(E[i][2])])
        else:
            graph[dic[E[i][0]]].append([dic[E[i][1]], int(E[i][2])])

    result = dijkstra(V, graph, 0, 1) + dijkstra(V, graph, 1, 2)
    if result >= INF:
        return -1

    return result


# main 함수 ----------
N = int(input())
E = []
for _ in range(N):
    E.append(list(map(str, input().split())))
print(solve())