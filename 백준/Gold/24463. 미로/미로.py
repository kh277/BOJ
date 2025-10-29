# 백준 24463

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(N, M, grid, escape):
    start = escape[0]
    end = escape[1]
    stack = []
    visited = [[None] * M for _ in range(N)]
    stack.append((start[0], start[1]))
    visited[start[0]][start[1]] = (-1, -1)

    while stack:
        curY, curX = stack.pop()

        if curY == end[0] and curX == end[1]:
            break
        
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < M and 0 <= nextY < N and grid[nextY][nextX] == '.' and visited[nextY][nextX] == None:
                stack.append((nextY, nextX))
                visited[nextY][nextX] = (curY, curX)

    # 최단거리 역추적
    traceX = end[1]
    traceY = end[0]
    trace = [end]
    while True:
        if traceX == start[1] and traceY == start[0]:
            return trace

        traceY, traceX = visited[traceY][traceX]
        trace.append((traceY, traceX))


def solve(N, M, grid):
    # 시작점 및 끝점 탐색
    escape = []
    for y in range(N):
        if grid[y][0] == '.':
            escape.append((y, 0))
        if grid[y][M-1] == '.':
            escape.append((y, M-1))
    for x in range(M):
        if grid[0][x] == '.':
            escape.append((0, x))
        if grid[N-1][x] == '.':
            escape.append((N-1, x))

    # DFS 탐색
    traceBack = set(DFS(N, M, grid, escape))

    # 최단 경로에 포함되지 않은 지점을 '@'로 변경
    for y in range(N):
        for x in range(M):
            if grid[y][x] == '.' and (y, x) not in traceBack:
                grid[y][x] = '@'

    return [''.join(i) for i in grid]


def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(input().decode().strip()))

    for i in solve(N, M, grid):
        print(i)


main()
