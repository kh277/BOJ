# 백준 16988

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# start가 위치한 상대 돌을 잡을 수 있는지 여부 및 개수 반환
def BFS(N, M, grid, visited, start):
    q = deque()
    q.append(start)
    canEscape = False
    visited[start[0]][start[1]] = 1
    catchCount = 1

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < M and 0 <= nextY < N and visited[nextY][nextX] == 0:
                if grid[nextY][nextX] == 2:
                    q.append((nextY, nextX))
                    visited[nextY][nextX] = 1
                    catchCount += 1
                elif grid[nextY][nextX] == 0:
                    canEscape = True

    if canEscape == False:
        return catchCount
    return 0


# 현재 grid 배치에서 잡히는 '2' 돌이 몇개나 있는지 체크
def catch(N, M, grid):
    result = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for y in range(N):
        for x in range(M):
            # 상대 돌의 위치에서 BFS 탐색
            if visited[y][x] == 0 and grid[y][x] == 2:
                result += BFS(N, M, grid, visited, (y, x))

    return result


def solve(N, M, grid):
    result = 0

    # 점을 2개 잡고 잡히는 돌의 개수 체크
    for aY in range(N):
        for aX in range(M):
            if grid[aY][aX] != 0:
                continue
            grid[aY][aX] = 1

            for bY in range(aY, N):
                for bX in range(M):
                    if grid[bY][bX] != 0 or (aX == bX and aY == bY):
                        continue

                    grid[bY][bX] = 1
                    result = max(result, catch(N, M, grid))
                    grid[bY][bX] = 0
            grid[aY][aX] = 0

    return result


def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    print(solve(N, M, grid))


main()
