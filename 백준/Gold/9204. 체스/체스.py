# 백준 9204

'''
두 좌표가 같은 색의 칸에 있다면 항상 2번 이내의 이동으로 이동할 수 있다.
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(startY, startX, endY, endX):
    # 0번만에 도착 가능한 경우
    if startY == endY and startX == endX:
        return f"0 {chr(startX + ord('A'))} {startY+1}"

    # 도착 불가능한 경우
    elif (startX + startY) % 2 != (endX + endY) % 2:
        return "Impossible"

    visited = [[False for _ in range(8)] for _ in range(8)]
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    q = deque()
    q.append([startY, startX, [[startY, startX]]])
    visited[startY][startX] = True

    while q:
        curY, curX, curVisit = q.popleft()
        if curX == endX and curY == endY:
            return f"{len(curVisit)-1} {' '.join([chr(i[1] + ord('A')) + ' ' + str(i[0]+1) for i in curVisit])}"

        for i in range(4):
            nextX = curX
            nextY = curY
            while True:
                nextX = nextX + dx[i]
                nextY = nextY + dy[i]
                if 0 <= nextX < 8 and 0 <= nextY < 8 and visited[nextY][nextX] == False:
                    q.append([nextY, nextX, curVisit + [[nextY, nextX]]])
                    visited[nextY][nextX] = True
                else:
                    break


def main():
    T = int(input())
    for _ in range(T):
        sx, sy, ex, ey = input().decode().split()
        print(solve(int(sy)-1, ord(sx)-ord('A'), int(ey)-1, ord(ex)-ord('A')))


main()
