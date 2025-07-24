# 백준 2210

import io
from array import array
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
SIZE = 5
result = set()


def DFS(start, grid):
    q = deque()
    q.append([start[0], start[1], [grid[start[0]][start[1]]]])

    while q:
        curY, curX, move = q.pop()

        if len(move) == 6:
            result.add(''.join(move))
            continue

        for i in range(4):
            nextY = curY + dy[i]
            nextX = curX + dx[i]

            if 0 <= nextX < SIZE and 0 <= nextY < SIZE:
                q.append([nextY, nextX, move + [grid[nextY][nextX]]])


def solve(grid):
    for y in range(SIZE):
        for x in range(SIZE):
            DFS((y, x), grid)
    
    return len(result)


def main():
    grid = [list(input().decode().split()) for _ in range(SIZE)]
    print(solve(grid))


main()
