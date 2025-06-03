# 백준 9063

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(pointX, pointY):
    return (max(pointX) - min(pointX)) * (max(pointY) - min(pointY))


def main():
    pointX = []
    pointY = []
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        pointX.append(x)
        pointY.append(y)

    print(solve(pointX, pointY))


main()
