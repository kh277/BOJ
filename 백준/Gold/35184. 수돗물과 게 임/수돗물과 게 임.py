# 백준 35184

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
INF = 10**9


def pqBFS(Y, X, T, grid, start):
    pq = [(start)]
    visited = [[[INF] * 4 for _ in range(X)] for _ in range(Y)]
    visited[start[1]][start[2]][start[3]] = 0
    result = INF

    while pq:
        curT, curY, curX, curW = heapq.heappop(pq)

        # 바다일 경우
        if grid[curY][curX] == 'S':
            result = min(result, curT)

        # 수돗물일 경우
        elif grid[curY][curX] == 'T':
            noSearch = False
            while grid[curY][curX] == 'T':
                nextW = (curW + 1) % 4
                nextX = curX + dx[nextW]
                nextY = curY + dy[nextW]
                if 0 <= nextX < X and 0 <= nextY < Y:
                    if visited[nextY][nextX][nextW] > visited[curY][curX][curW]:
                        visited[nextY][nextX][nextW] = visited[curY][curX][curW]
                        curX = nextX
                        curY = nextY
                        curW = nextW
                    else:
                        noSearch = True
                        break
                else:
                    noSearch = True
                    break
            if noSearch == False:
                heapq.heappush(pq, (curT, curY, curX, curW))
                visited[curY][curX][curW] = curT
        # 일반 칸일 경우
        else:
            # 회전하는 경우
            nextW = (curW + 1) % 4
            nextT = curT + T
            if visited[curY][curX][nextW] > nextT:
                heapq.heappush(pq, (nextT, curY, curX, nextW))
                visited[curY][curX][nextW] = nextT
            # 이동하는 경우
            for i in [1, 3]:
                way = (curW + i) % 4
                nextY = curY + dy[way]
                nextX = curX + dx[way]
                nextT = curT + 1
                if 0 <= nextX < X and 0 <= nextY < Y and visited[nextY][nextX][curW] > nextT:
                    heapq.heappush(pq, (nextT, nextY, nextX, curW))
                    visited[nextY][nextX][curW] = nextT

    if result == INF:
        return -1
    return result


def solve(Y, X, T, grid):
    for y in range(Y):
        for x in range(X):
            cur = grid[y][x]
            if cur != '.' and cur != 'T' and cur != 'S':
                return pqBFS(Y, X, T, grid, (0, y, x, int(cur)))


def main():
    Y, X, T = map(int, input().split())
    grid = []
    for _ in range(Y):
        grid.append(list(input().decode().strip()))
    print(solve(Y, X, T, grid))


main()
