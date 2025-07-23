# 백준 6304

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 이웃한 'X' 탐색
def BFSX(W, H, start, grid):
    XVisited = [[0 for _ in range(W)] for _ in range(H)]
    dotVisited = set()
    q = deque()
    q.append(start)
    XVisited[start[0]][start[1]] = 1
    dotVisited.add((start[0], start[1]))

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < W and 0 <= nextY < H and grid[nextY][nextX] == 'X' and XVisited[nextY][nextX] == 0:
                q.append([nextY, nextX])
                XVisited[nextY][nextX] = 1
                dotVisited.add((nextY, nextX))

    return dotVisited


# 이웃한 '*', 'X' 탐색
def BFS(W, H, start, grid, visited):
    count = 0
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    dotVisited = set()

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < W and 0 <= nextY < H and grid[nextY][nextX] != '.' and visited[nextY][nextX] == 0:
                # 다음이 'X'인 경우, BFS로 붙어있는 X의 개수 세기 및 방문처리
                if grid[nextY][nextX] == 'X':
                    if (nextY, nextX) not in dotVisited:
                        count += 1
                    dotVisited = dotVisited | BFSX(W, H, [nextY, nextX], grid)
                q.append([nextY, nextX])
                visited[nextY][nextX] = 1

    return count


def solve(W, H, grid):
    result = []
    visited = [[0 for _ in range(W)] for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if grid[y][x] == '*' and visited[y][x] == 0:
                result.append(BFS(W, H, [y, x], grid, visited))

    return sorted(result)


def main():
    T = 1
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        grid = []
        for _ in range(H):
            grid.append(list(input().decode().strip()))

        print(f"Throw {T}")
        print(*solve(W, H, grid))
        print()
        T += 1


main()
