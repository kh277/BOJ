# 백준 3190

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, apple, moveChange):
    pointX = [0, 1, 0, -1]
    pointY = [-1, 0, 1, 0]
    curX = 0
    curY = 0 
    curDir = 1      # 0 = 상, 1 = 우, 2 = 하, 3 = 좌 순서로 저장
    curTime = 1
    q = deque()
    q.append((0, 0))

    while True:
        # 움직임 처리
        curX += pointX[curDir]
        curY += pointY[curDir]

        if 0 <= curX < N and 0 <= curY < N:
            # 몸과 부딪히는지 체크
            for qy, qx in q:
                if curY == qy and curX == qx:
                    return curTime

            # 이동 및 사과 체크
            q.append((curY, curX))
            if (curY, curX) in apple:
                del apple[(curY, curX)]
            else:
                q.popleft()

            # 방향 전환 체크
            if curTime in moveChange:
                curDir = (curDir + moveChange[curTime]) % 4
            curTime += 1

        # 벽과 부딪힌 경우
        else:
            return curTime


def main():
    N = int(input())
    K = int(input())
    apple = dict()
    for _ in range(K):
        a, b = map(int, input().split())
        apple[(a-1, b-1)] = 1
    L = int(input())
    moveChange = dict()
    for _ in range(L):
        a, b = map(str, input().decode().strip().split())
        moveChange[int(a)] = -1 if b == 'L' else 1
    print(solve(N, apple, moveChange))


main()
