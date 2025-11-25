# 백준 34006

'''
전체 게이지의 합은 항상 3N으로 일정하므로 x축을 궁기 게이지, y축을 도올 게이지로 보고, 혼돈 게이지는 x, y값을 계산하여 사용한다.
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, start, delta, visited):
    dx = [delta[0], -delta[1], 0]
    dy = [0, delta[1], -delta[2]]
    maxG = 2*N
    tMaxG = 3*N

    q = deque()
    q.append((start[1], start[0]))
    visited[start[1]][start[0]] = 4

    while q:
        curY, curX = q.popleft()

        if curY == N and curX == N:
            return

        for i in range(3):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if 0 <= nextX < maxG and 0 <= nextY < maxG and N < nextX+nextY < tMaxG and visited[nextY][nextX] == -1:
                visited[nextY][nextX] = i
                q.append((nextY, nextX))


def solve(N, start, delta):
    # BFS 탐색
    visited = [[-1 for _ in range(2*N)] for _ in range(2*N)]
    BFS(N, start, delta, visited)

    # 게이지를 안정화하지 못한 경우
    if visited[N][N] == -1:
        return [-1]

    # 피격 순서 역추적
    traceback = []
    curX = N
    curY = N
    while True:
        curV = visited[curY][curX]
        if curV == 4:
            break
        elif curV == 0:
            traceback.append('A')
            curX -= delta[0]
        elif curV == 1:
            traceback.append('B')
            curX += delta[1]
            curY -= delta[1]
        elif curV == 2:
            traceback.append('C')
            curY += delta[2]
    return [len(traceback), ''.join(traceback[::-1])]


def main():
    N = int(input())
    start = tuple(map(int, input().split()))
    delta = tuple(map(int, input().split()))

    for i in solve(N, start, delta):
        print(i)


main()
