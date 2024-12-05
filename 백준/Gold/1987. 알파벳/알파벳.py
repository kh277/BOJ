# 백준 1987

import sys
from collections import deque

input = sys.stdin.readline
pointX = [-1, 1, 0, 0]
pointY = [0, 0, -1, 1]


def DFS(startY, startX):
    result = 0
    q = deque()
    q.append([startY, startX, set(board[startY][startX])])

    while q:
        curY, curX, curVisit = q.pop()
        result = max(result, len(curVisit))

        for i in range(4):
            nextX = curX + pointX[i]
            nextY = curY + pointY[i]

            if 0 <= nextX < C and 0 <= nextY < R and board[nextY][nextX] not in curVisit:
                q.append([nextY, nextX, curVisit | {board[nextY][nextX]}])

    return result


# main 함수 ----------
R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(list(input().rstrip()))

print(DFS(0, 0))
