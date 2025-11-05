# 백준 14461

import io
import heapq


input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**20
dx = [-3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3]
dy = [0, -1, 1, -2, 0, 2, -3, -1, 1, 3, -2, 0, 2, -1, 1, 0]


def Dijkstra(V, graph, start):
    pq = []
    distance = [INF for _ in range(V)]
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        curDist, curV = heapq.heappop(pq)

        if distance[curV] < curDist:
            continue

        for tempDist, nextV in graph[curV]:
            nextDist = curDist + tempDist
            if nextDist < distance[nextV]:
                distance[nextV] = nextDist
                heapq.heappush(pq, (nextDist, nextV))

    return distance


def solve(N, T, grid):
    # 이동할 수 있는 1칸, 3칸을 전부 간선으로 저장하여 그래프 형성
    graph = [[] for _ in range(N*N)]
    for curY in range(N):
        for curX in range(N):
            curV = N*curY + curX
            for i in range(16):
                nextX = curX + dx[i]
                nextY = curY + dy[i]
                nextV = N*nextY + nextX
                if 0 <= nextX < N and 0 <= nextY < N:
                    graph[curV].append((T*3+grid[nextY][nextX], nextV))

    # 다익스트라로 최단거리 도출
    dist = Dijkstra(N*N, graph, 0)

    # 도착점에서 1~2칸 떨어진 곳에서 이동하는 경우
    result = dist[N*N-1]
    for i in [N*N-3, N*N-N-2, N*N-2*N-1]:
        result = min(result, dist[i] + T*2)
    for i in [N*N-2, N*N-N-1]:
        result = min(result, dist[i] + T)

    return result


def main():
    N, T = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    print(solve(N, T, grid))


main()
