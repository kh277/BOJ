# 백준 16117

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(X, Y, silver):
    # 정수 좌표 시작 DP
    DP = [[0] * X for _ in range(Y)]
    for x in range(X):
        DP[0][x] = silver[0][x]
    for y in range(1, Y):
        for x in range(X):
            if x > 0:       # 위로 이동
                DP[y][x] = max(DP[y][x], DP[y-1][x-1] + silver[y][x])
            if x < X-1:     # 아래로 이동
                DP[y][x] = max(DP[y][x], DP[y-1][x+1] + silver[y][x])
            if y > 1:       # 앞으로 이동
                DP[y][x] = max(DP[y][x], DP[y-2][x] + silver[y-1][x] + silver[y][x])
            if y == 1:      # -1에서 앞으로 이동
                DP[y][x] = max(DP[y][x], DP[y-1][x] + silver[y][x])
            if y == Y-1:    # Y-1에서 앞으로 이동
                DP[y][x] = max(DP[y][x], DP[y-1][x] + silver[y][x])

    result = max(DP[Y-1])

    # .5 좌표 시작 DP
    DP = [[0] * (X+1) for _ in range(Y+1)]
    for y in range(1, Y+1):
        DP[y][0] = DP[y-1][1] + silver[y-1][0]
        DP[y][X] = DP[y-1][X-1] + silver[y-1][X-1]
        for x in range(1, X):
            DP[y][x] = max(DP[y-1][x-1] + silver[y-1][x-1], DP[y-1][x+1] + silver[y-1][x])

    result = max(result, max(DP[Y]))
    return result


def main():
    X, Y = map(int, input().split())
    silver = [[0] * X for _ in range(Y)]
    for x in range(X):
        for y, v in enumerate(list(map(int, input().split()))):
            silver[y][x] = v

    print(solve(X, Y, silver))


main()
