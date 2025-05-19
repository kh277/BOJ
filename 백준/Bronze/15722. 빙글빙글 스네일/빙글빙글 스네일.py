# 백준 15722

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solve(N):
    move = 1
    accMove = 0
    angle = 0
    curY = 0
    curX = 0

    while True:
        for _ in range(2):
            # 이번 움직임에 목표에 도착한다면
            if accMove + move >= N:
                return [curX + dx[angle]*(N-accMove), curY + dy[angle]*(N-accMove)]
            
            curX += dx[angle] * move
            curY += dy[angle] * move
            angle = (angle + 1) % 4
            accMove += move

        move += 1


def main():
    N = int(input())
    print(*solve(N))


main()
