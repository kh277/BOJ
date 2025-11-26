# 백준 7187

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
addX = [-1, 1, 0, 0, 0]
addY = [0, 0, -1, 1, 0]
MAX_SPEED = 7
BORDER_SPEED = 15
MAX = 30
BORDER = 60
INF = 10**5


# 선분 교차 판정 서브 함수
def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


# 선분 교차 판정
def LineIntersection(A, B, C, D):
    AB = CCW(A, B, C) * CCW(A, B, D)
    CD = CCW(C, D, A) * CCW(C, D, B)

    if AB == 0 and CD == 0:
        if B < A:
            A, B = B, A
        if D < C:
            C, D = D, C
        return not (B < C or D < A)

    return AB <= 0 and CD <= 0


# 선분 AB와 교차하는 다른 선분이 존재하는지 체크
def checkLines(N, lines, A, B):
    for i in range(N):
        if LineIntersection(A, B, (lines[i][0], lines[i][1]), (lines[i][2], lines[i][3])) == 1:
            return True
    return False


def BFS(N, lines, endX, endY):
    q = deque()
    visited = [[[[INF for _ in range(15)] for _ in range(15)] for _ in range(BORDER)] for _ in range(BORDER)]
    q.append((MAX, MAX, 0, 0))
    visited[MAX][MAX][7][7] = 0

    while q:
        curY, curX, dy, dx = q.popleft()

        if curX == endX and curY == endY:
            return visited[endY][endX][dy+7][dx+7]

        for i in range(5):
            moveX = dx + addX[i]
            moveY = dy + addY[i]
            nextX = curX + moveX
            nextY = curY + moveY
            
            if 0 <= nextX < BORDER and 0 <= nextY < BORDER and -7 <= moveX <= 7 and -7 <= moveY <= 7 and visited[nextY][nextX][moveY+7][moveX+7] == INF and checkLines(N, lines, (curX, curY), (nextX, nextY)) == False:
                q.append((nextY, nextX, moveY, moveX))
                visited[nextY][nextX][moveY+7][moveX+7] = visited[curY][curX][dy+7][dx+7] + 1

    return -1


def main():
    endX, endY, N = map(int, input().split())
    lines = []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        lines.append((a+MAX, b+MAX, c+MAX, d+MAX))

    print(BFS(N, lines, endX+MAX, endY+MAX))


main()
