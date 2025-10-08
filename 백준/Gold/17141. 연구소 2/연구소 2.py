# 백준 17141

import io
from itertools import combinations
from collections import deque
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 60
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(N, startPos, grid):
    # 시작점 큐에 저장
    visited = [array('q', [-1]) * N for _ in range(N)]
    q = deque()
    for i in startPos:
        q.append((i[0], i[1], 0))
        grid[i[0]][i[1]] = 0
        visited[i[0]][i[1]] = 0

    # BFS 탐색
    while q:
        curY, curX, count = q.popleft()
        
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            
            if 0 <= nextX < N and 0 <= nextY < N and visited[nextY][nextX] == -1 and grid[nextY][nextX] != 1:
                q.append((nextY, nextX, count+1))
                visited[nextY][nextX] = count+1

    # 바이러스가 퍼진 시간 체크
    result = 0
    for y in range(N):
        for x in range(N):
            if grid[y][x] != 1 and visited[y][x] == -1:
                return -1
            result = max(result, visited[y][x])

    return result


def solve(N, M, grid):
    # 시작점 탐색
    canSet = []
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 2:
                canSet.append((y, x))

    # 시작점 중 M개를 골라 BFS 탐색
    result = INF
    for startPos in combinations(canSet, M):
        r = BFS(N, startPos, grid)
        if r == -1:
            continue
        result = min(result, r)

    if result == INF:
        return -1
    return result


def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    print(solve(N, M, grid))


main()
