# 백준 20419

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
move = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def BFS(Y, X, K, grid):
    visited = [[[0] * 4 for _ in range(X)] for _ in range(Y)]
    q = deque()
    visited[0][0][0] = 1
    q.append((0, 0, 0))

    while q:
        curY, curX, status = q.popleft()
        curWay = move[grid[curY][curX]]

        # 왼쪽으로 회전시키는 경우
        if status == 0 or status == 2:
            nextWay = (curWay+3) % 4
            nextX = curX + dx[nextWay]
            nextY = curY + dy[nextWay]
            nextStatus = status + 1
            if 0 <= nextX < X and 0 <= nextY < Y and visited[nextY][nextX][nextStatus] == 0:
                q.append((nextY, nextX, nextStatus))
                visited[nextY][nextX][nextStatus] = 1

        # 오른쪽으로 회전시키는 경우
        if status == 0 or status == 1:
            nextWay = (curWay+1) % 4
            nextX = curX + dx[nextWay]
            nextY = curY + dy[nextWay]
            nextStatus = status + 2
            if 0 <= nextX < X and 0 <= nextY < Y and visited[nextY][nextX][nextStatus] == 0:
                q.append((nextY, nextX, nextStatus))
                visited[nextY][nextX][nextStatus] = 1

        # 그대로 움직이는 경우
        nextX = curX + dx[curWay]
        nextY = curY + dy[curWay]
        if 0 <= nextX < X and 0 <= nextY < Y and visited[nextY][nextX][status] == 0:
            q.append((nextY, nextX, status))
            visited[nextY][nextX][status] = 1

    if K == 0 and visited[Y-1][X-1][0] == 1:
        return 'Yes'
    elif K == 1 and max(visited[Y-1][X-1]) == 1:
        return 'Yes'
    return 'No'


def main():
    Y, X, K = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(input().decode().strip()))

    print(BFS(Y, X, K, grid))


main()
