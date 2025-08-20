# 백준 11547

'''
현재 시간이 t일 때, 그래프에서 간선의 비용은 At+B를 따른다.
따라서 최대 비용을 갖도록 하는 t를 삼분 탐색으로 찾으면 된다.
'''

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10
MAX_REPEAT = 100


def TernarySearch(N, graph):
    start = 0
    end = 1440
    repeat = 0

    while repeat < MAX_REPEAT:
        first = (2*start+end)/3
        second = (start+2*end)/3

        if Dijkstra(N, graph, first) < Dijkstra(N, graph, second):
            start = first
        else:
            end = second

        repeat += 1

    return Dijkstra(N, graph, end)


def Dijkstra(V, graph, time):
    start = 1
    distance = [INF for _ in range(V+1)]
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        curDist, curV = heapq.heappop(pq)

        if distance[curV] < curDist:
            continue

        for nextV, nextA, nextB in graph[curV]:
            nextDist = curDist + nextA*time + nextB

            if nextDist < distance[nextV]:
                distance[nextV] = nextDist
                heapq.heappush(pq, (nextDist, nextV))

    return distance[V]


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        i, j, a, b = map(int, input().split())
        graph[i].append([j, a, b])
        graph[j].append([i, a, b])
    
    print(f"{round(TernarySearch(N, graph), 5):.5f}")


main()
