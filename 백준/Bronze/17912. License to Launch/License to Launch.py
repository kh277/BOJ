# 백준 17912

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, day):
    minD = min(day)
    for i in range(N):
        if day[i] == minD:
            return i


def main():
    N = int(input())
    day = list(map(int, input().split()))
    print(solve(N, day))


main()
