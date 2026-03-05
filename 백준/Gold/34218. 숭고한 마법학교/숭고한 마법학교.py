# 백준 34218

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1000000000
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(Y, X, grid, visited, start, color):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = color
    cand = [start]

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < X and 0 <= nextY < Y and grid[nextY][nextX] == 1 and visited[nextY][nextX] == -1:
                q.append((nextY, nextX))
                cand.append((nextY, nextX))
                visited[nextY][nextX] = color

    return cand


def BFS2(Y, X, grid, visited, candidate):
    q = deque()
    for startY, startX in candidate:
        q.append((startY, startX, 0))
        visited[startY][startX] = 0
    
    while q:
        curY, curX, move = q.popleft()
    
        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < X and 0 <= nextY < Y:
                if visited[nextY][nextX] == -3:
                    return move+1
                elif visited[nextY][nextX] == -1:
                    q.append((nextY, nextX, move+1))
                    visited[nextY][nextX] = 1


def solve(Y, X, grid, start, end):
    visited = [[-1] * X for _ in range(Y)]

    # 시작 정점과 이어진 점을 -2로 표시
    candidate = BFS(Y, X, grid, visited, start, -2)
    if visited[end[0]][end[1]] == -2:
        return 0

    # 끝 정점과 이어진 점을 -3으로 표시
    BFS(Y, X, grid, visited, end, -3)

    # 시작 정점에서 벽을 부수지 않고 접근할 수 있는 정점들을 전부 시작점으로 잡고 BFS
    return BFS2(Y, X, grid, visited, candidate)


def main():
    Y, X = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(map(int, input().split())))
    sY, sX = map(int, input().split())
    eY, eX = map(int, input().split())
    print(solve(Y, X, grid, (sY-1, sX-1), (eY-1, eX-1)))


main()
