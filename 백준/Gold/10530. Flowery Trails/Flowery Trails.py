# 백준 10530

'''
0, V-1을 시작점으로 잡고 각각 다익스트라를 돌려서 다른 모든 정점까지의 거리를 구하고,
모든 간선에 대해 최단 거리에 포함되는 간선인지 아래 식을 통해 체크한다.
[0 -> 현재 간선 시작] + [현재 간선 시작 -> 현재 간선 끝] + [현재 간선 끝 -> V-1] = 최단 거리
'''

import io
from array import array
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def Dijkstra(V, graph, start):
    dist = array('I', [INF]) * V
    pq = []
    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        curDist, curV = heapq.heappop(pq)

        if dist[curV] < curDist:
            continue

        for nextV, tempDist in graph[curV]:
            nextDist = curDist + tempDist

            if nextDist < dist[nextV]:
                dist[nextV] = nextDist
                heapq.heappush(pq, (nextDist, nextV))

    return dist


def solve(V, E, edge):
    # 간선 정보로 그래프 구성
    graph = [[] for _ in range(V)]
    for i in range(E):
        s, e, d = edge[i]
        graph[s].append([e, d])
        graph[e].append([s, d])

    # 0, V-1에서 각각 다익스트라 진행
    distS = Dijkstra(V, graph, 0)
    distE = Dijkstra(V, graph, V-1)

    # 간선이 최단 거리에 포함되는 간선인지 체크
    accDist = 0
    for s, e, d in edge:
        if distS[s] + d + distE[e] == distS[V-1] or distS[e] + d + distE[s] == distS[V-1]:
            accDist += d

    return accDist * 2


def main():
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        edge.append(list(map(int, input().split())))

    print(solve(V, E, edge))


main()
