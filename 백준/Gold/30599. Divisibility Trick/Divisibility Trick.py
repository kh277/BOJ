# 백준 30599

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    return str(N) * N


def main():
    N = int(input())
    print(solve(N))


main()
