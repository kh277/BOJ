# 백준 34513

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 10**9


def BFS(N, grid, start, end):
    q = deque()
    visited = [[INF] * N for _ in range(N)]
    q.append(start)
    visited[start[0]][start[1]] = 0

    while q:
        curY, curX = q.popleft()
        curCount = visited[curY][curX]

        # 도착 지점에 도착한 경우
        if curY == end[0] and curX == end[1]:
            return curCount
        
        nextCount = curCount + 1

        for i in range(4):
            nextY = curY
            nextX = curX

            while True:
                nextY += dy[i]
                nextX += dx[i]

                # 이동 불가능한 경우
                if not (0 <= nextY < N and 0 <= nextX < N) or grid[nextY][nextX] == 'B':
                    break

                # 최적의 경로가 이미 존재하는 경우
                if visited[nextY][nextX] < nextCount:
                    break

                if visited[nextY][nextX] > nextCount:
                    q.append((nextY, nextX))
                    visited[nextY][nextX] = nextCount

                # 흰색을 잡은 경우
                if grid[nextY][nextX] != '.':
                    break

    return -1


def solve(N, grid):
    start = [-1, -1]
    end = [-1, -1]
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 'R':
                start[0] = y
                start[1] = x
            elif grid[y][x] == 'K':
                end[0] = y
                end[1] = x
    
    return BFS(N, grid, start, end)


def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(input().decode().strip()))
    
    print(solve(N, grid))


main()
