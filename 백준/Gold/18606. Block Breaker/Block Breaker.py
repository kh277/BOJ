# 백준 18606

'''
떨어지는 블록은 visit값을 4로 설정한다.
가로쪽이 뚫린 경우 visit | 1, 세로쪽이 뚫린 경우 visit | 2로 처리를 해 준다.
visit가 3인 경우 가로, 세로가 빈 블록이므로 visit를 4로 설정한 뒤, 큐에 넣고 계속 탐색해준다.
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
add = [1, 1, 2, 2]


def BFS(Y, X, visited, tY, tX):
    # 이미 방문한 경우
    if visited[tY][tX] == 4:
        return 0

    # 시작값 추가
    q = deque()
    q.append((tY, tX))
    visited[tY][tX] = 4
    count = 1

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0 <= nextX < X and 0 <= nextY < Y and visited[nextY][nextX] != 4:
                visited[nextY][nextX] |= add[i]

                # 떨어지는 블록인 경우
                if visited[nextY][nextX] == 3:
                    visited[nextY][nextX] = 4
                    q.append((nextY, nextX))
                    count += 1

    return count


def main():
    T = int(input())
    for _ in range(T):
        Y, X, Q = map(int, input().split())
        visited = [[0] * X for _ in range(Y)]
        for _ in range(Q):
            y, x = map(int, input().split())
            print(BFS(Y, X, visited, y-1, x-1))


main()
