# 백준 14442

'''
visited[y][x] = [y, x]에 도착하기 위해 사용한 파괴 횟수
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 1000000000


def BFS(Y, X, K, grid):
    visited = [[-1] * X for _ in range(Y)]
    q = deque()
    q.append((0, 0, K, 1))
    visited[0][0] = K

    while q:
        curY, curX, leftBreak, dist = q.popleft()

        # 도착점에 도달한 경우
        if curX == X-1 and curY == Y-1:
            return dist

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < X and 0 <= nextY < Y:
                # 다음 칸이 벽이고 더 많은 파괴 횟수를 남겼다면
                if grid[nextY][nextX] == '1' and leftBreak > 0 and visited[nextY][nextX] < leftBreak - 1:
                    q.append((nextY, nextX, leftBreak-1, dist+1))
                    visited[nextY][nextX] = leftBreak-1

                # 다음 칸이 일반 칸이고, 더 많은 파괴 횟수를 남겼다면
                elif grid[nextY][nextX] == '0' and visited[nextY][nextX] < leftBreak:
                    q.append((nextY, nextX, leftBreak, dist+1))
                    visited[nextY][nextX] = leftBreak

    return -1


def main():
    Y, X, K = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(input().decode().strip()))

    print(BFS(Y, X, K, grid))


main()
