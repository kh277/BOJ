# 백준 2468

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, graph, start, height, visited):
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < N and 0 <= nextY < N and visited[nextY][nextX] == False:
                if graph[nextY][nextX] > height:
                    q.append([nextY, nextX])
                    visited[nextY][nextX] = True

    return visited


def solve(N, graph):
    result = 1
    maxData = max([max(x) for x in graph])

    # 모든 높이에 대해 전수조사
    for height in range(maxData+1):
        curResult = 0
        visited = [[False for _ in range(N)] for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if visited[y][x] == False and graph[y][x] > height:
                    visited = BFS(N, graph, [y, x], height, visited)
                    curResult += 1

        result = max(result, curResult)
    
    return result


def main():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    print(solve(N, graph))


main()