# 백준 14597

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(Y, X, A, B):
    DP = [[0] * X for _ in range(Y)]
    for x in range(X):
        DP[0][x] = (A[0][x]-B[0][x])**2

    for y in range(1, Y):
        for x in range(X):
            cur = (A[y][x]-B[y][x])**2
            prev = DP[y-1][x]
            if x > 0:
                prev = min(prev, DP[y-1][x-1])
            if x < X-1:
                prev = min(prev, DP[y-1][x+1])
            DP[y][x] = cur + prev

    return min(DP[Y-1])


def main():
    Y, X = map(int, input().split())
    A = []
    B = []
    for _ in range(Y):
        A.append(list(map(int, input().split())))
    for _ in range(Y):
        B.append(list(map(int, input().split())))
    print(solve(Y, X, A, B))


main()
