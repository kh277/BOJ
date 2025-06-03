# 백준 3009

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(pointX, pointY):
    return [pointX[0] ^ pointX[1] ^ pointX[2], pointY[0] ^ pointY[1] ^ pointY[2]]


def main():
    pointX = []
    pointY = []
    for _ in range(3):
        x, y = map(int, input().split())
        pointX.append(x)
        pointY.append(y)

    print(*solve(pointX, pointY))


main()
