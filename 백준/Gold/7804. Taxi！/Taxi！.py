# 백준 7804

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def solve(V, graph, startV, endV, r):
    DP = [INF for _ in range(V)]
    DP[startV] = 0
    pq = [(0, 0, startV)]

    while pq:
        curT, curC, curV = heapq.heappop(pq)

        if curV == endV:
            return curT

        for nextV, time, cost in graph[curV]:
            nextT = curT + time
            nextC = curC + cost

            if nextC <= r and DP[nextV] > nextT:
                DP[nextV] = nextT
                heapq.heappush(pq, (nextT, nextC, nextV))


def main():
    while True:
        try:
            V, E = map(int, input().split())
            graph = [[] for _ in range(V)]
            for _ in range(E):
                u, v, t, c = map(int, input().split())
                graph[u].append((v, t, c))
                graph[v].append((u, t, c))
            start, end, r = map(int, input().split())
            print(solve(V, graph, start, end, r))
        except:
            break


main()
