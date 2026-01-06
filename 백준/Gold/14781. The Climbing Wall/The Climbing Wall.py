# 백준 14781

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, graph, start, end):
    visited = [0 for _ in range(N)]
    q = deque()
    for i in start:
        q.append((i, 1))
        visited[i] = 1
    
    while q:
        curV, moveC = q.popleft()

        if curV in end:
            return moveC

        for nextV in graph[curV]:
            if visited[nextV] == 0:
                q.append((nextV, moveC+1))
                visited[nextV] = 1


def solve(Y, N, points):
    start = []
    end = set()

    # 시작점, 끝점 처리
    top = Y-1000
    points.sort(key= lambda x: (x[1], x[0]))
    for i in range(N):
        if points[i][1] <= 1000:
            start.append(i)
        if points[i][1] >= top:
            end.add(i)

    # 그래프 생성
    graph = [[] for _ in range(N)]
    for i in range(N-1):
        curX, curY = points[i]
        # 오른쪽, 위쪽으로 이동 처리
        for j in range(i+1, N):
            nextX, nextY = points[j]
            if nextY - curY > 1000:
                break
            if (nextY-curY)**2 + (nextX-curX)**2 <= 1000000:
                graph[i].append(j)
                graph[j].append(i)

    # BFS로 최단거리 도출
    return BFS(N, graph, start, end)


def main():
    Y, N = map(int, input().split())
    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))

    print(solve(Y, N, points))


main()
