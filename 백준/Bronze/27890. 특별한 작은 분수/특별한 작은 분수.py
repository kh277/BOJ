# 백준 17912

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(x0, N):
    xt = x0
    for _ in range(N):
        if xt % 2 == 0:
            xt = xt//2 ^ 6
        else:
            xt = (2*xt)^6

    return xt


def main():
    x0, N = map(int, input().split())
    print(solve(x0, N))


main()
