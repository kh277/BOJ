# 백준 12701

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 10007
dy = [1, 2]
dx = [2, 1]


def solve(Y, X, DP):
    # 목표에 도달할 수 없는 경우
    if (X + Y - 2) % 3 != 0:
        return 0

    DP[0][0] = 1
    if X >= 3 and DP[1][2] == 0:
        DP[1][2] = 1
    if Y >= 3 and DP[2][1] == 0:
        DP[2][1] = 1

    # DP 계산
    for curY in range(2, Y):
        for curX in range(2, X):
            if DP[curY][curX] == -1:
                continue
            for i in range(2):
                prevX = curX - dx[i]
                prevY = curY - dy[i]
                if prevX >= 0 and prevY >= 0 and DP[prevY][prevX] != -1:
                    DP[curY][curX] += DP[prevY][prevX]
            DP[curY][curX] %= MOD

    return DP[Y-1][X-1]


def main():
    T = int(input())
    for i in range(1, T+1):
        Y, X, R = map(int, input().split())
        DP = [[0] * X for _ in range(Y)]
        for _ in range(R):
            y, x = map(int, input().split())
            DP[y-1][x-1] = -1
        print(f"Case #{i}: {solve(Y, X, DP)}")


main()
