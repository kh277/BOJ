# 백준 27294

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(T, S):
    if 12 <= T <= 16 and S == 0:
        return 320
    return 280


def main():
    T, S = map(int, input().split())
    print(solve(T, S))


main()