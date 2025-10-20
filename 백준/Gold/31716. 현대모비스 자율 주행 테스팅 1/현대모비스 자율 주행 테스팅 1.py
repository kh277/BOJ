# 백준 31716

import io
from collections import deque
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**15
dx = [0, 0, 1]
dy = [-1, 1, 0]


def BFS(N, road, start):
    # BFS로 한 트랙을 완주할 수 있는지 체크
    result = [INF, INF]
    visited = [array('q', [0]) * N for _ in range(2)]
    q = deque()

    if road[start[0]][start[1]] == '.':
        q.append([start[0], start[1], 0])
        visited[start[0]][start[1]] ^= 1

    while q:
        curY, curX, count = q.popleft()
        if curX == N-1:
            result[curY] = count

        for i in range(3):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < N and 0 <= nextY < 2 and visited[nextY][nextX] == 0 and road[nextY][nextX] == '.':
                q.append([nextY, nextX, count+1])
                visited[nextY][nextX] ^= 1

    return result


def solve(N, K, road):
    A = BFS(N, road, [0, 0])
    B = BFS(N, road, [1, 0])
    
    if K == 1:
        return min(min(A), min(B))
    elif A[0] == INF and B[1] == INF:
        return -1

    return min(min(A[0], B[0]) + A[0]*(K-2) + min(A) + K-1,\
                min(A[1], B[1]) + B[1]*(K-2) + min(B) + K-1)


def main():
    N, K = map(int, input().split())
    road = []
    for _ in range(2):
        road.append(list(input().decode().strip()))

    print(solve(N, K, road))


main()
