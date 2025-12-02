# 백준 25993

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, points):
    maxAngle = 0

    # 시작점으로부터의 시야각 계산
    for i in range(1, N-1):
        curAngle = 180 * math.atan((points[i][1])/(points[i][0]-points[0][0])) / math.pi
        maxAngle = max(maxAngle, curAngle)

    # 끝점으로부터의 시야각 계산
    for i in range(N-2, 0, -1):
        curAngle = 180 * math.atan((points[i][1])/(points[N-1][0]-points[i][0])) / math.pi
        maxAngle = max(maxAngle, curAngle)

    return maxAngle


def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))

    print(solve(N, points))


main()
