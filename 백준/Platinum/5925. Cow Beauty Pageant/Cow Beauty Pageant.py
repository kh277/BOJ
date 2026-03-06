# 백준 5925

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1000000000
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# start와 이어진 섬을 라벨링 및 해당 섬에 속한 좌표 반환
def BFS(Y, X, grid, start, label):
    q = deque()
    q.append(start)
    grid[start[0]][start[1]] = label
    part = [start[0]*100 + start[1]]

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < X and 0 <= nextY < Y and grid[nextY][nextX] == 'X':
                q.append((nextY, nextX))
                part.append(nextY*100+nextX)
                grid[nextY][nextX] = label

    return part


# label번 섬을 시작점으로 잡고, 다른 좌표까지 도달하기 위한 거리 계산 
def BFS2(Y, X, grid, dist, starts, label):
    q = deque()
    for i in starts:
        y, x = divmod(i, 100)
        q.append((y, x))
        dist[y][x][label] = 0
    
    while q:
        curY, curX = q.popleft()
        move = dist[curY][curX][label]

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < X and 0 <= nextY < Y and grid[nextY][nextX] == '.' and dist[nextY][nextX][label] > move+1:
                q.append((nextY, nextX))
                dist[nextY][nextX][label] = move+1


# label번과 label+1번 섬을 최단거리로 이을 때 필요한 거리 계산
def BFS3(Y, X, grid, dist, starts, label):
    otherLabel = (label+1) % 3
    visited = [[0] * X for _ in range(Y)]
    q = deque()
    for i in starts:
        y, x = divmod(i, 100)
        q.append((y, x))
        visited[y][x] = 1

    minDist = INF
    while q:
        curY, curX = q.popleft()

        if grid[curY][curX] == '.':
            minDist = min(dist[curY][curX][label] + dist[curY][curX][otherLabel] - 1, minDist)
            continue

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < X and 0 <= nextY < Y and grid[nextY][nextX] == '.' and visited[nextY][nextX] == 0:
                q.append((nextY, nextX))
                visited[nextY][nextX] = 1

    return minDist


def solve(Y, X, grid):
    # 전처리 - 세 점에 속하는 격자를 0, 1, 2으로 라벨링
    land = []
    label = 0
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 'X':
                t = BFS(Y, X, grid, (y, x), label)
                land.append(t)
                label += 1

    # 케이스1 : 특정한 한 좌표를 잡고 나머지 세 점까지 최단거리로 잇기
    dist = [[[INF] * 3 for _ in range(X)] for _ in range(Y)]
    for i in range(3):
        BFS2(Y, X, grid, dist, land[i], i)
    result = INF
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == '.':
                result = min(sum(dist[y][x])-2, result)

    # 케이스2 : 섬 3개 중 2개의 섬을 최단거리로 잇는 경로 3개를 도출하고 최소값 2개 선택
    minDist = [INF, INF, INF]
    for i in range(3):
        minDist[i] = BFS3(Y, X, grid, dist, land[i], i)
    result = min(sum(minDist) - max(minDist), result)

    return result


def main():
    Y, X = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(input().decode().strip()))
    print(solve(Y, X, grid))


main()
