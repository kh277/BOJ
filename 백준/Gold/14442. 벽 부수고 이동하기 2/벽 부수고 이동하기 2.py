# 백준 14442

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 1000000000


def BFS(Y, X, K, grid):
    visited = [[[INF] * (K+1) for _ in range(X)] for _ in range(Y)]
    q = deque()
    q.append([0, 0, K])
    visited[0][0][K] = 1

    while q:
        curY, curX, leftBreak = q.popleft()

        if curX == X-1 and curY == Y-1:
            return visited[curY][curX][leftBreak]

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            nextM = visited[curY][curX][leftBreak]+1
            if 0 <= nextX < X and 0 <= nextY < Y:
                # 다음 칸이 벽이고 돌파 가능하다면
                if grid[nextY][nextX] == 1 and leftBreak > 0 and visited[nextY][nextX][leftBreak-1] > nextM:
                    q.append((nextY, nextX, leftBreak-1))
                    visited[nextY][nextX][leftBreak-1] = nextM

                # 다음 칸이 일반 칸이라면
                elif grid[nextY][nextX] == 0 and visited[nextY][nextX][leftBreak] > nextM:
                    q.append((nextY, nextX, leftBreak))
                    visited[nextY][nextX][leftBreak] = nextM

    return -1


def main():
    Y, X, K = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(map(int, input().decode().strip())))

    print(BFS(Y, X, K, grid))


main()
