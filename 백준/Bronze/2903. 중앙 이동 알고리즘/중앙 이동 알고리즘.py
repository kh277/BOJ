# 백준 2903

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    cur = 3
    for _ in range(1, N):
        cur = cur*2 - 1

    return cur**2


def main():
    N = int(input())
    print(solve(N))


main()
