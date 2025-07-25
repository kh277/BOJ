# 백준 6798

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
MAX = 8


def BFS(start, end):
    visited = [[-1 for _ in range(MAX)] for _ in range(MAX)]
    q = deque()
    q.append([start[0], start[1], 0])
    visited[start[0]][start[1]] = 0

    while q:
        curY, curX, count = q.popleft()

        if [curY, curX] == end:
            return count

        for i in range(8):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < MAX and 0 <= nextY < MAX and visited[nextY][nextX] == -1:
                q.append([nextY, nextX, count+1])
                visited[nextY][nextX] = count+1


def main():
    sY, sX = map(int, input().split())
    eY, eX = map(int, input().split())
    
    print(BFS([sY-1, sX-1], [eY-1, eX-1]))


main()
