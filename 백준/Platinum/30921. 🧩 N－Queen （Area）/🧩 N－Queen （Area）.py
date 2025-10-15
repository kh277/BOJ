# 백준 30921

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, point):
    area = 0

    for i in range(4):
        j = (i+1) % 4
        area += point[i*2] * point[j*2+1]
        area -= point[i*2+1] * point[j*2]

    return abs(area) / 2 / N


def main():
    N = int(input())
    L = list(map(int, input().split()))

    print(solve(N, L))


main()
