# 백준 1669

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(X, Y):
    if X == Y:
        return 0

    gap = Y - X
    N = math.ceil(gap**0.5)

    if N*N - N < gap <= N*N:
        return 2*N-1
    return 2*N-2


def main():
    X, Y = map(int, input().split())
    print(solve(X, Y))


main()
